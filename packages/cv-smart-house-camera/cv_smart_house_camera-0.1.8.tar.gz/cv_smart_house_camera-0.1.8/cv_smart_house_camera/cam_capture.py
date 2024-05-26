import cv2
import time
from cv_smart_house_camera.modules.modules_processing import modules_processing

def cam_capture(video_file_path = "G:\\diploma\\camera-service\\test.mp4", fps=24):
    cap = cv2.VideoCapture(video_file_path)  # Path to the video file
    frame_number = 0
    frame_interval = 1.0 / fps  # Interval between frames in seconds

    while True:
        start_time = time.time()
        try:
            ret, frame = cap.read()
            if not ret:
                break
            frame_number += 1

            modules_processing(frame, frame_number)
            # cv2.imshow('Video', frame)

            # if cv2.waitKey(1) & 0xFF == ord('q'):
                # break

        except Exception as e:
            print(f"Error processing frame {frame_number}: {e}")

        # Sleep to maintain the frame rate
        elapsed_time = time.time() - start_time
        time_to_sleep = max(0, frame_interval - elapsed_time)
        time.sleep(time_to_sleep)
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file_path = 'path/to/your/video/file.mp4'  # Replace with your video file path
    cam_capture(video_file_path)
