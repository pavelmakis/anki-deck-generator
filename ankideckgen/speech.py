from pathlib import Path
from typing import Union

from speechkit import model_repository


def text_to_speech(text: str, speed: float, filename: Union[Path, str]) -> None:
   model = model_repository.synthesis_model()

   # Setting speech voice
   model.voice = "lea"
   model.sample_rate = speed

   # Синтез речи и создание аудио с результатом.
   result = model.synthesize(text, raw_format=False)
   result.export(filename, "mp3")
