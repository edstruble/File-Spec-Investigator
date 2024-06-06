import numpy as np
from PIL import Image
import streamlit as st


def investigate_file(uploaded_file):
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        st.write("File Type: PDF")
    else:
        img = Image.open(uploaded_file)
        img_data = np.array(img)
        mode = img.mode
        info = img.info
        width = img.width / 300
        height = img.height / 300
        file_res = info.get('dpi')
        x_resolution = info["photoshop"][1005]["XResolution"]
        y_resolution = info["photoshop"][1005]["YResolution"]
        # photoshop_res = photoshop_info[1]["Xresolutoin"]
        st.write("Width:", str(width))
        st.write("Height:", str(height))
        st.write("File Res", file_res)
        st.write("X Resolution", int(x_resolution))
        st.write("Y Resolution", int(x_resolution))
        # st.write(info)
        st.write("File mode:", mode)





    st.write("File Type:", file_type)



def main():
    st.title("Image Percentage Calculator")
    uploaded_file = st.file_uploader("Upload a File...")
    if uploaded_file is not None:
        investigate_file(uploaded_file)
        st.divider()
        # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.divider()


if __name__ == "__main__":
    main()




