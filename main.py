import streamlit as st

# 앱 제목
st.title('나의 첫 Streamlit 프로젝트')

# 설명 문구
st.write('안녕하세요! Streamlit에 오신 것을 환영합니다.')

# 간단한 입력 필드와 버튼
user_input = st.text_input('이름을 입력해주세요:')
if st.button('확인'):
    st.write(f'{user_input}님, 반갑습니다!')

# 간단한 숫자 입력과 계산
a = st.number_input('첫 번째 숫자를 입력하세요:', min_value=0, value=0)
b = st.number_input('두 번째 숫자를 입력하세요:', min_value=0, value=0)

if st.button('더하기 실행'):
    st.write(f'결과: {a + b}')
