# app.py
# 💄 AI 퍼스널컬러 화장품 추천 앱

import streamlit as st

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="AI Personal Beauty",
    page_icon="💄",
    layout="wide"
)

# -----------------------------------
# 화장품 데이터
# -----------------------------------
products = [

    # 봄웜
    {
        "name": "롬앤 쥬시래스팅 틴트",
        "tone": "봄웜",
        "category": "립",
        "skin": "모든 피부",
        "price_range": "1만원 이하",
        "color": "코랄",
        "price": "12000원",
        "ingredients": ["향료", "실리콘"],
        "description": "화사한 코랄 컬러로 봄웜 추천"
    },

    {
        "name": "에스쁘아 비글로우 쿠션",
        "tone": "봄웜",
        "category": "쿠션",
        "skin": "건성",
        "price_range": "3만원 이상",
        "color": "아이보리",
        "price": "35000원",
        "ingredients": ["향료"],
        "description": "촉촉한 윤광 피부 표현"
    },

    {
        "name": "클리오 코랄 팔레트",
        "tone": "봄웜",
        "category": "섀도우",
        "skin": "복합성",
        "price_range": "1~3만원",
        "color": "오렌지 브라운",
        "price": "22000원",
        "ingredients": ["실리콘"],
        "description": "따뜻한 음영 메이크업 추천"
    },

    # 여름쿨
    {
        "name": "롬앤 베어그레이프",
        "tone": "여름쿨",
        "category": "립",
        "skin": "민감성",
        "price_range": "1만원 이하",
        "color": "쿨핑크",
        "price": "13000원",
        "ingredients": ["향료"],
        "description": "뮤트 핑크 컬러 추천"
    },

    {
        "name": "헤라 블랙 쿠션",
        "tone": "여름쿨",
        "category": "쿠션",
        "skin": "지성",
        "price_range": "3만원 이상",
        "color": "뉴트럴 베이지",
        "price": "40000원",
        "ingredients": ["실리콘"],
        "description": "세미매트 피부 표현"
    },

    {
        "name": "에뛰드 라벤더 블러셔",
        "tone": "여름쿨",
        "category": "블러셔",
        "skin": "모든 피부",
        "price_range": "1만원 이하",
        "color": "라벤더 핑크",
        "price": "10000원",
        "ingredients": ["탈크"],
        "description": "여름쿨 라이트 추천"
    },

    # 가을웜
    {
        "name": "롬앤 브릭 립",
        "tone": "가을웜",
        "category": "립",
        "skin": "건성",
        "price_range": "1~3만원",
        "color": "브릭레드",
        "price": "14000원",
        "ingredients": ["향료"],
        "description": "분위기 있는 브릭 컬러"
    },

    {
        "name": "정샘물 에센셜 쿠션",
        "tone": "가을웜",
        "category": "쿠션",
        "skin": "건성",
        "price_range": "3만원 이상",
        "color": "샌드 베이지",
        "price": "42000원",
        "ingredients": ["향료"],
        "description": "고급스러운 윤광 피부 표현"
    },

    {
        "name": "3CE 무드레시피",
        "tone": "가을웜",
        "category": "섀도우",
        "skin": "복합성",
        "price_range": "3만원 이상",
        "color": "브라운",
        "price": "38000원",
        "ingredients": ["탈크", "실리콘"],
        "description": "딥 브라운 음영 추천"
    },

    # 겨울쿨
    {
        "name": "에뛰드 픽싱틴트",
        "tone": "겨울쿨",
        "category": "립",
        "skin": "지성",
        "price_range": "1~3만원",
        "color": "플럼",
        "price": "14000원",
        "ingredients": ["향료", "알코올"],
        "description": "채도 높은 플럼 컬러"
    },

    {
        "name": "바닐라코 커버리셔스 쿠션",
        "tone": "겨울쿨",
        "category": "쿠션",
        "skin": "지성",
        "price_range": "3만원 이상",
        "color": "쿨 바닐라",
        "price": "33000원",
        "ingredients": ["실리콘"],
        "description": "화사한 쿨톤 피부 표현"
    },

    {
        "name": "릴리바이레드 쿨톤 팔레트",
        "tone": "겨울쿨",
        "category": "섀도우",
        "skin": "복합성",
        "price_range": "1~3만원",
        "color": "플럼 브라운",
        "price": "29000원",
        "ingredients": ["실리콘"],
        "description": "강한 대비 메이크업 추천"
    }
]

