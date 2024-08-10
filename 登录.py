import streamlit as st
import time
st.title('登录网站')
st.header('这是一个飞友们的网站')
st.subheader("你是飞友吗？")
my_open = st.toggle('是')
my_open1 = st.toggle('不是')
if my_open:
    if st.button('登录'):
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载网站页面'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        st.link_button('进入网站', 'https://flycyd-6fvrpcckbxqjvjzfxmghan.streamlit.app/')
if my_open1:
    st.write('看来这个网站不适合你哟，去别的网站看看吧！')





