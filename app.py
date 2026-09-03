import json
import streamlit as st
import plotly.graph_objects as go

from src.ai_engine import (
    analyze_resume,
    generate_interview_question,
    evaluate_interview_answer,
    generate_roadmap,
)
from src.resume_parser import extract_resume_text
from src.styles import load_css
from src.utils import (
    calculate_career_score,
    calculate_match_score,
    get_skill_gaps,
)


st.set_page_config(
    page_title="AI CareerPilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()


def load_jobs():
    with open("data/sample_jobs.json", "r", encoding="utf-8") as file:
        return json.load(file)


def reset_session():
    for key in [
        "api_key",
        "analysis",
        "resume_text",
        "interview",
        "roadmap",
    ]:
        st.session_state.pop(key, None)


def api_key_page():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🚀 AI CareerPilot</div>
            <div class="hero-subtitle">
                Your AI-powered career assistant for resume analysis,
                job matching, skill-gap discovery, personalized learning
                and interview preparation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 🔐 Connect OpenAI")

    st.write("Enter your OpenAI API key to unlock the AI features.")

    st.info(
        "🔒 Your key is kept only in this Streamlit session. "
        "It is not written to a project file."
    )

    key = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-...",
    )

    if st.button(
        "🚀 Enter CareerPilot",
        type="primary",
        use_container_width=True,
    ):
        if not key.strip():
            st.error("Please enter your OpenAI API key.")
            return

        st.session_state["api_key"] = key.strip()
        st.rerun()

    st.markdown(
        '<div class="footer">AI CareerPilot • Secure session-only API key</div>',
        unsafe_allow_html=True,
    )


def gauge_chart(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Career Readiness"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"thickness": 0.3},
                "steps": [
                    {"range": [0, 40]},
                    {"range": [40, 70]},
                    {"range": [70, 100]},
                ],
            },
        )
    )
    fig.update_layout(height=310, margin=dict(l=20, r=20, t=60, b=20))
    return fig


