📌 Project Overview

This project is a QR Code Scanner Web Application built using Flask (Python web framework) and OpenCV (computer vision library).
It provides a simple web interface where users can upload images containing QR codes. The application then processes the image, extracts the QR code content, and displays the result. If the QR code contains a URL, the app will automatically open the link in the browser.

This project demonstrates how computer vision and web technologies can be combined to build practical tools.

🎯 Objectives

Provide an easy-to-use web interface for scanning QR codes.

Support multiple image formats like PNG, JPG, JPEG, BMP, GIF, and TIFF.

Automatically decode QR codes using OpenCV’s built-in detector.

Enable automatic redirection when a URL is detected.

Allow users to view scanned results and download processed images.

🏗️ Technologies Used

Python 3.7+

Flask – lightweight Python web framework

OpenCV – for QR code detection and image processing

NumPy – for image array manipulations

Werkzeug – for handling secure file uploads

HTML / Jinja2 Templates – for rendering web pages

⚙️ How It Works

User Uploads Image
The user selects and uploads an image file containing a QR code via the web form.

File Validation
The app checks if the uploaded file has a valid extension (png, jpg, jpeg, bmp, gif, tiff).

QR Code Detection

The image is read using OpenCV.

Converted to grayscale.

Thresholding (OTSU) is applied to enhance QR detection.

OpenCV’s QRCodeDetector extracts the encoded value.

Result Handling

If decoding is successful, the value is displayed on the result page.

If the value is a URL, the browser automatically opens the link.

A processed version of the image is saved for reference.

Result Display

Users see the decoded value on the webpage.

They can view/download the result image (stored in the uploads/ folder).

📈 Future Enhancements

Add support for multiple QR codes in one image.

Allow users to download decoded text as a .txt file.

Enable drag-and-drop uploads.

Add history/logging of past scans.

Build a Docker container for easier deployment.

Add API endpoint for programmatic QR code scanning.

<img width="489" height="362" alt="Screenshot 2025-10-05 074650" src="https://github.com/user-attachments/assets/0ada1308-f1a7-4757-8504-edb99a400b55" />

<img width="883" height="308" alt="Screenshot 2025-10-05 080324" src="https://github.com/user-attachments/assets/855d4d87-f087-4cc4-a46f-0e4ad497b6a7" />
