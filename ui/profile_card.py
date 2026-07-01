import streamlit as st


def profile_card(resume_json):

    st.subheader("👤 Candidate Profile")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Candidate",
            resume_json.get("name", "Unknown")
        )

        st.metric(
            "Email",
            resume_json.get("email", "N/A")
        )

        st.metric(
            "Phone",
            resume_json.get("phone", "N/A")
        )

    with c2:

        st.metric(
            "LinkedIn",
            resume_json.get("linkedin", "N/A")
        )

        st.metric(
            "GitHub",
            resume_json.get("github", "N/A")
        )

        skills = resume_json.get("skills", [])

        st.metric(
            "Skills",
            len(skills)
        )