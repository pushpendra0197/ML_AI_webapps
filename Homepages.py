
import streamlit as st
import base64
import joblib
st.set_page_config(
    page_title="Machinelearning_And_Deeplearning_Models",
    page_icon=r"Icon.png",
)
st.sidebar.success("select a page above")
path=(r"back.png")
with open(path,"rb") as file:
    image_back=base64.b64encode(file.read()).decode()
page_element=f"""
<style>
[data-testid="stAppViewContainer"]
{{
background-image:url("data:image;base64,{image_back}");
background-size=10px 10px;
background-repeat=no-repeat;
background-position=center;
}}
<style>
"""
st.markdown(page_element,unsafe_allow_html=True)
