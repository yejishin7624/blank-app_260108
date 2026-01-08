import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 앱 제목
st.title('초등학교 곱셈 학습용 웹 애플리케이션')

# 사용자 입력
num1 = st.number_input('첫 번째 숫자를 입력하세요:', min_value=1, max_value=10)
num2 = st.number_input('두 번째 숫자를 입력하세요:', min_value=1, max_value=10)

# 그림 선택
image_option = st.selectbox('어떤 그림으로 시각화할까요?', ['사과', '바나나', '배'])

# 곱셈 결과 시각화
result = num1 * num2
st.write(f'{num1} x {num2} = {result}')

# 선택한 그림에 따라 시각화
if image_option == '사과':
    img = np.random.rand(10, 10, 3)  # 예시 이미지
    plt.imshow(img)
    plt.title('사과 이미지')
    plt.axis('off')
    st.pyplot()
elif image_option == '바나나':
    img = np.random.rand(10, 10, 3)  # 예시 이미지
    plt.imshow(img)
    plt.title('바나나 이미지')
    plt.axis('off')
    st.pyplot()
else:
    img = np.random.rand(10, 10, 3)  # 예시 이미지
    plt.imshow(img)
    plt.title('배 이미지')
    plt.axis('off')
    st.pyplot()

# 결과값 입력란
user_answer = st.number_input('계산 결과값을 입력하세요:')

# 정답 여부 확인
if st.button('정답 확인'):
    if user_answer == result:
        st.success('정답입니다!')
    else:
        st.error('틀렸습니다. 다시 시도하세요.')

# 초기화 기능
if st.button('초기화'):
    st.experimental_rerun()
