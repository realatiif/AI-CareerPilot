import json
from openai import OpenAI


MODEL = "gpt-5.6-luna"


def create_client(api_key):
    if not api_key or not api_key.strip():
        raise ValueError("OpenAI API key is required.")
    return OpenAI(api_key=api_key.strip())


def _parse_json(content):
    if not content:
        raise ValueError("The AI returned an empty response.")

    text = content.strip()

    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    try:
        return json.loads(text.strip())
    except json.JSONDecodeError as exc:
        raise ValueError("The AI returned an invalid JSON response.") from exc


def analyze_resume(resume_text, api_key, target_career):
    client = create_client(api_key)

    prompt = f"""
Analyze this resume for a candidate targeting: {target_career}

Rules:
- Use only information supported by the resume.
- Never invent experience, education, certifications, skills, or projects.
- Skills should contain concrete technical/professional skills explicitly demonstrated or listed.
- Keep lists concise and useful.
- Return ONLY valid JSON.

Schema:
{{
  "summary": "short professional summary",
  "skills": ["skill"],
  "education": ["item"],
  "certifications": ["item"],
  "projects": ["item"],
  "experience": ["item"],
  "strengths": ["strength"],
  "improvements": ["improvement"]
}}

RESUME:
{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional career and resume analyst.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )

    return _parse_json(response.choices[0].message.content)


def generate_interview_question(api_key, target_career, interview_type, difficulty, question_number, resume_context):
    client = create_client(api_key)

    prompt = f"""
Create exactly ONE interview question.

Target career: {target_career}
Interview type: {interview_type}
Difficulty: {difficulty}
Question number: {question_number}

Candidate context:
{resume_context[:5000]}

Return ONLY valid JSON:
{{
  "question": "the interview question"
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert technical interviewer."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )

    return _parse_json(response.choices[0].message.content)


def evaluate_interview_answer(api_key, target_career, question, answer):
    client = create_client(api_key)

    prompt = f"""
Evaluate a candidate's interview answer.

Target career: {target_career}
Question: {question}
Candidate answer: {answer}

Return ONLY valid JSON:
{{
  "score": 0,
  "rating": "Excellent|Good|Needs Improvement|Weak",
  "strengths": ["specific strength"],
  "improvements": ["specific improvement"],
  "feedback": "short professional feedback"
}}

Score from 0 to 100.
Be fair and specific. Do not invent facts about the candidate.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a professional interview evaluator."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )

    return _parse_json(response.choices[0].message.content)


def generate_roadmap(api_key, target_career, skills, skill_gaps, improvements):
    client = create_client(api_key)

    prompt = f"""
Create a practical 6-step learning roadmap for a candidate targeting {target_career}.

Current skills:
{skills}

Skill gaps:
{skill_gaps}

Resume improvement areas:
{improvements}

Return ONLY valid JSON:
{{
  "roadmap": [
    {{
      "step": 1,
      "title": "title",
      "focus": "what to learn",
      "action": "what to build or practice"
    }}
  ]
}}

Exactly 6 steps. Make it realistic for a junior/student candidate.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an AI career planning expert."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )

    return _parse_json(response.choices[0].message.content)
