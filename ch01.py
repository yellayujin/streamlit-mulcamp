# -*- coding:utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("This is a title!")
    st.header("This is a header!")
    st.subheader("subheader")  # 문법 에러 디버깅 쉬움(페이지에서 알려줌)
    st.write("Hello! :smile: ")    # 파이썬의 문법 사용 가능("-"*3 하면 - 3번 나옴) print와 유사

    a=1
    b=2
    st.write(a+b)

    st.markdown("This is a markdown.")
    st.markdown("""
    # PART 1. 
    - 색상 테스트: ~~~
    """)

    st.markdown("""
    ## CHAPTER 1. 수식
    - 피타고라스 정리 : :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
    """)

    st.markdown("HTML CSS 마크다운 적용")
    html_css = """
    <style>
        table.customTable {
        width: 100%;
        background-color: #FFFFFF;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #7ea8f8;
        border-style: solid;
        color: #000000;
        }
    </style>
    <table class="customTable">
      <thead>
        <tr>
          <th>이름</th>
          <th>나이</th>
          <th>직업</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Evan</td>
          <td>25</td>
          <td>데이터 분석가</td>
        </tr>
        <tr>
          <td>Sara</td>
          <td>25</td>
          <td>프로덕트 오너</td>
        </tr>
      </tbody>
    </table>
    """

    st.markdown(html_css, unsafe_allow_html=True)


    st.markdown("HTML JS Streamlit 적용")
    js_code = """ 
    <h3>Hi</h3>
    <script>
    function sayHello() {
        alert('Hello from JavaScript in Streamlit Web');
    }
    </script>
    <button onclick="sayHello()">Click me</button>
    """
    components.html(js_code)

if __name__ == "__main__":
    main()