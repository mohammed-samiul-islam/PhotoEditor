🖼️ Image Batch Processing Tool (Python)

This project is a simple Python-based image processing script that automates bulk image editing using the Pillow (PIL) library. It reads all images from a specified input directory, applies a series of transformations, and saves the edited versions to an output folder with modified filenames.

✨ Features

Batch processes all images in a folder automatically

Applies sharpening filter for improved clarity

Converts images to grayscale

Rotates images by 90 degrees

Enhances image contrast for better visual quality

Saves edited images with a clean and consistent filename format

🛠️ Technologies Used

Python

Pillow (PIL) library

OS module for file handling

🔄 How It Works

The script scans the ./images directory for image files.

Each image is opened and processed with the following steps:

Sharpening filter applied

Converted to grayscale

Rotated by -90 degrees

Contrast enhanced by a factor of 1.5

The edited image is saved in the ./edited directory with _edited appended to the original filename.

📁 Example Output

Input:
photo1.jpg

Output:
photo1_edited.jpg

🎯 Use Cases

Automating repetitive image editing tasks

Preparing datasets for machine learning or computer vision projects

Bulk photo enhancement

Learning image manipulation with Python
