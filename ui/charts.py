# Visualization

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def plot_payment_breakdown(schedule: pd.DataFrame):
    st.subheader("Payment Breakdown")

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=schedule["Month"],
        y=schedule["Principal"],
        name="Principal",
        marker_color="#2C3E50"
    ))

    fig.add_trace(go.Bar(
        x=schedule["Month"],
        y=schedule["Interest"],
        name="Interest",
        marker_color="#AF906E" 
    ))

    fig.update_layout(
        barmode='stack',
        xaxis_title="Month",
        yaxis_title="Monthly Payment (₪)",
        legend_title="Component",
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_remaining_balance(schedule: pd.DataFrame):
    st.subheader("Remaining Balance Over Time")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=schedule["Month"],
        y=schedule["Remaining Balance"],
        mode="lines",
        name="Remaining Balance",
        line=dict(color="#2C3E50", width=2)
    ))

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Remaining Balance (₪)",
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_compare_remaining(annuity_df, linear_df):
    st.subheader("Remaining Balance: Annuity vs Linear")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=annuity_df["Month"],
        y=annuity_df["Remaining Balance"],
        mode="lines",
        name="Annuity",
        line=dict(color="#4CAF50")
    ))

    fig.add_trace(go.Scatter(
        x=linear_df["Month"],
        y=linear_df["Remaining Balance"],
        mode="lines",
        name="Linear",
        line=dict(color="#FF9800", dash="dash")
    ))

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Remaining Balance (₪)",
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_uploaded_schedule(schedule: pd.DataFrame):
    st.subheader("Remaining Balance from Uploaded Table")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=schedule["Month"],
        y=schedule["Remaining Balance"],
        mode="lines+markers",
        name="Remaining Balance",
        line=dict(color="#9c27b0", width=2)
    ))

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Remaining Balance (₪)",
        template="simple_white",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)