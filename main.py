import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
@st.cache
def load_data():
    file_path = 'https://raw.githubusercontent.com/yurmii/yurmi/refs/heads/main/%EB%8F%8C%ED%94%84%EB%9F%AC%20%ED%9A%A8%EA%B3%BC%20%EC%97%B0%EC%8A%B5%EC%9A%A9.xlsx'
    data = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=6)
    data = data[['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12']]
    data.columns = ['Angle', 'Time', 'Radial_Velocity']
    data = data.dropna()
    return data

data = load_data()

# 제목 및 설명
st.title('도플러 효과 시선속도 분석')
st.write('이 애플리케이션은 외계 행성계에서 도플러 효과에 의해 변화하는 중심별의 시선속도를 분석합니다.')

# 데이터 시각화
st.subheader('시선속도 변화 그래프')
fig, ax = plt.subplots()
ax.plot(data['Time'], data['Radial_Velocity'], label='시선속도', marker='o')
ax.set_xlabel('시간 (t)')
ax.set_ylabel('시선속도 (km/s)')
ax.legend()
st.pyplot(fig)

# 데이터 테이블 표시
st.subheader('데이터 테이블')
st.dataframe(data)
