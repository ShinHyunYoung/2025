import streamlit as st

st.set_page_config(
    page_title="컬러&무드 밴드 추천🎧",
    page_icon="🎶",
    layout="wide",
)

st.markdown("""
<style>
.song-card { 
    border-radius: 16px; padding: 20px; background: #ffffffcc; 
    backdrop-filter: blur(6px); border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}
.song-title { font-size:1.5rem; font-weight:700; }
.song-artist { font-size:1.3rem; opacity:0.85; margin-bottom:4px; }
</style>
""", unsafe_allow_html=True)

# 지정 아티스트 곡 데이터
SEED_SONGS = [
    {"title":"영원은 그렇듯","artist":"Redoor","moods":["몽환","쓸쓸"],"color":"#9BB5FF","url":"https://youtu.be/E5BLkMGxDgQ?si=Fq_QbdaN5XEfnnnL"},
    {"title":"사랑의 미학","artist":"Redoor","moods":["서정","몽환"],"color":"#AEC6FF","url":"https://youtu.be/3VlqlntAOt8?si=cxjnyiN0nGSxDbzX"},
    {"title":"tree","artist":"오월오일 (May05)","moods":["따뜻함","여유"],"color":"#FFD6A5","url":"https://youtu.be/eT54rGmRvLQ?si=0lXwuXcn19-zrI3O"},
    {"title":"Everything","artist":"검정치마","moods":["쓸쓸","밤"],"color":"#A0A0FF","url":"https://youtu.be/ITnT4L988G0?si=NgpCOKApJbkx3MXR"},
    {"title":"Realize","artist":"Silica Gel","moods":["몽환","청춘"],"color":"#B5E0FF","url":"https://youtu.be/mIuIAlGLlyM?si=LPCdwKMpWRkg8bnu"},
    {"title":"NO PAIN","artist":"Silica Gel","moods":["강렬","몽환"],"color":"#B0D0FF","url":"https://youtu.be/JaIMSzE5yLA?si=-X5jlhPzt3wJllkg"},
    {"title":"나무","artist":"카더가든","moods":["따뜻함","서정"],"color":"#FFD4A5","url":"https://youtu.be/cHkDZ1ekB9U?si=vpBXpdqa7O6SQpy7"},
    {"title":"So let's go see the stars","artist":"BOYNEXTDOOR","moods":["청춘","낭만"],"color":"#A1C5FF","url":"https://youtu.be/3kAbNPj7-aM?si=vNdUc5ymtASOLLxG"},
    {"title":"Die 4 you","artist":"Dean","moods":["쓸쓸","밤"],"color":"#C8C8C8","url":"https://youtu.be/xrxxALETANY?si=Clvja35mZ5a6G8H5"}
]

if "songs" not in st.session_state:
    st.session_state["songs"] = SEED_SONGS.copy()

ALL_MOODS = sorted({m for s in st.session_state["songs"] for m in s["moods"]})

with st.sidebar:
    st.markdown("### 🎨 오늘의 색과 감정 선택")
    picked_color = st.color_picker("색 선택", "#FFC8DD")
    selected_moods = st.multiselect("감정 선택", options=ALL_MOODS, default=[])
    confirm = st.button("🔍 추천곡 확인")

if confirm:
    st.markdown("### 🎶 추천 곡")
    for song in st.session_state["songs"]:
        if not selected_moods or any(m in song["moods"] for m in selected_moods):
            st.markdown(f"<div class='song-card'><div class='song-title'>{song['title']}</div><div class='song-artist'>{song['artist']}</div><iframe width='300' height='150' src='{song['url'].replace('watch?v=','embed/')}' frameborder='0' allowfullscreen></iframe></div>", unsafe_allow_html=True)
