import os
import requests as rq
import streamlit as st


BACKEND_URL = "backend"
BACKEND_PORT = os.getenv('BACKEND_PORT')

DEFAULT_TEXT = """В тихом городке, утопающем в зелени, располагался старинный парк.
Каждый уголок этого места хранил в себе множество тайн и историй.
Здесь, среди раскидистых деревьев и цветущих кустарников, можно было услышать шепот ветра,
который словно делился своими секретами с прохожими.
На одной из скамеек сидела пожилая женщина, её лицо было обрамлено серебристыми волосами, а глаза светились добротой."""

st.set_page_config(page_title="Voicing text", layout="wide")

st.header("Введите текст для озвучания")

text = st.text_area("Введите текст", placeholder=DEFAULT_TEXT, value=DEFAULT_TEXT, height=400)

if text:
    request_json = {
        "text": text
    }

    response = rq.post(f"http://{BACKEND_URL}:{BACKEND_PORT}/voice/", json=request_json)

    if response.status_code == 200:
        st.audio(response.content, format="audio/wav")
    else:
        st.error(response, icon="🚨")
