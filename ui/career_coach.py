"""
career_coach.py

Displays the AI Career Coach section.
"""

import streamlit as st


def career_coach_card(coach_data):

    st.header("🤖 AI Career Coach")

    tab1, tab2, tab3, tab4 = st.tabs([
        "💡 Suggestions",
        "🎓 Certifications",
        "❓ Interview Questions",
        "📈 Career Roadmap"
    ])

    # ------------------------------------
    # Suggestions
    # ------------------------------------

    with tab1:

        suggestions = coach_data.get(
            "resume_suggestions",
            []
        )

        if suggestions:

            for item in suggestions:
                st.success(item)

        else:

            st.info("No suggestions available.")

    # ------------------------------------
    # Certifications
    # ------------------------------------

    with tab2:

        certs = coach_data.get(
            "recommended_certifications",
            []
        )

        if certs:

            for cert in certs:
                st.info(cert)

        else:

            st.info("No certifications suggested.")

    # ------------------------------------
    # Interview Questions
    # ------------------------------------

    with tab3:

        questions = coach_data.get(
            "interview_questions",
            []
        )

        if questions:

            for i, question in enumerate(
                questions,
                start=1
            ):

                st.write(
                    f"**{i}.** {question}"
                )

        else:

            st.info("No interview questions generated.")

    # ------------------------------------
    # Career Roadmap
    # ------------------------------------

    with tab4:

        roadmap = coach_data.get(
            "career_roadmap",
            []
        )

        if roadmap:

            for step in roadmap:

                st.markdown(
                    f"➡️ {step}"
                )

        else:

            st.info("No roadmap generated.")