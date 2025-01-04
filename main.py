import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GitHub Raw 파일 URL
file_path = 'https://raw.githubusercontent.com/yurmii/yurmi/refs/heads/main/doppler_effect_data.xlsx'

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=6)
    data = data[['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12']]
    data.columns = ['Angle', 'Time', 'Radial_Velocity']
    
    # 데이터 타입 변환 및 결측값 제거
    data = data.dropna()  # Null 값 제거
    data['Time'] = pd.to_numeric(data['Time'], errors='coerce')  # 숫자로 변환
    data['Radial_Velocity'] = pd.to_numeric(data['Radial_Velocity'], errors='coerce')  # 숫자로 변환
    data = data.dropna()  # 변환 후 다시 Null 값 제거
    return data

data = load_data()

# Streamlit UI
st.title('도플러 효과 시선속도 분석')
st.write('외계행성계에서 도플러 효과로 인한 중심별의 시선속도 변화를 분석합니다.')

# 시선속도 변화 그래프
st.subheader('시간에 따른 시선속도 변화')
fig, ax = plt.subplots()
ax.plot(data['Time'], data['Radial_Velocity'], marker='o', label='시선속도')
ax.set_xlabel('시간 (t)')
ax.set_ylabel('시선속도 (km/s)')
ax.legend()
st.pyplot(fig)

# 데이터 테이블 표시
st.subheader('데이터 테이블')
st.dataframe(data)
