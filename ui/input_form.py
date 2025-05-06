# Input form

import streamlit as st

def loan_input_form():
    st.sidebar.header("Loan Parameters")

    loan_amount = st.sidebar.number_input(
        "Loan Amount (₪)", min_value = 5000.0, max_value = 200000.0, step=0.1, value=10000.0
    )
    
    annual_rate = st.sidebar.number_input(
        "Annual Interest Rate (%)", min_value=0.1, max_value=30.0, step=0.1, value=14.5
    )
    months = st.sidebar.slider("Loan Term (months)", 1, 36, 12)

    repayment_method = st.sidebar.radio(
        "Repayment Type",
        options=["Annuity", "Linear"],
        index=0,
        help="Annuity = fixed payments (שפיצר), Linear = equal principal payments (קרן שווה)"
    )

    grace_months = []
    grace_active = st.sidebar.checkbox("Add grace period (interest-only months)?")

    if grace_active:
        grace_months = st.sidebar.multiselect(
            "Select grace months:",
            options=list(range(1, months + 1)),
            help="Selected months will only include interest payments"
        )

    if loan_amount <= 0 or months <= 0 or annual_rate <= 0:
        st.sidebar.error("Please enter valid loan parameters.")
        return None

    return loan_amount, annual_rate, months, repayment_method, grace_months

    

