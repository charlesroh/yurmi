import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
st.title('도플러 효과 분석 및 궤도 시뮬레이션')
st.write('외계행성계에서 도플러 효과로 인한 중심별의 시선속도 변화를 분석하고 별과 행성의 궤도를 시뮬레이션합니다.')

# 별과 행성의 궤도 시뮬레이션
st.subheader('별과 행성의 공전 궤도')

def orbit_simulation():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim(-700, 700)
    ax.set_ylim(-700, 700)
    ax.set_xlabel('X 좌표 (AU)')
    ax.set_ylabel('Y 좌표 (AU)')

    # 별과 행성의 공전 반지름
    star_orbit_radius = 60  # AU
    planet_orbit_radius = 600  # AU

    # 공전 데이터 생성
    angles = np.linspace(0, 2 * np.pi, len(data))  # 각도 데이터 (0~360도)
    star_x = star_orbit_radius * np.cos(angles)
    star_y = star_orbit_radius * np.sin(angles)
    planet_x = planet_orbit_radius * np.cos(angles)
    planet_y = planet_orbit_radius * np.sin(angles)

    # 궤도 그리기
    ax.plot(star_x, star_y, label='항성 궤도', color='orange')
    ax.plot(planet_x, planet_y, label='행성 궤도', color='blue')

    # 초기 위치 표시
    ax.scatter([star_x[0]], [star_y[0]], color='orange', label='항성 초기 위치', zorder=5)
    ax.scatter([planet_x[0]], [planet_y[0]], color='blue', label='행성 초기 위치', zorder=5)

    ax.legend()
    return fig

fig1 = orbit_simulation()
st.pyplot(fig1)

# 시선속도 변화 그래프
st.subheader('시간에 따른 시선속도 변화')
fig2, ax2 = plt.subplots()
ax2.plot(data['Time'], data['Radial_Velocity'], marker='o', label='시선속도')
ax2.set_xlabel('시간 (t)')
ax2.set_ylabel('시선속도 (km/s)')
ax2.legend()
st.pyplot(fig2)
