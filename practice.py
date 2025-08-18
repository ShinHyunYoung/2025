import streamlit as st
import colorsys
from math import sqrt
from typing import List, Dict

st.set_page_config(
    page_title="컬러&무드 밴드 추천🎧",
    page_icon="🎶",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background: radial-gradient(1000px 500px at 10% 0%, #fff6ff, transparent),
                    radial-gradient(800px 400px at 90% 0%, #e7f5ff, transparent),
                    linear-gradient(180deg, #ffffff, #fbfbff);
    }
    .title { font-size: 2.6rem; font-weight: 800; letter-spacing: -0.5px; }
    .subtitle { opacity: 0.85; font-size: 1.15rem; }
    .pill {
        display:inline-block; padding: 6px 12px; border-radius: 999px; 
        background: #111; color:#fff; font-size:12px; margin-right:6px; margin-bottom:6px;
    }
    .song-card { 
        border-radius: 16px; padding: 20px; background: #ffffffcc; 
        backdrop-filter: blur(6px); border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        transition: transform 0.2s ease;
    }
    .song-card:hover { transform: translateY(-3px); }
    .song-title { font-size:1.5rem; font-weight:700; }
    .song-artist { font-size:1.3rem; opacity:0.85; margin-bottom:4px; }
    .footer { opacity: 0.7; font-size: 0.9rem; text-align:center; margin-top:20px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<div class="title">🎨 + 😶‍🌫️ → 🎶<br>색과 감정으로 오늘의 밴드 음악을 추천해요 ✨</div>
<div class="subtitle">🎵 색을 고르고 지금 감정 태그를 선택하면,<br> 감성에 맞는 인디 밴드/R&B 곡을 추천해 드립니다 💿</div>
""", unsafe_allow_html=True)

# 밴드/인디 중심 곡 데이터
SEED_SONGS: List[Dict] = [
    {"title":"영원은 그렇듯","artist":"Redoor","moods":["몽환","쓸쓸","밤"],"color":"#9BB5FF","url":"https://www.youtube.com/watch?v=nX6jTzFQ2P0"},
    {"title":"사랑의 미학","artist":"Redoor","moods":["서정","쓸쓸","몽환"],"color":"#AEC6FF","url":"https://www.youtube.com/watch?v=umLm9d6V95c"},
    {"title":"Dreamer","artist":"오월오일 (May05)","moods":["따뜻함","여유","서정"],"color":"#FFD6A5","url":"https://www.youtube.com/watch?v=szjjK9PT6nM"},
    {"title":"Dive","artist":"Wave to Earth","moods":["고요","몽환","서정"],"color":"#A3D5FF","url":"https://www.youtube.com/watch?v=aAZGszNvV-Y"},
    {"title":"Snooze","artist":"검정치마","moods":["쓸쓸","밤","여유"],"color":"#B5B5FF","url":"https://www.youtube.com/watch?v=ZcFqPbc3nGk"},
    {"title":"Blue","artist":"Adoy","moods":["몽환","여유","밤"],"color":"#7F9CF5","url":"https://www.youtube.com/watch?v=4tYVd21RdJc"},
    {"title":"Island","artist":"Off the menu","moods":["행복","여유","따뜻함"],"color":"#FFE3A3","url":"https://www.youtube.com/watch?v=3xyWmZ5_pjs"},
    {"title":"Love Again","artist":"SURL","moods":["설렘","밤","서정"],"color":"#94A3B8","url":"https://www.youtube.com/watch?v=ZyqLz6oQ3L4"},
    {"title":"Okinawa","artist":"Wave to Earth","moods":["여유","고요","따뜻함"],"color":"#C6F6D5","url":"https://www.youtube.com/watch?v=CEUQ33K1coU"},
    {"title":"Mango","artist":"Saevom","moods":["상큼","경쾌","여유"],"color":"#FFD166","url":"https://www.youtube.com/watch?v=fVgxu9q2gHQ"},
    {"title":"Walk in the Night","artist":"Se So Neon","moods":["몽환","밤","쓸쓸"],"color":"#6C63FF","url":"https://www.youtube.com/watch?v=6dVZ-nU5Hyo"},
    {"title":"Moonlight","artist":"ADOY","moods":["설렘","몽환","밤"],"color":"#FFAFCC","url":"https://www.youtube.com/watch?v=YoYHBn3sWGU"},
    {"title":"Orange","artist":"달리","moods":["상큼","행복","따뜻함"],"color":"#FF9AA2","url":"https://www.youtube.com/watch?v=elZbUQ4M1bI"},
    {"title":"Youth","artist":"Parannoul","moods":["쓸쓸","몽환","서정"],"color":"#A0AEC0","url":"https://www.youtube.com/watch?v=lW9aljVwMTY"},
    {"title":"Forest","artist":"Silica Gel","moods":["몽환","희망","상승"],"color":"#D8B4FE","url":"https://www.youtube.com/watch?v=K9dw-7buv2M"},
    {"title":"Night Drive","artist":"ADOY","moods":["몽환","밤","서정"],"color":"#C1C8E4","url":"https://www.youtube.com/watch?v=5hYxG4eZ3vA"},
    {"title":"Butterfly","artist":"Wave to Earth","moods":["설렘","행복","여유"],"color":"#FFF3C4","url":"https://www.youtube.com/watch?v=H5F4YxXyG6M"},
]

if "songs" not in st.session_state:
    st.session_state["songs"] = SEED_SONGS.copy()

ALL_MOODS = sorted({m for s in st.session_state["songs"] for m in s["moods"]})

# Helper functions (생략, 이전과 동일)
# Sidebar (생략, 이전과 동일)
# Recommendations (생략, 이전과 동일)
