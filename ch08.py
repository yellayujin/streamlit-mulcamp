# -*- coding:utf-8 -*-
# 레이아웃과 시각화

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Hello")

    with st.sidebar:
        st.header("Sidebar")
        day = st.selectbox("Select a day", ["Thur", "Fri", "Sat", "Sun"])

    tips = sns.load_dataset("tips")
    filtered_tips = tips[tips["day"] == day]
    top_bill = filtered_tips["total_bill"].max()
    top_tip = filtered_tips["tip"].max()


    tab1, tab2, tab3 = st.tabs(['Total Bill', 'Tip', 'Size'])
    with tab1: #total bill
        fig, ax = plt.subplots()
        st.header("Total Bill Amounts")
        sns.histplot(filtered_tips["total_bill"], kde=False, ax=ax)
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots()
        st.header("Tip Amounts")
        sns.histplot(filtered_tips["tip"], kde=False, ax=ax)
        st.pyplot(fig)

    with tab3:
        fig, ax = plt.subplots()
        st.header("Table Sizes")
        sns.boxplot(data=filtered_tips, x="sex", y="tip", ax=ax)
        st.pyplot(fig)

    
    col1, col2, col3 = st.columns([1, 1, 1]) # 각 숫자는 크기 비율, 2개정도만 만들기를 권장, 각 컬럼 안에 시각화차트 넣는 것 비추(UI 안 예쁨)
                                             # 그냥 metric정도만 컬럼 쓰는 것 추천(시각화차트는 안 예뻐)
    with col1:
        st.metric("Top Bill", f"${top_bill:.2f}")

    with col2:
        st.metric("Top Tip", f"${top_tip:.2f}")

    with col3:
        st.write("col3")

if __name__ == "__main__":
    main()
