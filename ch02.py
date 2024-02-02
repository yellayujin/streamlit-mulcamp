# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data   # 캐싱 메모리를 잡음, 자료마다 캐싱 데이터 쓰거나 리소스 쓰거나 여부가 갈림. 이 줄은 decorator로 함수의 중급 레벨 사용법
def load_data():
    # df = sns.load_dataset('iris')
    df = sns.load_dataset('tips')
    return df

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)

    tips = load_data()
    st.dataframe(tips, use_container_width=True)

    st.write("-" *10)
    st.title("st.metric()")

    tip_max = tips['tip'].max()
    tip_min = tips['tip'].min()

    st.write(tip_max, tip_min)

    st.metric(label = '최대', value=tip_max, delta = tip_max - tip_min)
    st.metric(label = '최소', value=tip_min, delta = tip_min - tip_max)



if __name__ == "__main__":
    main()                  # streamlit run ch02.py