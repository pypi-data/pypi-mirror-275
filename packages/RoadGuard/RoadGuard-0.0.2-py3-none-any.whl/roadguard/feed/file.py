import os
import time
import cv2
import base64

from roadguard import feed

def extract_frame(path: str, seconds_per_frame=1):
    start = time.time()
    base64Frames = []
    base_video_path, _ = os.path.splitext(path)

    video = cv2.VideoCapture(path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * seconds_per_frame)
    curr_frame = 0

    # Loop through the video and extract frames at specified sampling rate
    while curr_frame < total_frames - 1:
        video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
        curr_frame += frames_to_skip
    video.release()

    print(f"Extracted {len(base64Frames)} frames")

    feed.trace.add({
        "extract": {
            "num_frames": len(base64Frames),
            "latency": time.time() - start,
        }
    })
    return base64Frames
