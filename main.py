import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

# 초기 변수 설정
M = 300  # 항성 질량
m = 30   # 행성 질량
r = 300  # 행성의 공전 반지름 (고정)
P = 100  # 공전 주기
R = (m * r) / M  # 초기 항성의 공전 반지름 계산

# Streamlit 앱 제목
st.title('외계행성계 공전 시뮬레이션 및 시선속도 분석')
st.write("항성 질량(M), 행성 질량(m)을 변경하여 궤도를 확인하세요.")

# 사용자 입력을 통해 질량 값 변경
M = st.number_input("항성 질량 (M):", value=M, step=10)
m = st.number_input("행성 질량 (m):", value=m, step=1)
R = (m * r) / M  # 항성의 공전 반지름 업데이트

# 시뮬레이션 초기화
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-700, 700)
ax.set_ylim(-700, 700)
ax.set_xlabel('X 좌표 (AU)')
ax.set_ylabel('Y 좌표 (AU)')

# 궤도 점선 초기화
star_orbit, = ax.plot([], [], 'orange', linestyle='--', label='항성 궤도')
planet_orbit, = ax.plot([], [], 'blue', linestyle='--', label='행성 궤도')

# 궤도 업데이트
angles = np.linspace(0, 2 * np.pi, 100)
star_x = R * np.cos(angles)
star_y = R * np.sin(angles)
planet_x = r * np.cos(angles)
planet_y = r * np.sin(angles)
star_orbit.set_data(star_x, star_y)
planet_orbit.set_data(planet_x, planet_y)

# 실시간 좌표 점 초기화
star_point, = ax.plot([], [], 'o', color='orange', label='항성')
planet_point, = ax.plot([], [], 'o', color='blue', label='행성')

# 애니메이션 함수
def update(frame):
    t = frame / 10.0  # 시간 증가
    star_x = R * np.cos(2 * np.pi * t / P + np.pi)
    star_y = R * np.sin(2 * np.pi * t / P + np.pi)
    planet_x = r * np.cos(2 * np.pi * t / P)
    planet_y = r * np.sin(2 * np.pi * t / P)

    star_point.set_data(star_x, star_y)
    planet_point.set_data(planet_x, planet_y)
    return star_point, planet_point

ani = FuncAnimation(fig, update, frames=range(1000), interval=50, blit=True)
st.pyplot(fig)

# 시선속도 변화 그래프
st.subheader('시간에 따른 항성의 시선속도 변화')
times = np.linspace(0, P, 1000)
Vr = (2 * np.pi * R / P) * np.sin(2 * np.pi * times / P + np.pi)
fig2, ax2 = plt.subplots()
ax2.plot(times, Vr, label='시선속도')
ax2.set_xlabel('시간 (t)')
ax2.set_ylabel('시선속도 (Vr)')
ax2.legend()
st.pyplot(fig2)