# -----------------------------------
# 제목
# -----------------------------------
st.title("💄 AI 퍼스널컬러 화장품 추천 앱")
st.write("퍼스널컬러 기반 화장품 추천 + 성분 분석")

# -----------------------------------
# 사이드바 설정
# -----------------------------------
st.sidebar.header("🎨 퍼스널컬러 설정")

# 퍼스널컬러 선택
tone = st.sidebar.selectbox(
    "퍼스널컬러 선택",
    ["봄웜", "여름쿨", "가을웜", "겨울쿨"]
)

# 피부 타입 선택
skin_type = st.sidebar.selectbox(
    "피부 타입",
    ["모든 피부", "건성", "지성", "복합성", "민감성"]
)

# 가격대 선택
price_range = st.sidebar.selectbox(
    "가격대",
    ["전체", "1만원 이하", "1~3만원", "3만원 이상"]
)

# 화장품 종류 선택
category = st.sidebar.selectbox(
    "화장품 종류",
    [
        "전체",
        "립",
        "쿠션",
        "섀도우",
        "블러셔",
        "아이브로우",
        "하이라이터",
        "파운데이션",
        "틴트",
        "마스카라"
    ]
)

# -----------------------------------
# 추천 제품 필터링
# -----------------------------------
recommended = []

for product in products:

    tone_match = product["tone"] == tone

    skin_match = (
        skin_type == "모든 피부"
        or product["skin"] == skin_type
        or product["skin"] == "모든 피부"
    )

    price_match = (
        price_range == "전체"
        or product["price_range"] == price_range
    )

    category_match = (
        category == "전체"
        or product["category"] == category
    )

    if tone_match and skin_match and price_match and category_match:
        recommended.append(product)

# -----------------------------------
# 추천 결과
# -----------------------------------
st.header(f"✨ {tone} 추천 화장품")

if recommended:

    for item in recommended:

        st.subheader(f"💄 {item['name']}")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"📂 카테고리: {item['category']}")
            st.write(f"🎨 컬러: {item['color']}")
            st.write(f"💰 가격: {item['price']}")
            st.write(f"🧴 피부 타입: {item['skin']}")

        with col2:
            st.write("🤖 AI 추천 이유")
            st.info(item["description"])

        # 성분 분석
        st.write("🧪 성분 분석")

        ingredients = item["ingredients"]

        if "향료" in ingredients:
            st.warning("향료 포함 → 민감성 피부 주의")

        if "알코올" in ingredients:
            st.warning("알코올 포함 → 건성 피부 주의")

        if "실리콘" in ingredients:
            st.info("실리콘 포함 → 모공 막힘 가능성")

        if "탈크" in ingredients:
            st.info("탈크 포함 → 민감 피부 주의")

        st.success("AI 성분 분석 완료 ✅")

        st.divider()

else:
    st.error("해당 조건의 추천 제품이 없습니다.")

# -----------------------------------
# 퍼스널컬러 설명
# -----------------------------------
st.header("🎨 퍼스널컬러 분석")

tone_description = {

    "봄웜": """
    🌸 밝고 따뜻한 코랄, 피치 계열 추천
    생기 있고 화사한 메이크업이 잘 어울립니다.
    """,

    "여름쿨": """
    ❄️ 로즈핑크, 라벤더 계열 추천
    부드럽고 뮤트한 메이크업 추천
    """,

    "가을웜": """
    🍂 브릭, 브라운, 테라코타 계열 추천
    분위기 있고 깊은 메이크업 추천
    """,

    "겨울쿨": """
    💎 플럼, 체리레드 계열 추천
    선명하고 강한 대비 메이크업 추천
    """
}

st.info(tone_description[tone])

# -----------------------------------
# 인기 추천템
# -----------------------------------
st.header("🔥 퍼컬별 인기템")

popular_items = {

    "봄웜": [
        "롬앤 코랄틴트",
        "에스쁘아 비글로우 쿠션",
        "클리오 코랄 팔레트"
    ],

    "여름쿨": [
        "롬앤 베어그레이프",
        "헤라 블랙 쿠션",
        "라벤더 블러셔"
    ],

    "가을웜": [
        "3CE 무드레시피",
        "롬앤 브릭 립",
        "정샘물 쿠션"
    ],

    "겨울쿨": [
        "에뛰드 플럼틴트",
        "바닐라코 쿠션",
        "릴리바이레드 팔레트"
    ]
}

for item in popular_items[tone]:
    st.write("💋", item)

# -----------------------------------
# 푸터
# -----------------------------------
st.markdown("---")
st.caption("Made with Streamlit 💖")
