# -*- coding: utf-8 -*-
import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan", icon="📑"),
    st.Page(page="pages/page2.py", title="Hasil dan Pembahasan", icon="📑"),
    st.Page(page="pages/page3.py", title="Penutup", icon="📑")
    st.Page(page="pages/page4.py", title="Visualisasi Data", icon="📑")
]

pg = st.navigation(
    pages,
    position="sidebar"
)

pg.run()
