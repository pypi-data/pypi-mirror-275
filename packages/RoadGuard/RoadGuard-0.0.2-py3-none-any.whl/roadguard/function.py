import os

from roadguard import feed
from roadguard.feed import speaker, camera
from roadguard.constant import RG_SAMPLE_DATA_PATH

DEFAULT_VIDEO_PATH = os.path.join(
    RG_SAMPLE_DATA_PATH,
    "didi", "city-5s.mp4"
)


def report():
    frames = feed.extract_frame(
        path=DEFAULT_VIDEO_PATH,
        seconds_per_frame=1
    )

    transcription = feed.summarize_video(frames)

    return transcription


def listen():
    def capture():
        print("Trigger detected! Capturing video...")
        frames = camera.capture()
        print(f"Captured {len(frames)} frames")

    speaker.trigger_and_run(
        func=capture,
        catch_phrase="catch"
    )
