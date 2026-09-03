import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 0%, rgba(99,102,241,.16), transparent 32%),
                radial-gradient(circle at 90% 5%, rgba(168,85,247,.14), transparent 30%),
                #0b1120;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        .hero {
            padding: 34px;
            border-radius: 26px;
            background: linear-gradient(135deg, rgba(79,70,229,.28), rgba(147,51,234,.18));
            border: 1px solid rgba(255,255,255,.10);
            box-shadow: 0 20px 55px rgba(0,0,0,.28);
            margin-bottom: 28px;
        }

        .hero-title {
            font-size: 48px;
            font-weight: 800;
            letter-spacing: -1.5px;
        }

        .hero-subtitle {
            color: #cbd5e1;
            font-size: 18px;
            line-height: 1.65;
            max-width: 900px;
        }

        .card {
            padding: 22px;
            border-radius: 18px;
            background: rgba(30,41,59,.72);
            border: 1px solid rgba(255,255,255,.08);
            box-shadow: 0 12px 30px rgba(0,0,0,.18);
            margin-bottom: 18px;
        }

        .feature-card {
            padding: 22px;
            border-radius: 18px;
            background: rgba(30,41,59,.68);
            border: 1px solid rgba(255,255,255,.08);
            min-height: 155px;
        }

        .feature-icon {
            font-size: 30px;
        }

        .feature-title {
            font-size: 18px;
            font-weight: 700;
            margin-top: 8px;
        }

        .feature-text {
            color: #cbd5e1;
            font-size: 14px;
            line-height: 1.55;
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            padding-top: 28px;
            font-size: 13px;
        }

        .stButton > button {
            border-radius: 12px;
            font-weight: 700;
            min-height: 44px;
        }

        [data-testid="stFileUploader"] {
            background: rgba(30,41,59,.55);
            border-radius: 16px;
            padding: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
