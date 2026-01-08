import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 앱 제목
st.title('초등학교 곱셈 학습용 웹 애플리케이션')

# 세션 상태 초기화
if 'num1' not in st.session_state:
    st.session_state.num1 = 1
if 'num2' not in st.session_state:
    st.session_state.num2 = 1
if 'image_option' not in st.session_state:
    st.session_state.image_option = '사과'
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

# 레이아웃 설정
col1, col2 = st.columns(2)

with col1:
    st.session_state.num1 = st.number_input('첫 번째 숫자를 입력하세요:', min_value=1, max_value=10, value=st.session_state.num1)

with col2:
    st.session_state.num2 = st.number_input('두 번째 숫자를 입력하세요:', min_value=1, max_value=10, value=st.session_state.num2)

st.session_state.image_option = st.selectbox('어떤 그림으로 시각화할까요?', ['사과', '바나나', '배'], index=['사과', '바나나', '배'].index(st.session_state.image_option))

# 곱셈 결과 계산
result = st.session_state.num1 * st.session_state.num2

# 곱셈 문제 표시
st.subheader(f'문제: {st.session_state.num1} × {st.session_state.num2} = ?')

# 시각화 함수
def draw_grid(num1, num2, image_type):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 격자 그리기
    for i in range(num1):
        for j in range(num2):
            if image_type == '사과':
                ax.text(j + 0.5, i + 0.5, '🍎', fontsize=30, ha='center', va='center')
            elif image_type == '바나나':
                ax.text(j + 0.5, i + 0.5, '🍌', fontsize=30, ha='center', va='center')
            else:  # 배
                ax.text(j + 0.5, i + 0.5, '🍐', fontsize=30, ha='center', va='center')
    
    ax.set_xlim(0, num2)
    ax.set_ylim(0, num1)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.axis('off')
    
    return fig

# 그림 표시
fig = draw_grid(st.session_state.num1, st.session_state.num2, st.session_state.image_option)
st.pyplot(fig)

# 답 입력 섹션
st.divider()
st.subheader('답을 맞혀보세요!')
user_answer = st.number_input('계산 결과를 입력하세요:', min_value=0, max_value=100, key='answer_input')

# 버튼 레이아웃
col1, col2 = st.columns(2)

with col1:
    if st.button('✓ 정답 확인'):
        if user_answer == result:
            st.success(f'🎉 정답입니다! {st.session_state.num1} × {st.session_state.num2} = {result}')
        else:
            st.error(f'❌ 틀렸습니다. 정답은 {result}입니다.')

with col2:
    if st.button('🔄 초기화'):
        st.session_state.num1 = 1
        st.session_state.num2 = 1
        st.session_state.image_option = '사과'
        st.rerun()
