# object-detection
Step-by-Step Guide for YOLOv4-Tiny Setup and Configuration

Certainly! Here's a step-by-step guide for setting up YOLOv4-tiny with OpenCV on Ubuntu, including addressing common issues:

Step-by-Step Guide for YOLOv4-Tiny Setup and Configuration
1. Set Up Your Environment
1.1 Install Python and Pip:

   sudo apt update
   sudo apt install python3 python3-pip
1.2 Create and Activate a Virtual Environment:

   python3 -m venv yolov4-tiny-env
   source yolov4-tiny-env/bin/activate
2. Install Required Python Packages
2.1 Upgrade Pip and Install OpenCV:

   pip install --upgrade pip
   pip install opencv-python-headless
3. Download YOLOv4-Tiny Files
3.1 Download YOLOv4-Tiny Configuration and Weights:

YOLOv4-Tiny Configuration (yolov4-tiny.cfg)

YOLOv4-Tiny Weights (yolov4-tiny.weights)

3.2 Download COCO Class Labels File (coco.names):

You can download the coco.names file from the official YOLO website.

3.3 Place All Files in a Directory:

   mkdir ~/yolo
   mv yolov4-tiny.cfg yolov4-tiny.weights coco.names ~/yolo/
4. Write Your YOLOv4-Tiny Python Script
5. Run Your Python Script
5.1 Execute the Script:

   python3 main.py

6. Troubleshooting Common Issues
6.1 QT Platform Plugin Error: (Using SSH)

If you encounter the error qt.qpa.xcb: could not connect to display, ensure you have the correct display environment or try running the script with DISPLAY set.

6.2 Lag Issues:

If the video is laggy, consider optimizing the script or using a smaller model like YOLOv4-tiny.

6.3 OpenCV cv2.error:

Ensure that paths to configuration and weights files are correct. Double-check if the files are accessible and properly formatted.

7. Optimizations
7.1 Reduce Image Size:

Consider using a smaller image size for processing to improve performance.

7.2 Use YOLOv4-tiny:

YOLOv4-tiny is faster than the full YOLOv4 model and suitable for real-time applications.

Feel free to customize or expand on this documentation based on your specific needs or setup.
