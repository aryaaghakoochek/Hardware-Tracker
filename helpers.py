import time
import psutil
import streamlit as st
import platform
import cpuinfo


def visualized_usage(cpu, mem, bars=50):
    #while True:
    cpuPercent = (cpu / 100.0)
    cpuBar = '╹' * int(cpuPercent * bars) + '⁃' * (bars - int(cpuPercent * bars))

    st.write(f"\rCPU USAGE: |{cpuBar}| {cpu:.2f}%  ", end="")

    memPercent = (mem / 100.0)
    memBar = '╹' * int(memPercent * bars) + '⁃' * (bars - int(memPercent * bars))

    st.write(f"\rMEM USAGE: |{memBar}| {mem:.2f}%  ", end="\r")

        #time.sleep(3)

def bandwidth():
    lastReceived = psutil.net_io_counters().bytes_recv
    lastSent = psutil.net_io_counters().bytes_sent
    lastTotal = lastReceived + lastSent

    while True:
        bytesReceived = psutil.net_io_counters().bytes_recv
        bytesSent = psutil.net_io_counters().bytes_sent
        bytesTotal = bytesReceived + bytesSent

        newReceived = bytesReceived - lastReceived
        newSent = bytesSent - lastSent
        newTotal = bytesTotal - lastTotal

        mbNewReceived = newReceived / 1024 / 1024
        mbNewSent = newSent / 1024 / 1024
        mbNewTotal = newTotal / 1024 / 1024

        st.write(f"{mbNewReceived:.2f} MB RECEIVED, {mbNewSent:.2f} MB SENT, {mbNewTotal:.2f} MB TOTAL")

        lastReceived = bytesReceived
        lastSent = bytesSent
        lastTotal = bytesTotal

        time.sleep(1)

def architecture():
    cpuInfo = cpuinfo.get_cpu_info()

    st.write(f"Architecture: {platform.architecture()}")
    st.write(f"Network Name: {platform.node()}")
    st.write(f"Operating System: {platform.platform()}")
    st.write(f"CPU Details: {cpuInfo['brand_raw']}")
    st.write(f"Actual Frequency: {cpuInfo['hz_actual_friendly']}")
    st.write(f"Advertised Frequency: {cpuInfo['hz_advertised_friendly']}")
    st.write(f"Total RAM: {psutil.virtual_memory().total /1024 /1024 /1024} GB")
