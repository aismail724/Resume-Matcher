import json
import re
from pathlib import Path

def load_json(path: str):

    return json.loads(Path(path).read_text(encoding="utf-8"))

def normalize(text: str, synonyms: dict) -> str:

    text = text.lower()

    # replace most punctuation with spaces (keeps letters/numbers)
    text = re.sub(r"[^a-z0-9\s\.\-/]", " ", text)

    # collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text).strip()

    # apply synonyms
    for k, v in synonyms.items():
        text = text.replace(k, v)

    return text

def extract_skills(text: str, skills_list: list[str]) -> set[str]:
   
    found = set()
    for skill in skills_list:
        if skill in text:
            found.add(skill)
    return found

