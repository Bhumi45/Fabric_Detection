from flask import Flask, render_template, request, flash, redirect, url_for, session
from deployment.utils.common import delete_artifacts_folder
from werkzeug.utils import secure_filename
import os
import json
from io import BytesIO
from PIL import Image
import subprocess


app = Flask(__name__)
app.secret_key = os.urandom(24)  # Add secret key for flashing

# Allowed file extensions for uploaded images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check if the uploaded file is an allowed image format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def prediction():
    """
    This page allows the user to upload an image file with a suitable format (.png, .jpg, .jpeg)
    and checks whether the file is an image or not.
    
    If the file is an image, it is processed in memory (RAM) using Pillow.
    Then we execute the "execute_prediction_pipeline.py" file, return the prediction,
    and show the image along with the predicted label.
    """
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
            # Load image directly into memory
            img = Image.open(BytesIO(file.read()))

            # Run the prediction pipeline script (assuming it uses the processed image)
            subprocess.run(["python3", "execute_prediction_pipeline.py"])

            # Read the predicted label from the JSON file
            with open("artifacts_deployment/prediction/prediction_result.json", "r") as json_file:
                prediction_result = json.load(json_file)

            predicted_label = prediction_result.get('label', 'Unknown')

            # delete_artifacts_folder() will not be needed since no artifacts to be created

            # Show the image along with the label
            return render_template("predict.html", label=predicted_label)
        else:
            flash('File is not an image or invalid format. Please upload a .png, .jpg, or .jpeg file.')
            #delete_artifacts_folder()
            return redirect(request.url)

    return render_template("upload_image.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
