from dataclasses import dataclass

@dataclass
class MatchResult:
    score: float
    matched: set[str]
    missing: set[str]

def match_skills(resume_skills: set[str], job_skills: set[str]) -> MatchResult:
    if not job_skills:
        return MatchResult(score=0.0, matched=set(), missing=set())

    matched = resume_skills.intersection(job_skills)
    missing = job_skills.difference(resume_skills)
    score = (len(matched) / len(job_skills)) * 100

    return MatchResult(score=score, matched=matched, missing=missing)
