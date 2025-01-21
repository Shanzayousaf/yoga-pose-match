import cv2
import mediapipe as mp

# Initialize MediaPipe Pose detection
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Counter to track how many times a pose has been detected
detection_counter = 0


def detect_pose_webcam():
    """
    Detect pose from the webcam feed, track detection counts, and allow user to quit with 'q'.
    """
    global detection_counter

    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 'q' to exit the webcam view.")

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame from webcam.")
                break

            # Convert the frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame for pose detection
            result = pose.process(rgb_frame)

            # If landmarks are detected, draw them and increment the counter
            if result.pose_landmarks:
                detection_counter += 1
                mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                print(f"Pose Detected! Count: {detection_counter}")

            # Display the frame
            cv2.imshow("Pose Detection - Webcam", frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Stopping webcam detection loop...")
                break
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected. Exiting the webcam detection loop.")
    finally:
        # Release the webcam and destroy windows
        cap.release()
        cv2.destroyAllWindows()
        print(f"Total poses detected: {detection_counter}")


if __name__ == "__main__":
    detect_pose_webcam()
    pose.close()
    print("Program terminated gracefully.")
