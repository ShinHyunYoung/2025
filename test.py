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

# 밴드/인디 중심 곡 데이터 정의
SEED_SONGS: List[Dict] = [
    {"title":"영원은 그렇듯","artist":"Redoor","moods":["몽환","쓸쓸","밤"],"color":"#9BB5FF","url":"https://youtu.be/E5BLkMGxDgQ?si=h5qkQCNpQm1i2SrM"},
    {"title":"사랑의 미학","artist":"Redoor","moods":["서정","쓸쓸","몽환"],"color":"#AEC6FF","url":"https://youtu.be/3VlqlntAOt8?si=peG7VJ_ZVXLk0av9"},
    {"title":"tree","artist":"오월오일 (May05)","moods":["따뜻함","여유","서정"],"color":"#FFD6A5","urlhttps://youtu.be/BuwE1zC7xg4?si=V10t0RC4KuvLwydd"},
    {"title":"Tik Tak Tok (feat. So!YoON!)","artist":"Silica Gel","moods":["몽환","밤","에너지"],"color":"#C0C8E4","url":"https://youtu.be/VpZjRvy8AR8?si=vcH-PWWnP578F7mZ"},
    {"title":"NO PAIN","artist":"Silica Gel","moods":["강렬","현대록","감정 분출"],"color":"#708090","url":"https://youtu.be/JaIMSzE5yLA?si=WYGvPv5tscSTxdMQ"},
    {"title": "EVERYTHING", "artist": "The Black Skirts", "moods": ["서정", "쓸쓸", "밤"], "color": "#F4BFBF",
     "url": "https://youtu.be/ITnT4L988G0?si=A8xafs2vCluRSt0G"},
    {"title": "나무", "artist": "Car, the garden", "moods": ["따뜻함", "감성", "휴식"], "color": "#C8E6C9",
     "url": "https://youtu.be/cHkDZ1ekB9U?si=CIuMKkSN0xII482Z"},
    {"title":"So let's go see the stars","artist":"BOYNEXTDOOR","moods":["낭만","밤","청춘"],"color":"#A1C5FF","url":"https://youtu.be/3kAbNPj7-aM?si=8VQ0r7h1hRkvV-3O"},


    # 추가 곡도 동일 형식으로 넣어주세요
]

# session_state 초기화 전에 SEED_SONGS 정의가 반드시 필요
if "songs" not in st.session_state:
    st.session_state["songs"] = SEED_SONGS.copy()

ALL_MOODS = sorted({m for s in st.session_state["songs"] for m in s["moods"]})

# Sidebar: 컬러 선택과 감정 선택창 추가
with st.sidebar:
    st.markdown("### 🎨 오늘의 색과 감정 선택")
    picked_color = st.color_picker("색 선택", "#FFC8DD")
    selected_moods = st.multiselect("감정 선택", options=ALL_MOODS, default=[])
    w_color = st.slider("🎨 색 매칭 비중", 0.0, 1.0, 0.55, 0.05)
    w_mood = 1.0 - w_color
    st.caption(f"→ 현재 ⚪ 색 {int(w_color*100)}% / 💭 감정 {int(w_mood*100)}%")

# Helper functions, Recommendations 코드 등 기존대로 유지

