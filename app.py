# -*- coding: utf-8 -*-
# @Time    : 2024/11/29 21:17
# @Author  : Maki Wang
# @FileName: app.py
# @Software: PyCharm
# !/usr/bin/env python3

import app1
import app2
import app3
import streamlit as st

PAGES = {"Chatbot": app1,"CSV-Analyzer": app2,"Script-Generator": app3}
st.sidebar.title('LLM Project Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