def job_chart(results):
    fig = go.Figure(
        go.Bar(
            x=[x["score"] for x in results],
            y=[x["title"] for x in results],
            orientation="h",
            text=[f'{x["score"]}%' for x in results],
            textposition="auto",
        )
    )
    fig.update_layout(
        title="Job Compatibility",
        xaxis_title="Match %",
        xaxis=dict(range=[0, 100]),
        height=390,
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig


def feature_cards():
    cols = st.columns(3)
    items = [
        ("📄", "Resume Analyzer", "Extract skills, education, projects and certifications."),
        ("💼", "Job Matcher", "Compare your skills with realistic sample job roles."),
        ("🎤", "AI Interviewer", "Generate questions and receive AI-powered scoring."),
    ]

    for col, (icon, title, text) in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def dashboard():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🚀 AI CareerPilot</div>
            <div class="hero-subtitle">
                Turn your resume into a practical career strategy:
                analyze, match, improve, learn and practice.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    top1, top2 = st.columns([4, 1])
    with top2:
        if st.button("🔒 Exit", use_container_width=True):
            reset_session()
            st.rerun()

    st.markdown("## 🎯 Target Career")
    target = st.selectbox(
        "Choose your target role",
        [
            "AI/ML Engineer",
            "Generative AI Developer",
            "Python Developer",
            "Data Analyst",
            "Software Engineer",
        ],
    )
    st.session_state["target_career"] = target

    st.markdown("## 📄 Resume")
    uploaded = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"],
        help="PDF and DOCX are supported.",
    )

    if uploaded is None and "analysis" not in st.session_state:
        feature_cards()
        return

    if uploaded is not None:
        if st.button(
            "🔍 Analyze Resume",
            type="primary",
            use_container_width=True,
        ):
            try:
                with st.spinner("📄 Reading your resume..."):
                    text = extract_resume_text(uploaded)

                if not text:
                    st.error("No readable text was found in the resume.")
                    return

                with st.spinner("🧠 AI is analyzing your career profile..."):
                    analysis = analyze_resume(
                        text,
                        st.session_state["api_key"],
                        target,
                    )

                st.session_state["resume_text"] = text
                st.session_state["analysis"] = analysis
                st.session_state.pop("interview", None)
                st.session_state.pop("roadmap", None)

                st.success("✅ Resume analysis completed.")
            except Exception as error:
                st.error(f"❌ Analysis failed: {error}")
                return

    if "analysis" not in st.session_state:
        return

    analysis = st.session_state["analysis"]

    st.divider()
    st.header("📊 Career Dashboard")

    score = calculate_career_score(analysis)

    left, right = st.columns(2)
    with left:
        st.plotly_chart(gauge_chart(score), use_container_width=True)

    with right:
        st.markdown(
            f"""
            <div class="card">
                <h2>🎯 {target}</h2>
                <p>Your analysis is focused on this career direction.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.metric("Career Readiness", f"{score}%")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🛠️ Skills", len(analysis.get("skills", [])))
    c2.metric("🚀 Projects", len(analysis.get("projects", [])))
    c3.metric("📜 Certifications", len(analysis.get("certifications", [])))
    c4.metric("🎓 Education", len(analysis.get("education", [])))

    st.divider()
    st.header("👤 Professional Profile")

    st.subheader("Professional Summary")
    st.write(analysis.get("summary", "No summary available."))

    p1, p2 = st.columns(2)

    with p1:
        st.subheader("💪 Strengths")
        for item in analysis.get("strengths", []) or ["No strengths detected."]:
            st.write(f"• {item}")

    with p2:
        st.subheader("🎯 Areas to Improve")
        for item in analysis.get("improvements", []) or ["No improvements detected."]:
            st.write(f"• {item}")

    sections = [
        ("🎓 Education", "education"),
        ("📜 Certifications", "certifications"),
        ("🚀 Projects", "projects"),
        ("💼 Experience", "experience"),
    ]

    for title, key in sections:
        st.subheader(title)
        values = analysis.get(key, [])
        if values:
            for value in values:
                st.write(f"• {value}")
        else:
            st.write("No information detected.")

    st.divider()
    st.header("🛠️ Skill Analysis")

    skills = analysis.get("skills", [])
    if skills:
        st.write("**Detected skills:**")
        skill_cols = st.columns(3)
        for i, skill in enumerate(skills):
            with skill_cols[i % 3]:
                st.success(f"✓ {skill}")
    else:
        st.info("No technical skills detected.")

    st.divider()
    st.header("💼 Job Matching")

    jobs = load_jobs()
    results = []

    for job in jobs:
        score_value = calculate_match_score(skills, job["skills"])
        results.append(
            {
                "title": job["title"],
                "company": job["company"],
                "score": score_value,
                "missing": get_skill_gaps(skills, job["skills"]),
                "description": job["description"],
            }
        )

    results.sort(key=lambda x: x["score"], reverse=True)
    st.plotly_chart(job_chart(results), use_container_width=True)

    best = results[0]
    st.markdown(
        f"""
        <div class="card">
            <h3>🏆 Best Current Match</h3>
            <h2>{best["title"]}</h2>
            <p>{best["company"]}</p>
            <h3>{best["score"]}% Match</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for job in results:
        with st.container(border=True):
            st.subheader(f'{job["title"]} — {job["company"]}')
            st.progress(min(int(job["score"]), 100))
            st.write(f'**Match Score: {job["score"]}%**')
            st.write(job["description"])

            if job["missing"]:
                st.write("**🎯 Skills to develop:**")
                st.write(", ".join(job["missing"]))
            else:
                st.success("Excellent! No major skill gaps detected.")

    all_gaps = []
    for job in results:
        for skill in job["missing"]:
            if skill not in all_gaps:
                all_gaps.append(skill)

    st.divider()
    st.header("🧩 Overall Skill Gaps")

    if all_gaps:
        gap_cols = st.columns(3)
        for i, skill in enumerate(all_gaps):
            with gap_cols[i % 3]:
                st.warning(f"⚠️ {skill}")
    else:
        st.success("🎉 No major skill gaps found.")

    st.divider()
    st.header("📚 Personalized Learning Roadmap")

    if st.button(
        "🧠 Generate My AI Roadmap",
        type="primary",
        use_container_width=True,
    ):
        try:
            with st.spinner("🧠 Creating your personalized roadmap..."):
                roadmap = generate_roadmap(
                    st.session_state["api_key"],
                    target,
                    skills,
                    all_gaps,
                    analysis.get("improvements", []),
                )
            st.session_state["roadmap"] = roadmap
        except Exception as error:
            st.error(f"❌ Roadmap generation failed: {error}")

    if "roadmap" in st.session_state:
        for step in st.session_state["roadmap"].get("roadmap", []):
            with st.container(border=True):
                st.markdown(f'### Step {step.get("step", "")} — {step.get("title", "")}')
                st.write(f'**Focus:** {step.get("focus", "")}')
                st.write(f'**Action:** {step.get("action", "")}')

    st.divider()
    interview_page(target, analysis)


def interview_page(target, analysis):
    st.header("🎤 AI Interview Simulator")
    st.write(
        "Generate a real interview question, answer it, and receive "
        "AI-powered scoring and feedback."
    )

    i1, i2 = st.columns(2)
    with i1:
        interview_type = st.selectbox(
            "Interview Type",
            ["Technical", "Behavioral", "Mixed"],
            key="interview_type",
        )
    with i2:
        difficulty = st.selectbox(
            "Difficulty",
            ["Beginner", "Intermediate", "Advanced"],
            key="interview_difficulty",
        )

    if st.button(
        "🎤 Generate Interview Question",
        type="primary",
        use_container_width=True,
    ):
        try:
            with st.spinner("🧠 Preparing your interview question..."):
                result = generate_interview_question(
                    st.session_state["api_key"],
                    target,
                    interview_type,
                    difficulty,
                    1,
                    st.session_state.get("resume_text", ""),
                )

            st.session_state["interview"] = {
                "question": result.get("question", ""),
                "answer": "",
                "feedback": None,
            }
        except Exception as error:
            st.error(f"❌ Question generation failed: {error}")

    interview = st.session_state.get("interview")

    if not interview:
        st.info("Click the button above when you are ready to start.")
        return

    st.markdown(
        f"""
        <div class="card">
            <h3>Question</h3>
            <p>{interview["question"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    answer = st.text_area(
        "Your Answer",
        value=interview.get("answer", ""),
        placeholder="Write your interview answer here...",
        height=190,
        key="interview_answer",
    )

    if st.button(
        "📊 Evaluate My Answer",
        use_container_width=True,
    ):
        if not answer.strip():
            st.warning("Please write your answer first.")
        else:
            try:
                with st.spinner("🧠 Evaluating your answer..."):
                    feedback = evaluate_interview_answer(
                        st.session_state["api_key"],
                        target,
                        interview["question"],
                        answer,
                    )

                interview["answer"] = answer
                interview["feedback"] = feedback
                st.session_state["interview"] = interview
            except Exception as error:
                st.error(f"❌ Evaluation failed: {error}")

    feedback = interview.get("feedback")

    if feedback:
        st.divider()
        st.subheader("📊 AI Evaluation")

        score = int(feedback.get("score", 0))
        rating = feedback.get("rating", "Needs Improvement")

        a1, a2 = st.columns(2)
        with a1:
            st.metric("Interview Score", f"{score}/100")
        with a2:
            st.metric("Rating", rating)

        st.info(feedback.get("feedback", ""))

        f1, f2 = st.columns(2)
        with f1:
            st.subheader("✅ Strengths")
            for item in feedback.get("strengths", []):
                st.write(f"• {item}")

        with f2:
            st.subheader("🎯 Improvements")
            for item in feedback.get("improvements", []):
                st.write(f"• {item}")

        if st.button("🔄 New Interview Question"):
            st.session_state.pop("interview", None)
            st.rerun()


def main():
    if "api_key" not in st.session_state:
        api_key_page()
    else:
        dashboard()


if __name__ == "__main__":
    main()
