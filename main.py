import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 로드
@st.cache
def load_data():
    file_path = 'https://raw.githubusercontent.com/yurmii/yurmi/main/%EB%8F%8C%ED%94%84%EB%9F%AC%20%ED%9A%A8%EA%B3%BC%20%EC%97%B0%EC%8A%B5%EC%9A%A9.xlsx'
    data = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=6)
    data = data[['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12']]
    data.columns = ['Angle', 'Time', 'Radial_Velocity']
    data = data.dropna()
    return data

data = load_data()

# 공전 시뮬레이션 함수
def orbit_simulation(data):
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
    angles = np.radians(data['Angle'])
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

# 제목 및 설명
st.title('외계 행성계 공전 시뮬레이션')
st.write('이 애플리케이션은 별과 행성이 공전하는 모습을 시뮬레이션하여 보여줍니다.')

# 공전 시뮬레이션 시각화
st.subheader('항성과 행성의 공전 궤도')
fig = orbit_simulation(data)
st.pyplot(fig)

# 데이터 테이블 표시
st.subheader('공전 데이터 테이블')
st.dataframe(data)
