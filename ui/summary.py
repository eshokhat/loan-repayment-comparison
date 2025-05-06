# Key Metrics

import streamlit as st
import pandas as pd

def show_loan_summary(schedule: pd.DataFrame):
    total_payment = schedule["Payment"].sum()
    total_interest = schedule["Interest"].sum()
    first_payment = schedule.iloc[0]["Payment"]
    last_payment = schedule.iloc[-1]["Payment"]

    st.subheader("Loan Summary")


    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Paid (₪)", f"{total_payment:,.2f}")
        st.metric("Total Interest (₪)", f"{total_interest:,.2f}")

    with col2:
        st.metric("First Payment (₪)", f"{first_payment:,.2f}")
        st.metric("Last Payment (₪)", f"{last_payment:,.2f}")


def show_method_comparison(annuity_df: pd.DataFrame, linear_df: pd.DataFrame):
    st.subheader(" Method Comparison")

    col1, col2 = st.columns(2)

    # Annuity metrics
    with col1:
        st.markdown("**Annuity (שפיצר)**")
        st.metric("Total Paid", f"{annuity_df['Payment'].sum():,.2f} ₪")
        st.metric("Interest", f"{annuity_df['Interest'].sum():,.2f} ₪")
        st.metric("First Payment", f"{annuity_df.iloc[0]['Payment']:,.2f} ₪")
        st.metric("Last Payment", f"{annuity_df.iloc[-1]['Payment']:,.2f} ₪")

    # Linear metrics
    with col2:
        st.markdown("**Linear (קרן שווה)**")
        st.metric("Total Paid", f"{linear_df['Payment'].sum():,.2f} ₪")
        st.metric("Interest", f"{linear_df['Interest'].sum():,.2f} ₪")
        st.metric("First Payment", f"{linear_df.iloc[0]['Payment']:,.2f} ₪")
        st.metric("Last Payment", f"{linear_df.iloc[-1]['Payment']:,.2f} ₪")