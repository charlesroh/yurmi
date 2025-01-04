import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

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

# 공전 궤도 애니메이션
st.subheader("항성과 행성의 공전 궤도")

# 시간 데이터 생성
time_steps = np.linspace(0, P, 200)

# 궤도 데이터 생성
star_x = R * np.cos(2 * np.pi * time_steps / P + np.pi)
star_y = R * np.sin(2 * np.pi * time_steps / P + np.pi)
planet_x = r * np.cos(2 * np.pi * time_steps / P)
planet_y = r * np.sin(2 * np.pi * time_steps / P)

# Plotly Figure 생성
fig = go.Figure()

# 항성 및 행성 궤도 추가
fig.add_trace(go.Scatter(x=R * np.cos(np.linspace(0, 2 * np.pi, 100)),
                         y=R * np.sin(np.linspace(0, 2 * np.pi, 100)),
                         mode='lines',
                         line=dict(color='orange', dash='dash'),
                         name='항성 궤도'))
fig.add_trace(go.Scatter(x=r * np.cos(np.linspace(0, 2 * np.pi, 100)),
                         y=r * np.sin(np.linspace(0, 2 * np.pi, 100)),
                         mode='lines',
                         line=dict(color='blue', dash='dash'),
                         name='행성 궤도'))

# 애니메이션 데이터 추가
fig.add_trace(go.Scatter(x=[star_x[0]],
                         y=[star_y[0]],
                         mode='markers',
                         marker=dict(color='orange', size=10),
                         name='항성'))
fig.add_trace(go.Scatter(x=[planet_x[0]],
                         y=[planet_y[0]],
                         mode='markers',
                         marker=dict(color='blue', size=10),
                         name='행성'))

# Layout 설정
fig.update_layout(width=800, height=800,
                  xaxis=dict(range=[-700, 700]),
                  yaxis=dict(range=[-700, 700]),
                  updatemenus=[dict(type="buttons",
                                    showactive=False,
                                    buttons=[dict(label="▶ Start",
                                                  method="animate",
                                                  args=[None, dict(frame=dict(duration=50, redraw=True),
                                                                   fromcurrent=True)])])])

# 애니메이션 프레임 추가
frames = []
for t, sx, sy, px, py in zip(time_steps, star_x, star_y, planet_x, planet_y):
    frame = go.Frame(data=[go.Scatter(x=[sx], y=[sy], mode='markers',
                                      marker=dict(color='orange', size=10)),
                           go.Scatter(x=[px], y=[py], mode='markers',
                                      marker=dict(color='blue', size=10))])
    frames.append(frame)

fig.frames = frames

# Streamlit에 Plotly 그래프 표시
st.plotly_chart(fig)

# 시선속도 변화 그래프
st.subheader('시간에 따른 항성의 시선속도 변화')
Vr = (2 * np.pi * R / P) * np.sin(2 * np.pi * time_steps / P + np.pi)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=time_steps, y=Vr, mode='lines', name='시선속도'))
fig2.update_layout(width=800, height=400,
                   xaxis_title='시간 (t)',
                   yaxis_title='시선속도 (Vr)')
st.plotly_chart(fig2)
