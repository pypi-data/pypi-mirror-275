import os
import time
from openai import OpenAI

from roadguard import feed
from roadguard.feed.core.struct import Prompt
from roadguard.feed.video import parameter, prompt


def openai(frames: list,
           prompt=prompt.role,
           model=parameter.model) -> str:
    start = time.time()
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",
             "content": prompt},
            {"role": "user", "content": [
                "These are the frames from the video.",
                *map(lambda x:
                     {"type": "image_url",
                      "image_url":
                          {"url": f'data:image/jpg;base64,{x}',
                           "detail": "low"}
                      }, frames),
            ],
             }
        ],
        temperature=parameter.temperature,
    )

    feed.trace.add({
        "model": {
            "num_input_tokens": response.usage.total_tokens - response.usage.completion_tokens,
            "num_output_tokens": response.usage.completion_tokens,
            "latency": time.time() - start,
        }
    })

    return response.choices[0].message.content


def transcribe(frames: list) -> str:
    return openai(
        frames, prompt=Prompt.join(
            prompt.role,
            prompt.transcribe,
            prompt.output,
        )
    )


def summarize(frames: list) -> str:
    return openai(
        frames, prompt=Prompt.join(
            prompt.role,
            prompt.summarize,
            prompt.detect_violation,
            prompt.output,
        )
    )
