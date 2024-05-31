from gptvision import GPTVISION
import streamlit as st
from PIL import Image
import utils
import base64
import os
from dotenv import load_dotenv

st.set_page_config(
    page_title="Product Scheduler",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Product Scheduler👷‍")
st.markdown("## Welcome to the Product Scheduler!")
st.markdown("In this App you need to Upload Nit sketch of your product. This app will gives you Project Planning,Initiation and Schedule Development")

load_dotenv()
api = os.getenv("OPENAI_API_KEY")


openai_4o_model = GPTVISION(api_key=api,parameters={})

data = "data"
os.makedirs(data, exist_ok=True)


def encode_image(image_path):
        with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')


prompt = f"""
You are an Expert Project Manager in Automotive industry.Your Task is to create Project Planning,Initiation and Schedule Development.
Follow Below Instructions:
1/ Analyze given Design and Note all features and parts carefully.
2/ Think About Resource utilise in Manufacturing process.
3/ Make Planning to build this design in realistic model.
4/ Develop Detailed Monthly schedule table with following columns month,Task,week,Description.

Output Requirements:
Detailed Monthly schedule table with following columns month,Task,week,Description.
"""

uploaded_files = st.file_uploader("Upload Nit sketch of product", type=['png', 'jpg'])
if uploaded_files is not None:
        st.success(f"File uploaded: {uploaded_files.name}")
        file_path = utils.save_uploaded_file(uploaded_files)
        if file_path is not None:
            st.sidebar.image(file_path)
            if st.button("Generate"):
                encoded_image = encode_image(file_path)
                planning = openai_4o_model.generate_text(prompt=prompt, image_url=encoded_image)
                st.markdown(planning)



