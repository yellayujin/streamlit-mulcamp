# -*- coding:utf-8 -*-
# sidebar, with

import streamlit as st
import matplotlib.pyplot as plt

def main():
    value1 = st.slider('Choose', 0, 100)
    st.write(value1)

    value2 = st.sidebar.slider('Choose2', 0, 100)    # sidebar.쓰면 사이드 공간에 들어감
    st.sidebar.write(value2)                         # 마찬가지

    with st.sidebar:
        value3 = st.slider('Choose3', 0, 100)
        st.write(value3)

        st.markdown("Matplotlib")
        fig, ax = plt.subplots()   # sidebar안에 들어감
        ax.plot([1, 2, 3])
        st.pyplot(fig)

    st.markdown("Matplotlib2")  # 메인공간에 들어감
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    st.pyplot(fig)

if __name__ == "__main__":
    main()