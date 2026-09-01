import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Bank Cheque Extraction",
    page_icon="🏦",
    layout="wide"
)

# ---------- HEADER ----------

st.title("🏦 Bank Cheque Data Extraction")
st.caption("AI-powered cheque information extraction from scanned documents")

st.divider()

# ---------- UPLOAD ----------

st.subheader("📄 Upload Cheque PDF")

uploaded_file = st.file_uploader(
    "Upload a scanned cheque PDF",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("👆 Upload a scanned cheque PDF to begin.")

else:
    st.success(f"Uploaded: {uploaded_file.name}")

    # Save uploaded PDF temporarily
    pdf_path = os.path.join("uploaded_cheque.pdf")

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.pdf(uploaded_file)

    st.divider()

    # ---------- EXTRACTION ----------

    if st.button("🔍 Extract Cheque Data", type="primary"):

        csv_file = "extracted_data.csv"

        if os.path.exists(csv_file):

            df = pd.read_csv(csv_file)

            st.success("✅ Cheque data extracted successfully!")

            st.subheader("📋 Extracted Cheque Information")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            # Download
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download Extracted CSV",
                data=csv,
                file_name="extracted_cheque_data.csv",
                mime="text/csv"
            )

        else:
            st.error("extracted_data.csv not found.")

st.divider()

st.caption(
    "Cheque Extraction System • Python • OpenCV • TrOCR • Streamlit"
)
