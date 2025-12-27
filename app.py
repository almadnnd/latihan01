# -*- coding: utf-8 -*-
import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan"),
    st.Page(page="pages/page2.py", title="Hasil dan Pembahasan"),
    st.Page(page="pages/page3.py", title="Penutup"),
    st.Page(page="pages/page4.py", title="Visualisasi Data"),
]

pg = st.navigation(
    pages,
    position="sidebar"
)

pg.run()
