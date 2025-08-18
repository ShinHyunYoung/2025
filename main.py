import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎓", layout="centered")

# 헤더
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🎓 MBTI 기반 진로 추천 사이트 ✨</h1>", unsafe_allow_html=True)
st.write("---")

# MBTI-직업 매핑
career_dict = {
    "INTJ": ["🧠 전략기획가", "🔬 과학자", "💻 개발자"],
    "ENTP": ["🚀 기업가", "📣 마케터", "🧑‍💼 컨설턴트"],
    "INFJ": ["💖 상담가", "📖 작가", "🍎 교사"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "🤝 영업직"],
    "ISTJ": ["📊 회계사", "⚖️ 판사", "🏦 은행원"],
    "ENFP": ["🌈 크리에이터", "🎤 아티스트", "📱 콘텐츠 기획자"],
    "ISFJ": ["🧑‍⚕️ 간호사", "🏫 교사", "🛟 사회복지사"],
    "ESTP": ["🏅 운동선수", "📺 방송인", "🛠️ 기술영업"],
    "ENTJ": ["👑 CEO", "🪄 리더십 코치", "📊 전략 컨설턴트"],
    "INTP": ["🔍 연구원", "🧩 분석가", "💻 개발자"],
    "ESFJ": ["🤗 상담사", "📋 HR 매니저", "🍳 요리사"],
    "ISTP": ["🔧 엔지니어", "✈️ 파일럿", "🚓 경찰관"],
    "ENFJ": ["🎤 강연가", "🧑‍🏫 교육자", "🤝 NGO 활동가"],
    "ISFP": ["🎨 디자이너", "🎶 음악가", "📷 사진작가"],
    "ESTJ": ["🏢 관리자", "📑 행정가", "⚙️ 운영 책임자"],
    "INFP": ["📝 시인", "🎬 영화감독", "🎨 일러스트레이터"]
}

# MBTI 선택
mbti = st.selectbox("✨ 당신의 MBTI를 선택하세요:", options=list(career_dict.keys()))

# 추천 결과
if mbti:
    st.markdown(f"<h2 style='color:#FF6F61;'>✨ {mbti} 유형 추천 직업 ✨</h2>", unsafe_allow_html=True)
    st.success("🌟 당신에게 어울리는 직업들이에요!")
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")

    st.write("---")
    st.info("💡 MBTI는 참고용이에요! 가장 중요한 건 당신의 열정과 꾸준함 💪")
