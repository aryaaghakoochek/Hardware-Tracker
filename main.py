import psutil
import streamlit as st
import helpers

cpuCol, bandWCol, CompInfo = st.columns(3)

with cpuCol:
    if st.button('Test CPU Percentage'):
        helpers.visualized_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)

with bandWCol:
    if st.button('Test Bandwidth'):
        helpers.bandwidth()

with CompInfo:
    if st.button('Computer Information'):
        helpers.architecture()
