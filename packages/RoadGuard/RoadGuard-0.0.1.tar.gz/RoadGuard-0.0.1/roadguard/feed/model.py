import os
from openai import OpenAI

from roadguard import feed
from roadguard.feed import parameter, prompt


def transcribe_video(frames: list,
                     prompt=prompt.transcribe_video) -> str:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model=parameter.MODEL,
        messages=[
            {"role": "system",
             "content": prompt},
            {"role": "user", "content": [
                "These are the frames from the video.",
                *map(lambda x: {"type": "image_url",
                                "image_url": {"url": f'data:image/jpg;base64,{x}',
                                              "detail": "low"}}, frames),
            ],
             }
        ],
        temperature=parameter.TEMPERATURE,
    )

    input_tokens = response.usage.total_tokens - response.usage.completion_tokens
    output_tokens = response.usage.completion_tokens

    feed.trace.add({
        "model": {
            "num_input_tokens": input_tokens,
            "num_output_tokens": output_tokens,
        }
    })

    return response.choices[0].message.content


def summarize_video(frames: list) -> str:
    return transcribe_video(
        frames, prompt=prompt.summarize_video
    )


def transcribe_audio(path: str) -> str:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response = client.audio.transcriptions.create(
        model="whisper-1",
        file=open(path, "rb"),
    )
    return response.choices[0].message.content
