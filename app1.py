# -*- coding: utf-8 -*-
# @Time    : 2024/8/10 23:47
# @Author  : Maki Wang
# @FileName: app1.py
# @Software: PyCharm
# !/usr/bin/env python3

import streamlit as st
from utils1 import get_chat_response
from langchain.memory import ConversationBufferMemory

def app():
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image("maki.jpg")
    with col2:
        st.title("MakiGenie")
    st.divider()

    with st.sidebar:
        openai_api_key = st.text_input("Please Enter Your OpenAI API Key：", type="password")
        st.markdown("[Obtain OpenAI API Key](https://platform.openai.com/account/api-keys)")
        st.markdown("---")
        st.markdown('<p style="color:red;">Designed by Xianmu, please contact via <em style="color:blue;">wangxianmu@gmail.com</em></p>', unsafe_allow_html=True)

    if 'memory' not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(return_messages=True)
        st.session_state['messages'] = [{"role":'ai',
                                         "content":'Hello, I am your AI assistant Maki. How can I help you today?'}]

    for message in st.session_state['messages']:
        st.chat_message(message['role']).write(message['content'])

    prompt = st.chat_input()
    if prompt:
        if not openai_api_key:
            st.info("Please enter your OpenAI API Key😄")
            st.stop()
        st.session_state['messages'].append({'role':'human','content':prompt})
        st.chat_message('human').write(prompt)

        with st.spinner('Maki is thinking, please wait...'):
            response = get_chat_response(prompt, st.session_state.memory, openai_api_key)
        st.session_state['messages'].append({"role":"ai", "content":response})
        st.chat_message("ai").write(response)

