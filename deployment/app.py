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

@app.route("/predict", methods=["POST"])
def prediction():
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            # Load the image in memory (Pillow)
            img = Image.open(BytesIO(file.read()))

            # Convert Pillow image to OpenCV format (NumPy array)
            img = np.array(img)

            # If the image has an alpha channel, remove it
            if img.shape[-1] == 4:
                img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

            # Create the PredictionPipeline object and pass the image to it
            prediction_pipeline = PredictionPipeline()
            predicted_label = prediction_pipeline.main(img)  # Pass the in-memory image

            # Show the result
            return render_template("predict.html", label=predicted_label)

        else:
            flash('File is not an image or invalid format. Please upload a .png, .jpg, or .jpeg file.')
            return redirect(request.url)

    return render_template("upload_image.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
