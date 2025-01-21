# Pose Detection Project  
This project leverages **MediaPipe** and **OpenCV** to detect and analyze human poses in real-time and static images. It includes features such as posture feedback, similarity comparison, and audio alerts for incorrect postures.  

## Features  
- **Real-Time Pose Detection:** Detect poses using a webcam and overlay landmarks.  
- **Image Pose Detection:** Analyze and detect poses from selected images.  
- **Posture Feedback:** Provides audio and text feedback on incorrect posture.  
- **Pose Comparison:** Compares real-time poses with a reference image.  
- **Audio Alerts:** Plays a beep sound for incorrect posture.  
- **Extensible:** Modular design for easy customization and extension.  

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/shanzayousaf/yoga-pose-match.git  
## Navigate to the project directory:
cd pose-detection  

## Create a virtual environment and activate it:
python -m venv venv  

# Windows  
venv\Scripts\activate  
# macOS/Linux  
source venv/bin/activate  

## Install dependencies:
pip install -r requirements.txt  

## Usage:
**Real-Time Pose Detection:**
Run the webcam.py script to detect poses using your webcam:
python scripts/webcam.py 

**Image Pose Detection:**
Run the image.py script to detect poses from an image:
python scripts/image.py  

**Pose Comparison:**
Run the compare.py script to compare a pose from your webcam to a reference image:
python scripts/compare.py  

**Audio Alerts:**
Configure the beep sound by replacing the beep.wav file in the assets/ directory.

**Posture Feedback:**
Run the feedback.py script for real-time feedback on posture:
python scripts/feedback.py  

## Project Structure:
pose-detection/  
├── scripts/  
│   ├── webcam.py        # Real-time pose detection  
│   ├── image.py         # Pose detection in images  
│   ├── compare.py       # Pose comparison with a reference image  
│   ├── audio.py         # Beep sound for posture alerts  
│   ├── feedback.py      # Audio feedback for posture  
├── assets/  
│   ├── beep.wav         # Audio file for alerts  
│   ├── reference.jpg    # Example reference image  
├── requirements.txt     # Python dependencies  
├── .gitignore           # Ignored files and directories  
├── README.md            # Project documentation  

## Dependencies:
MediaPipe
OpenCV
Pygame
pyttsx3
NumPy

## Contributing:
Contributions are welcome! If you'd like to contribute:

1. Fork the repository.

2. Create a new branch:
git checkout -b feature-name  

3. Commit your changes:
git commit -m "Add new feature"  

4. Push to your branch:
git push origin feature-name  

5. Create a pull request.

## Contact:
For questions or suggestions, feel free to contact me at **shanzayousaf2002@gmail.com**.
