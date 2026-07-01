import plotly.graph_objects as go
import streamlit as st


def gauge_chart(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=score,

            number={
                "suffix": "%"
            },

            title={
                "text": "ATS Score"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#00CC96"
                },

                "steps": [

                    {
                        "range": [0, 50],
                        "color": "#ffdddd"
                    },

                    {
                        "range": [50, 75],
                        "color": "#fff4cc"
                    },

                    {
                        "range": [75, 100],
                        "color": "#ddffdd"
                    }

                ]
            }
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )