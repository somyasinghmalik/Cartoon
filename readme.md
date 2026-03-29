# Cartoonifier using OpenCV

##  Overview

This project converts real-world images into cartoon-style images using computer vision techniques such as bilateral filtering, edge detection, and color quantization.

##  Problem Statement

Modern tools for image stylization are either complex or require manual effort. This project automates the process of converting images into cartoon-like visuals.

##  Technologies Used

* Python
* OpenCV
* NumPy
* Tkinter (for GUI)

##  Methodology

1. Apply bilateral filtering for smoothing
2. Perform color quantization
3. Detect edges using Canny edge detection
4. Combine edges with simplified colors

##  How to Run

```bash
pip install -r requirements.txt
python main.py
```
##  Virtual Environment Setup (Recommended)

It is recommended to run this project inside a virtual environment to avoid dependency conflicts.

### Create and activate virtual environment:

**Windows:**

```bash
py -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```


##  Sample Output

Input Image → Cartoonified Output

##  Learning Outcomes

* Understanding of image processing techniques
* Hands-on with OpenCV
* GUI development using Tkinter

## Future Improvements

* Convert into web app (Flask/React)
* Add real-time webcam cartoonification
* Improve performance using vectorization
