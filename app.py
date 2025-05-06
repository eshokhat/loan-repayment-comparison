import streamlit as st
from ui.input_form import loan_input_form
from ui.summary import show_loan_summary, show_method_comparison
from ui.charts import plot_payment_breakdown, plot_remaining_balance, plot_compare_remaining
from ui.upload_tab import handle_upload_tab
from logic.calculator import calculate_annuity, calculate_linear


st.set_page_config(page_title="Debt Repayment Visualizer", layout="centered")
st.title("Debt Repayment Visualizer")

page = st.sidebar.selectbox(
    "Select a page:",
    ["Loan Calculator", "📂 Upload Amortization Table (לוח סילוקין)"]
)
if page == "Loan Calculator":

    params = loan_input_form()
    if not params:
        st.stop()
    loan_amount, annual_rate, months, repayment_method, grace_months = params
    compare = st.checkbox("🔍 Compare with other method")

    try:
        # Calculate selected schedule
        if repayment_method == "Annuity":
            schedule = calculate_annuity(loan_amount, annual_rate, months, grace_months)
        else:
            schedule = calculate_linear(loan_amount, annual_rate, months, grace_months)
        # Show metrics
        show_loan_summary(schedule)
        plot_payment_breakdown(schedule)
        plot_remaining_balance(schedule)
        st.markdown("### Repayment Schedule (Preview)")
        st.dataframe(schedule, use_container_width=True)

        # --- Comparison logic ---
        if compare:
            st.markdown("---")
            st.subheader(" Comparison: Annuity vs Linear")

            # Calculate both methods
            annuity_df = calculate_annuity(loan_amount, annual_rate, months)
            linear_df = calculate_linear(loan_amount, annual_rate, months)

            # Show side-by-side summary
            show_method_comparison(annuity_df, linear_df)

            # Compare balance dynamics
            plot_compare_remaining(annuity_df, linear_df)

    except Exception as e:
        st.error(f"Something went wrong during calculation: {e}")

if page == "📂 Upload Amortization Table (לוח סילוקין)":
    handle_upload_tab()