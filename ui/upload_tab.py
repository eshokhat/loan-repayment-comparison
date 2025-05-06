# ui/upload_tab.py

import streamlit as st
import pandas as pd
from ui.charts import plot_uploaded_schedule


def handle_upload_tab():
    st.subheader("📂 Upload לוח סילוקין (Amortization Table)")

    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Read file
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("✅ File loaded successfully.")
            st.markdown("### 📋 Raw Preview")
            st.dataframe(df, use_container_width=True)

            # --- Column detection ---
            col_map = {
                "Month": ["מספר תשלום", "חודש", "תאריך", "Month"],
                "Payment": ["החזר חודשי", "סה\"כ תשלום", "תשלום", "Payment"],
                "Interest": ["פרעון ריבית", "ריבית", "Interest"],
                "Principal": ["פרעון קרן", "קרן", "Principal"],
                "Balance": ["יתרה", "יתרת קרן", "Balance"]
            }

            detected = {}

            for key, options in col_map.items():
                for col in df.columns:
                    if str(col).strip() in options:
                        detected[key] = col
                        break

            missing = [key for key in col_map if key not in detected]

            if missing:
                st.warning(f"Could not detect the following required fields: {', '.join(missing)}")
                return
            else:
                st.success("✅ All key fields detected.")
                for k, v in detected.items():
                    st.markdown(f"- **{k}** → `{v}`")

            # --- Normalize table ---
            st.markdown("### ✅ Normalized Table")
            normalized_df = pd.DataFrame({
                "Month": df[detected["Month"]],
                "Payment": df[detected["Payment"]],
                "Principal": df[detected["Principal"]],
                "Interest": df[detected["Interest"]],
                "Remaining Balance": df[detected["Balance"]],
            })

            st.dataframe(normalized_df, use_container_width=True)

            # Optional: summary
            st.markdown("### Summary")
            st.metric("Total Paid", f"{normalized_df['Payment'].sum():,.2f} ₪")
            st.metric("Total Interest", f"{normalized_df['Interest'].sum():,.2f} ₪")
            
            plot_uploaded_schedule(normalized_df)
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
    else:
        st.info("Upload an amortization table to begin.")

