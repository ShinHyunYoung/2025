import streamlit as st
import colorsys
from math import sqrt

st.set_page_config(
    page_title="컬러&무드 밴드 추천🎧",
    page_icon="🎶",
    layout="wide",
)

st.markdown("""
<style>
.main {
    background: radial-gradient(1000px 500px at 10% 0%, #fff6ff, transparent),
                radial-gradient(800px 400px at 90% 0%, #e7f5ff, transparent),
                linear-gradient(180deg, #ffffff, #fbfbff);
}
.song-card { 
    border-radius: 16px; padding: 20px; background: #ffffffcc; 
    backdrop-filter: blur(6px); border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}
.song-title { font-size:1.5rem; font-weight:700; }
.song-artist { font-size:1.3rem; opacity:0.85; margin-bottom:4px; }
</style>
""", unsafe_allow_html=True)

SEED_SONGS = [
    {"title":"tree","artist":"오월오일 (May05)","moods":["따뜻함","여유","서정"],"color":"#FFD6A5","url":"https://youtu.be/BuwE1zC7xg4"},
    {"title":"영원은 그렇듯","artist":"Redoor","moods":["몽환","쓸쓸","밤"],"color":"#9BB5FF","url":"https://www.youtube.com/watch?v=nX6jTzFQ2P0"},
    {"title":"사랑의 미학","artist":"Redoor","moods":["서정","쓸쓸","몽환"],"color":"#AEC6FF","url":"https://www.youtube.com/watch?v=umLm9d6V95c"},
    {"title":"So let's go see the stars","artist":"BOYNEXTDOOR","moods":["낭만","밤","청춘"],"color":"#A1C5FF","url":"https://www.youtube.com/watch?v=8JoqUs9Y1EY"}
]

if "songs" not in st.session_state:
    st.session_state["songs"] = SEED_SONGS.copy()

ALL_MOODS = sorted({m for s in st.session_state["songs"] for m in s["moods"]})

with st.sidebar:
    st.markdown("### 🎨 오늘의 색과 감정 선택")
    picked_color = st.color_picker("색 선택", "#FFC8DD")
    selected_moods = st.multiselect("감정 선택", options=ALL_MOODS, default=[])
    w_color = st.slider("🎨 색 매칭 비중", 0.0, 1.0, 0.55, 0.05)
    w_mood = 1.0 - w_color
    confirm = st.button("🔍 추천곡 확인")

if confirm:
    st.markdown("### 🎶 추천 곡")
    for song in st.session_state["songs"]:
        if any(m in song["moods"] for m in selected_moods):
            st.markdown(f"<div class='song-card'><div class='song-title'>{song['title']}</div><div class='song-artist'>{song['artist']}</div><iframe width='300' height='150' src='{song['url'].replace('watch?v=','embed/')}' frameborder='0' allowfullscreen></iframe></div>", unsafe_allow_html=True)
