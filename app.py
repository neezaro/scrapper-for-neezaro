import streamlit as st
import pandas as pd
from scraper import scrape_data_from_url

st.set_page_config(page_title="Social & Contact Scraper", layout="centered")
st.title("🔍 Bulk Contact + Social Link Scraper")

uploaded_file = st.file_uploader("Upload CSV file with website URLs", type=["csv"])

if uploaded_file:
    df_input = pd.read_csv(uploaded_file)
    
    if "Website" not in df_input.columns:
        st.error("CSV must contain a 'Website' column.")
    else:
        st.success(f"{len(df_input)} websites loaded.")
        
        if st.button("Start Scraping"):
            results = []
            with st.spinner("Scraping in progress..."):
                for index, row in df_input.iterrows():
                    url = row['Website']
                    if not url.startswith("http"):
                        url = "http://" + url
                    data = scrape_data_from_url(url)
                    results.append(data)
            df_results = pd.DataFrame(results)
            st.success("✅ Scraping complete!")

            st.dataframe(df_results)

            csv = df_results.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results CSV", data=csv, file_name="scraped_data.csv", mime="text/csv")
