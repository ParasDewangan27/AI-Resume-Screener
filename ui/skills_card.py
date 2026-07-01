import streamlit as st


def skills_card(matched, missing):

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("✅ Matched Skills")

        for skill in matched:

            st.success(skill.title())

    with c2:

        st.subheader("❌ Missing Skills")

        for skill in missing:

            st.error(skill.title())