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
    if request.method == "POST":
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # Check if the user uploaded an image
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Check if the file is an allowed image file
        if file and allowed_file(file.filename):
            img = Image.open(BytesIO(file.read()))  # Process image in memory

            # Run the prediction pipeline script and capture the output
            result = subprocess.run(["python3", "execute_prediction_pipeline.py"], capture_output=True, text=True)
            
            # Parse the JSON output from the prediction script
            #WILL CHANGE IT SOON
            prediction_result = json.loads(result.stdout)
            predicted_label = prediction_result.get('label', 'Unknown')

            delete_artifacts_folder()

            # Show the result on the prediction page
            return render_template("predict.html", label=predicted_label)

        else:
            flash('File is not an image or invalid format. Please upload a .png, .jpg, or .jpeg file.')
            delete_artifacts_folder()
            return redirect(request.url)

    return render_template("upload_image.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
