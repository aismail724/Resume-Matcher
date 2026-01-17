from flask import Flask, render_template, request
import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"
sys.path.append(str(SRC_DIR))

from parser import load_json, normalize, extract_skills  # noqa: E402
from matcher import match_skills  # noqa: E402

app = Flask(__name__)


SKILLS = load_json(str(PROJECT_ROOT / "data" / "skills.json"))
SYNONYMS = load_json(str(PROJECT_ROOT / "data" / "synonyms.json"))


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/analyze")
def analyze():
    resume_text_raw = request.form.get("resume_text", "")
    job_text_raw = request.form.get("job_text", "")

   
    if not resume_text_raw.strip() or not job_text_raw.strip():
        return render_template(
            "index.html",
            error="Please paste both a resume and a job posting."
        )


    resume_text = normalize(resume_text_raw, SYNONYMS)
    job_text = normalize(job_text_raw, SYNONYMS)

    resume_skills = extract_skills(resume_text, SKILLS)
    job_skills = extract_skills(job_text, SKILLS)

    result = match_skills(resume_skills, job_skills)

    return render_template(
        "result.html",
        score=round(result.score, 1),
        matched=sorted(result.matched),
        missing=sorted(result.missing),
        resume_count=len(resume_skills),
        job_count=len(job_skills),
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
