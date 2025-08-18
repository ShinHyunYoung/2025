import streamlit as st

# MBTI와 직업 매핑 데이터
career_dict = {
    "INTJ": ["전략기획가", "과학자", "개발자"],
    "ENTP": ["기업가", "마케터", "컨설턴트"],
    "INFJ": ["상담가", "작가", "교사"],
    "ESFP": ["배우", "이벤트 플래너", "영업직"],
    # 나머지 MBTI도 채우면 됨
}

st.title("MBTI 기반 진로 추천 사이트 🎯")

# 선택 박스
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=list(career_dict.keys())
)

# 추천 직업 보여주기
if mbti:
    st.subheader(f"✨ {mbti} 유형 추천 직업")
    for job in career_dict[mbti]:
        st.write(f"- {job}")

