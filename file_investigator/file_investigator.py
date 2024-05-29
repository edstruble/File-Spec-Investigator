import numpy as np
from PIL import Image
import streamlit as st


def investigate_file(uploaded_file):
    if uploaded_file == pdf
        do stuff
    else
        img = Image.open(uploaded_file)
        img_data = np.array(img)

        file_size_px = img_data.size
        file_size_inch = file_size_px

        st.write("File Dimensions:", file_size_inch)



def main():
    st.title("Image Percentage Calculator")
    uploaded_file = st.file_uploader("Upload a File...")
    if uploaded_file is not None:
        investigate_file(uploaded_file)
        st.divider()
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.divider()


if __name__ == "__main__":
    main()