# Resume–Job Skill Matcher (Python)

A simple Python tool that compares a resume against a job posting and outputs:
- a match score (%)
- matched skills
- missing skills

## Features
- Loads a curated skill list (`skills.json`)
- Normalizes text and applies synonyms (`synonyms.json`)
- Extracts skills from resume/job text
- Computes match score using set comparison
- Exports the report to `report.md`

## Project Structure
resume-matcher/

src/

main.py

parser.py

matcher.py

report.py

data/

skills.json

synonyms.json

samples/

resume_sample.txt

job_sample.txt

## Output example

Resume–Job Match Summary
--------------------------------------------------
Overall Match Score: 28.6%

Matched Skills (2):
✔ python
✔ git

Missing Skills (5):
✖ api
✖ aws
✖ docker
✖ rest api
✖ sql
--------------------------------------------------

