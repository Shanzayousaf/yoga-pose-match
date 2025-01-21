import pyttsx3
import threading

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Set the speech rate (default is typically around 200)
tts_engine.setProperty("rate", 150)

def speak_feedback(feedback_messages):
    """
    Convert a list of feedback messages into speech asynchronously.
    """
    if not feedback_messages:
        print("No feedback to speak.")
        return

    def speak():
        print(f"Speaking feedback: {feedback_messages}")  # Debugging message
        for message in feedback_messages:
            tts_engine.say(message)
        tts_engine.runAndWait()
    
    # Run the speak function in a separate thread
    speech_thread = threading.Thread(target=speak)
    speech_thread.daemon = True  # Daemon thread to exit with the main program
    speech_thread.start()

def check_posture(landmarks):
    feedback = []
    
    # Example: Check if shoulders are not level
    if landmarks[11].y > landmarks[12].y:
        feedback.append("Your left shoulder is lower than your right. Straighten up.")
    elif landmarks[11].y < landmarks[12].y:
        feedback.append("Your right shoulder is lower than your left. Straighten up.")

    # Example: Check if hips are not level
    if landmarks[23].y < landmarks[24].y:
        feedback.append("Your left hip is higher than your right. Adjust your stance.")
    elif landmarks[23].y > landmarks[24].y:
        feedback.append("Your right hip is higher than your left. Adjust your stance.")

    # New Condition: Check if back is not straight
    if abs(landmarks[11].x - landmarks[23].x) > 0.1:  # Example threshold
        feedback.append("Your back is not straight. Keep your torso aligned with your hips.")

    # New Condition: Check for slouching (head too far forward)
    if landmarks[0].x < landmarks[11].x - 0.2:  # Head compared to shoulder (x-axis threshold)
        feedback.append("You are slouching. Pull your head back to align with your shoulders.")

    # New Condition: Check if knees are bent unevenly
    if abs(landmarks[25].y - landmarks[26].y) > 0.1:  # Difference in knee heights
        feedback.append("Your knees are uneven. Stand with your legs balanced.")

    # New Condition: Check if feet are misaligned
    if abs(landmarks[27].x - landmarks[28].x) > 0.15:  # Feet too far apart horizontally
        feedback.append("Your feet are misaligned. Place them parallel to each other.")

    # Call text-to-speech for feedback
    if feedback:
        speak_feedback(feedback)
    else:
        print("No posture issues detected.")  # Debugging message

    return feedback

if __name__ == "__main__":
    try:
        while True:
            # Simulate landmarks data for testing
            landmarks = [
                # Example landmark positions (x, y) for head, shoulders, hips, knees, and feet
                {"x": 0.5, "y": 0.1},  # Head
                {"x": 0.5, "y": 0.5},  # Left shoulder
                {"x": 0.6, "y": 0.5},  # Right shoulder
                {"x": 0.5, "y": 0.8},  # Left hip
                {"x": 0.6, "y": 0.8},  # Right hip
                {"x": 0.5, "y": 1.0},  # Left knees
                {"x": 0.6, "y": 1.0},  # Right knee
                {"x": 0.5, "y": 1.2},  # Left foot
                {"x": 0.6, "y": 1.2},  # Right foot
            ]
            check_posture(landmarks)
    except KeyboardInterrupt:
        print("\nPose detection interrupted. Exiting gracefully.")
