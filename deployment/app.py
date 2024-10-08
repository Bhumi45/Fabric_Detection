from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from utils.common import delete_artifacts_folder
from werkzeug.utils import secure_filename
import os
import numpy as np
import pandas as pd
import subprocess
import json

app = Flask(__name__)

# We have to make it
@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/nested_cross_validation", methods=["GET", "POST"])
def nested_cross_validation():
    """
    On visiting this page a button should be shown to run the nested cross validation.
    If pressed then execute_cross_validation.py among other things.
    
    After the nested cross validation is done then another button should ask whether the user wants to train the model on the entire training data or not.
    If yes then execute_final_model_training.py
    """
    if request.method == "POST":
        if 'run_cross_validation' in request.form:
            subprocess.run(["python3", "execute_cross_validation.py"])
            flash("Nested cross-validation completed successfully.", "success")
            return redirect(url_for("nested_cross_validation"))

        elif 'train_final_model' in request.form:
            subprocess.run(["python3", "execute_final_model_training.py"])
            flash("Model training on the entire dataset completed successfully.", "success")
            
            # Redirect to the route that shows the classification report
            return redirect(url_for("classification_report"))

    return render_template("nested_cross_validation.html")


@app.route("/classification_report", methods=["GET"])
def classification_report():
    # Load the classification report from the JSON file
    with open("artifacts/model_evaluation/metrics/metrics.json", "r") as json_file:
        classification_report = json.load(json_file)

    # Pass the report to the template for rendering
    return render_template("classification_report.html", report=classification_report)





"""
    This page allows the user to upload an image file with a suitable format.(.png,.jpg,.jpeg)
    and also checks whether the file is an image or not.

    If the file is an image then it is saved at artifacts_deployment/data_ingestion/uploaded_images
    Then we execute the "execute_prediction_pipeline.py" file. This file will return us the label and
    then we show the image along with the label.
"""
# Define the upload folder and allowed file extensions
UPLOAD_FOLDER = 'artifacts_deployment/data_ingestion/uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Configure upload folder in Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the uploaded file is an allowed image format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, browser might submit an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # Check if the file is an allowed image file
        if file and allowed_file(file.filename):
            # Secure the filename
            filename = secure_filename(file.filename)
            
            # Save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Run the prediction pipeline script
            subprocess.run(["python3", "execute_prediction_pipeline.py"])

            # Read the predicted label from the JSON file
            with open("artifacts_deployment/prediction/prediction_result.json", "r") as json_file:
                prediction_result = json.load(json_file)

            predicted_label = prediction_result.get('label', 'Unknown')
            
            delete_artifacts_folder()
            
            # Show the image along with the label
            return render_template("prediction_result.html", filename=filename, label=predicted_label)
        else:
            flash('File is not an image or invalid format. Please upload a .png, .jpg, or .jpeg file.')
            delete_artifacts_folder()
            return redirect(request.url)
    
    return render_template("upload_image.html")



#Route for Serving Uploaded Files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)
