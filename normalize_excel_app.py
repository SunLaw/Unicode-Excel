import streamlit as st
import pandas as pd
import unicodedata
from io import BytesIO

def normalize_unicode_df(df):
    # Áp dụng chuẩn hóa NFC cho toàn bộ ô là chuỗi
    return df.applymap(lambda x: unicodedata.normalize('NFC', x) if isinstance(x, str) else x)

def convert_df_to_excel(df):
    # Lưu DataFrame vào một buffer Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return output

# Giao diện web
st.set_page_config(page_title="Chuẩn hóa Unicode trong Excel")
st.title("📄 Chuẩn hóa Unicode tổ hợp → dựng sẵn trong file Excel")

uploaded_file = st.file_uploader("📤 Tải lên file Excel (.xlsx):", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("🔍 Xem trước dữ liệu gốc:")
        st.dataframe(df.head())

        if st.button("✅ Chuẩn hóa Unicode"):
            normalized_df = normalize_unicode_df(df)
            st.subheader("📋 Kết quả sau chuẩn hóa:")
            st.dataframe(normalized_df.head())

            # Tải về
            excel_file = convert_df_to_excel(normalized_df)
            st.download_button(
                label="📥 Tải xuống file đã chuẩn hóa",
                data=excel_file,
                file_name="excel_da_chuan_hoa.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")