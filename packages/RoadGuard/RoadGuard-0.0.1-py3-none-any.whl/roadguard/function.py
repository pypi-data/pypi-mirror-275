import os
import time

from roadguard.feed import file, model
from roadguard.constant import RG_SAMPLE_DATA_PATH

DEFAULT_VIDEO_PATH = os.path.join(
    RG_SAMPLE_DATA_PATH,
    "didi", "city-5s.mp4"
)


def report():
    frames = file.extract_frame(
        path=DEFAULT_VIDEO_PATH,
        seconds_per_frame=1
    )

    start = time.time()
    transcription = model.summarize_video(frames)

    print(f"Number of frames {len(frames)}")
    print(f"Transcription:\n{transcription}")
    print(f"Time taken: {time.time() - start}")
