# Loan Repayment Comparison Tool

An interactive financial tool for calculating and visualizing loan repayment schedules — including **annuity and linear methods**, **custom grace periods**, and support for real-world amortization table uploads (לוח סילוקין).

---

## Key Features

- Calculate schedules for:
  - **Annuity (שפיצר)**
  - **Linear (קרן שווה)**
- Support for **grace periods** (interest-only months)
- Upload amortization tables (CSV/XLSX, Hebrew headers supported)
- Visual breakdown of principal vs. interest
- Compare calculated vs uploaded repayment schedules

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas

---
## Run Locally

Clone the repo and run it with Streamlit:

```bash
git clone https://github.com/eshokhat/loan-repayment-comparison.git
cd loan-repayment-comparison
pip install -r requirements.txt
streamlit run app.py
```

---

## Run Online

Try the live app in your browser:

👉 [Open the app on Streamlit Cloud](https://loan-repayment-comparison.streamlit.app)
