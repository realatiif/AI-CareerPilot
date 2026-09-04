# 🚀 AI CareerPilot

> **AI-powered Personal Career & Job Assistant**

AI CareerPilot is a modern AI-powered career assistant that helps students, fresh graduates, and junior developers understand their professional profile, discover suitable career opportunities, identify skill gaps, build a personalized learning roadmap, and practice job interviews.

The application uses **Python, Streamlit, OpenAI API, resume parsing, structured AI outputs, and data visualization** to provide an interactive career-planning experience.

---

## ✨ Features

### 📄 AI Resume Analyzer

Upload your resume in **PDF or DOCX** format and let AI analyze:

* Professional summary
* Technical skills
* Education
* Certifications
* Projects
* Experience
* Strengths
* Areas for improvement

### 📊 Career Readiness Dashboard

Get a visual overview of your career profile with:

* Career readiness score
* Skills count
* Projects count
* Certifications count
* Education information
* Professional profile analysis

### 💼 AI Job Matching

AI CareerPilot compares your resume skills with available job roles and calculates:

* Job compatibility percentage
* Best matching career opportunity
* Required skills
* Missing skills
* Overall job compatibility

### 🧩 Skill Gap Analysis

Identify the technical skills you need to develop for your target career.

The system highlights missing skills across different job roles so you can prioritize your learning.

### 📚 Personalized Learning Roadmap

Generate an AI-powered six-step roadmap based on:

* Current skills
* Target career
* Skill gaps
* Resume improvement areas

### 🎤 AI Interview Simulator

Practice realistic interviews with AI.

Choose:

* Technical
* Behavioral
* Mixed

And select:

* Beginner
* Intermediate
* Advanced

The AI can generate interview questions and evaluate your answers with:

* Score out of 100
* Rating
* Strengths
* Improvements
* Detailed feedback

### 🎨 Modern Interface

AI CareerPilot includes a professional dark-themed dashboard designed for an attractive portfolio/project presentation.

---

## 🧠 Technologies Used

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| Python       | Core programming language            |
| Streamlit    | Web application interface            |
| OpenAI API   | AI-powered analysis and evaluation   |
| PyPDF        | PDF resume text extraction           |
| python-docx  | DOCX resume extraction               |
| Plotly       | Interactive data visualization       |
| JSON         | Job data and structured AI responses |
| Git & GitHub | Version control and project hosting  |

---

## 🏗️ Project Architecture

```text
AI-CareerPilot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── ai_engine.py
│   ├── resume_parser.py
│   ├── styles.py
│   └── utils.py
│
└── data/
    └── sample_jobs.json
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/realatiif/AI-CareerPilot.git
```

### 2. Open the project

```bash
cd AI-CareerPilot
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 6. Run the application

```powershell
python -m streamlit run app.py
```

The application will open in your browser.

---

## 🔐 OpenAI API Key

When the application starts, AI CareerPilot displays an API key entry screen.

Enter your OpenAI API key to access the AI features.

The application keeps the key in the current Streamlit session and does not require storing it inside the project source code.

> ⚠️ Never commit an API key to GitHub.

---

## 🚀 Application Workflow

```text
             ┌─────────────────────┐
             │   Open AI CareerPilot│
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Enter API Key     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Select Target Career│
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Upload Resume     │
             │     PDF / DOCX      │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   AI Resume Analysis│
             └──────────┬──────────┘
                        │
             ┌──────────┼───────────┐
             ▼          ▼           ▼
       ┌──────────┐ ┌─────────┐ ┌───────────┐
       │ Job Match│ │ Skill   │ │ Career    │
       │          │ │ Gaps    │ │ Score     │
       └────┬─────┘ └────┬────┘ └─────┬─────┘
            │            │             │
            └────────────┼─────────────┘
                         ▼
              ┌────────────────────┐
              │ AI Learning Roadmap│
              └──────────┬─────────┘
                         │
                         ▼
              ┌────────────────────┐
              │ AI Interview       │
              │ Simulator          │
              └────────────────────┘
```

---

## 🎯 Target Users

AI CareerPilot is designed for:

* 🎓 Computer Science students
* 👨‍💻 Junior developers
* 🤖 AI/ML beginners
* 🧠 Generative AI learners
* 💼 Fresh graduates
* 📄 Job seekers
* 🎤 Interview preparation

---

## 💡 Example Career Paths

The application currently supports career targeting such as:

* AI/ML Engineer
* Generative AI Developer
* Python Developer
* Data Analyst
* Software Engineer

---

## 📈 Future Improvements

Possible future versions can include:

* 🔎 Real-time job searching
* 🌐 LinkedIn job integration
* 📚 RAG-based career knowledge base
* 🤖 Autonomous AI career agent
* 🧠 Advanced interview sessions
* 📊 Resume ATS scoring
* 📝 AI resume improvement
* 💾 User profiles and database
* 📧 Job application tracking
* ☁️ Cloud deployment
* 📱 Mobile-friendly interface

---

## 🔒 Security

AI CareerPilot follows basic security practices:

* API keys are not hard-coded.
* API keys are not stored in `.env`.
* `.env` is included in `.gitignore`.
* Virtual environments are excluded from Git.
* Sensitive files should never be committed to the repository.

---

## ⚠️ Disclaimer

AI CareerPilot provides AI-generated career guidance for educational and informational purposes.

Career scores, job matches, recommendations, and interview feedback should be treated as supporting information and **not as professional hiring decisions**.

---

## 👨‍💻 Developer

**Rana Atif**

Computer Science Student | AI/ML & Generative AI Developer

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Generative AI
* Large Language Models
* AI Agents
* Python
* Computer Science
* AI Application Development

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 🚀 AI CareerPilot

**Analyze → Match → Improve → Learn → Practice → Grow**
