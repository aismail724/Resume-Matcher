import sys
from pathlib import Path

from parser import load_json, normalize, extract_skills
from matcher import match_skills
from report import print_report


def read_text_file(path: str) -> str:
    
    return Path(path).read_text(encoding="utf-8")


def main() -> None:

    # 1) Validate command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <resume.txt> <job.txt>")
        print("Example: python main.py ../samples/resume_sample.txt ../samples/job_sample.txt")
        sys.exit(1)

    resume_path = sys.argv[1]
    job_path = sys.argv[2]

    # 2) Load skills + synonyms data files
    skills = load_json("../data/skills.json")
    synonyms = load_json("../data/synonyms.json")

    # 3) Read and normalize raw text
    resume_text = normalize(read_text_file(resume_path), synonyms)
    job_text = normalize(read_text_file(job_path), synonyms)

    # 4) Extract skills from each
    resume_skills = extract_skills(resume_text, skills)
    job_skills = extract_skills(job_text, skills)

    # 5) Match + score
    result = match_skills(resume_skills, job_skills)

    # 6) Print report
    print_report(result)


if __name__ == "__main__":
    main()
