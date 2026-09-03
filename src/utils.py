def normalize_skill(skill):
    skill = str(skill).lower().strip()

    replacements = {
        "git and github": "git",
        "github": "git",
        "chatopenai": "openai api",
        "openai and chatopenai": "openai api",
        "llms": "large language models",
        "large language model": "large language models",
        "natural language processing": "nlp",
        "natural-language processing": "nlp",
        "object-oriented programming": "oop",
        "data structures and algorithms": "dsa",
    }

    return replacements.get(skill, skill)


def calculate_match_score(resume_skills, job_skills):
    resume = {normalize_skill(x) for x in resume_skills if str(x).strip()}
    required = {normalize_skill(x) for x in job_skills if str(x).strip()}

    if not required:
        return 0

    return round(len(resume.intersection(required)) / len(required) * 100, 1)


def get_skill_gaps(resume_skills, job_skills):
    resume = {normalize_skill(x) for x in resume_skills if str(x).strip()}
    return [skill for skill in job_skills if normalize_skill(skill) not in resume]


def calculate_career_score(analysis):
    skills = analysis.get("skills", [])
    projects = analysis.get("projects", [])
    education = analysis.get("education", [])
    certifications = analysis.get("certifications", [])
    strengths = analysis.get("strengths", [])

    score = 0
    score += min(len(skills) * 2, 30)
    score += min(len(projects) * 8, 25)
    score += 15 if education else 0
    score += 15 if certifications else 0
    score += min(len(strengths) * 2, 15)

    return min(score, 100)
