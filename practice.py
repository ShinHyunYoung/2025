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
    .title { font-size: 2.4rem; font-weight: 800; letter-spacing: -0.5px; }
    .subtitle { opacity: 0.8; font-size: 1.1rem; }
    .pill {
        display:inline-block; padding: 6px 12px; border-radius: 999px; 
        background: #111; color:#fff; font-size:12px; margin-right:6px; margin-bottom:6px;
    }
    .song-card { 
        border-radius: 16px; padding: 18px; background: #ffffffaa; 
        backdrop-filter: blur(6px); border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        transition: transform 0.2s ease;
    }
    .song-card:hover { transform: translateY(-3px); }
    .footer { opacity: 0.7; font-size: 0.9rem; text-align:center; margin-top:20px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<div class="title">🎨 + 😶‍🌫️ → 🎶<br>색과 감정으로 오늘의 밴드 음악을 추천해요 ✨</div>
<div class="subtitle">🎵 색을 고르고 지금 감정 태그를 선택하면,<br> 감성에 맞는 인디 밴드/R&B 곡을 추천해 드립니다 💿</div>
""", unsafe_allow_html=True)

# ------------------------------------
# 밴드/인디 중심 곡 데이터
# ------------------------------------
SEED_SONGS: List[Dict] = [
    {"title":"Glass House","artist":"Redoor","moods":["몽환","쓸쓸","밤"],"color":"#9BB5FF","url":"https://www.youtube.com/watch?v=tp1l0uqyzD4"},
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
]

if "songs" not in st.session_state:
    st.session_state["songs"] = SEED_SONGS.copy()

ALL_MOODS = sorted({m for s in st.session_state["songs"] for m in s["moods"]})

# ------------------------------------
# Helper functions
# ------------------------------------
def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def color_distance_hex(hex1: str, hex2: str) -> float:
    r1, g1, b1 = [x/255 for x in hex_to_rgb(hex1)]
    r2, g2, b2 = [x/255 for x in hex_to_rgb(hex2)]
    h1, s1, v1 = colorsys.rgb_to_hsv(r1, g1, b1)
    h2, s2, v2 = colorsys.rgb_to_hsv(r2, g2, b2)
    hue = min(abs(h1-h2), 1-abs(h1-h2)) * 2
    rgb = sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)
    return hue*0.7 + rgb*0.3

def mood_overlap_score(selected: List[str], song_moods: List[str]) -> float:
    if not selected:
        return 0.2
    inter = len(set(selected) & set(song_moods))
    return inter / max(1, len(selected))

def rank_songs(user_color: str, moods: List[str], weight_color: float, weight_mood: float, k: int = 6):
    scored = []
    for s in st.session_state["songs"]:
        cd = color_distance_hex(user_color, s["color"])
        md = mood_overlap_score(moods, s["moods"])
        color_sim = 1 - min(cd / 1.5, 1)
        score = color_sim * weight_color + md * weight_mood
        scored.append((score, cd, md, s))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:k]

def embed_media(url: str, height: int = 80):
    if "youtube.com" in url or "youtu.be" in url:
        st.video(url)
    else:
        st.write(f"🔗 [노래 링크 열기]({url})")

# ------------------------------------
# Sidebar
# ------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ 추천 설정 🎛️")
    picked_color = st.color_picker("🎨 오늘의 색", "#FFC8DD")
    selected_moods = st.multiselect("😊 지금 감정 태그", options=ALL_MOODS, default=[])

    w_color = st.slider("🎨 색 매칭 비중", 0.0, 1.0, 0.55, 0.05)
    w_mood = 1.0 - w_color
    st.caption(f"→ 현재 ⚪ 색 {int(w_color*100)}% / 💭 감정 {int(w_mood*100)}%")

# ------------------------------------
# Recommendations
# ------------------------------------
results = rank_songs(picked_color, selected_moods, w_color, w_mood, k=6)

st.markdown("#### 🔥 오늘의 추천 밴드 곡 ✨")
if not results:
    st.info("😢 곡 데이터가 부족합니다. 더 많은 밴드 음악을 추가해 주세요!")
for i, (score, cd, md, s) in enumerate(results, 1):
    with st.container():
        st.markdown(
            f"""
            <div class="song-card">
                <div style="display:flex; align-items:center; gap:16px;">
                    <div style="width:20px; height:20px; border-radius:50%; background:{s['color']}; border:1px solid rgba(0,0,0,0.1);"></div>
                    <div style="flex:1;">
                        <div style="font-weight:700;">🎶 {i}. {s['title']}</div>
                        <div style="opacity:0.8;">👤 {s['artist']}</div>
                    </div>
                    <div style="text-align:right; opacity:0.8; font-size:0.85rem;">
                        ⭐ {score:.2f}<br/>
                        🎨 {1 - min(color_distance_hex(picked_color, s['color'])/1.5,1):.2f} · 😊 {md:.2f}
                    </div>
                </div>
                <div style="margin-top:8px;">{" ".join([f"<span class='pill'>#{m}</span>" for m in s['moods']])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if s.get("url"):
            embed_media(s["url"], height=80)

st.divider()
st.markdown(
    """
    <div class="footer">🌱 이 앱은 인디 밴드/R&B 기반 추천 전용이에요 🎵<br>💡 새로운 곡은 직접 추가해보세요!</div>
    """,
    unsafe_allow_html=True,
)
