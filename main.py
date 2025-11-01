import requests
import streamlit as st



st.set_page_config(page_title="Mushaf Quranic Web APP", layout="centered")

# --- Custom CSS for Amiri Quran Font ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri+Quran&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Amiri Quran', serif;
    }

    .quran-text {
        font-family: 'Amiri Quran', serif;
        font-size: 28px;
        direction: rtl;
        text-align: right;
        line-height: 2.3;
    }

    .english-title {
        font-family: 'Segoe UI', sans-serif;
        font-size: 20px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)






st.title("Mushaf Quranic Web APP ")


response= requests.get("https://api.alquran.cloud/v1/surah").json()["data"]





surahIndex=[f"{s["number"]}.{s["name"]}{s["englishName"]}"  for s  in response]


st.sidebar.title("Controls")
surahname=st.sidebar.selectbox("select surah",surahIndex)


surahnum=int(surahname.split(".")[0])


reciters=[
    "ar.abdurrahmaansudais",
    "ar.saoodshuraym",
    "ar.mahermuaiqly",
    "ar.alafasy"]

reciter = st.sidebar.selectbox("select a reciter", reciters)


show_recitation=st.sidebar.checkbox("Show Recitation")

response_surah= requests.get(f"https://api.alquran.cloud/v1/surah/{surahnum}/{reciter}").json()["data"]["ayahs"]



for ayah in response_surah:
    # st.write(ayah["text"])
    st.markdown(f"<div class='quran-text'>{ayah['text']}</div>", unsafe_allow_html=True)
    if show_recitation:
        st.audio(ayah["audio"])