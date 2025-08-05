import streamlit as st

# 타이틀
st.title("🎉 나의 첫 Streamlit 앱")

# 텍스트 출력
st.write("안녕하세요! 이것은 간단한 Streamlit 예제입니다.")

# 숫자 입력 받고 제곱 출력
number = st.number_input("숫자를 입력하세요", min_value=1, max_value=100)
st.write(f"{number}의 제곱은 {number ** 2}입니다.")

# 버튼
if st.button("버튼을 눌러보세요"):
    st.success("버튼이 눌렸어요! 🎯")
