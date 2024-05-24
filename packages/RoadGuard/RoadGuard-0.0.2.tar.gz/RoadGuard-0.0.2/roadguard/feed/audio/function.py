import os
import time
from openai import OpenAI

from roadguard import feed
from roadguard.feed.audio import parameter, prompt


def transcribe(path: str,
               model=parameter.model) -> str:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response = client.audio.transcriptions.create(
        model=model,
        file=open(path, "rb"),
    )
    return response.choices[0].message.content
