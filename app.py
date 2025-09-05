import cv2
import os
import sys
import subprocess
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Initialize Flask
app = Flask(__name__)

# Upload folder and allowed extensions
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "gif", "tiff"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Function to open URLs
def open_url(url):
    if sys.platform == "win32":
        subprocess.run(["start", url], shell=True)
    elif sys.platform == "darwin":
        subprocess.run(["open", url])
    else:
        subprocess.run(["xdg-open", url])

# Check allowed files
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# QR Code scanner
def scan_qr_code(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Could not read image {image_path}")
        return None, None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = cv2.QRCodeDetector()

    # Apply thresholding
    _, thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    value, pts, _ = detector.detectAndDecode(thresh_img)

    # Save result image
    result_image_path = os.path.join(app.config["UPLOAD_FOLDER"], "result.png")
    cv2.imwrite(result_image_path, frame)

    return value, result_image_path

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        value, result_image_path = scan_qr_code(file_path)

        if value:
            if value.startswith("http://") or value.startswith("https://"):
                open_url(value)
            return render_template("result.html", value=value, image_path=result_image_path)
        else:
            return render_template("result.html", value=None, image_path=result_image_path)

    return redirect(request.url)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)