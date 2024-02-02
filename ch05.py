# -*- coding:utf-8 -*-
# widget(버튼) input widgets 문서 참고
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

@st.cache_data
def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales

    return revenue

# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df

def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)
    
def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)
def plot_plotly(df):
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = df['sepal_length'],
                   y = df['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)

def main():
    st.title("Button Widget")
    price = st.slider("단가:", 100, 10000, value=5000)
    total_sales = st.slider("전체 판매 갯수:", 1, 1000, value=500)

    st.write(price, total_sales)

    if st.button("매출액 계산"):
        revenue = cal_sales_revenue(price, total_sales)
        st.write(revenue)

    st.title("Check Box Control")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox('시각화 보여주기')   # checkbox에서 체크되면 True, 아니면 False됨
    # st.write(show_plot)

    fig, ax = plt.subplots()
    ax.plot(x, y)

# 솔루션(태블로, power bi) 사용시 데이터 크기가 1기가 넘어가면 시스템 뻗음
# 전처리나 머신러닝 등에서도 마찬가지.
# 프로젝트 목적에 따라 솔루션(단순 결과 보여줌-태블로 쉬움)과 오픈소스(예측 모델링 해서 보여줌-태블로로는 힘듬) 선택  => TabPy도 있어유
    if show_plot:  # 체크박스가 클릭되면 시각화 보여줌(이런거 (세부적인 컨트롤) 태블로로는 어려움)
        st.pyplot(fig)
    
    else:
        st.write("Fine, ")


    st.title('라이브러리 선택')
    iris = load_data()
    st.data_editor(iris)  # 권장 / 내일 오후에도 적용 및 공부하기

    plot_type = st.radio(
        "어떤 스타일의 산점도를 보고 싶은가요?",
        ("Matplotlib", "Seaborn", "Plotly")
    )

    st.write(plot_type)

    # 조건문 사용해서 3개 메서드 radio마다 해당 시각화 메서드 호출되게(위 함수 이용)
    if plot_type == 'Matplotlib':
        plot_matplotlib(iris)

    elif plot_type == 'Seaborn':
        plot_seaborn(iris)

    elif plot_type == 'Plotly':
        plot_plotly(iris)

    else:
        st.write("Error!")

    
    st.title("SelectBox 사용")
    
    # 행 추출
    val = st.selectbox("1개의 종을 선택하십숑", iris.species.unique())
    st.write("Chosen one:", val)

    result = iris.loc[iris['species'] == val, :].reset_index(drop=True)
    st.data_editor(result)

    cols = st.multiselect("복수의 컬럼을 선택하세용", iris.columns)
    st.dataframe(iris.loc[:,cols])


if __name__ == "__main__":
    main()