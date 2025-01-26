import streamlit as st
import func.load_image as load_image
import func.generate_zip as generate_zip


st.set_page_config(
    page_title="PDF to Image Converter",
    page_icon="static/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title('PDF to Image Converter')

row = st.columns(2)

pdf_files = st.sidebar.file_uploader('Upload a PDF file', label_visibility='hidden', type=["pdf"], accept_multiple_files=True, )

if not pdf_files and len(pdf_files) == 0:
    st.sidebar.warning("Upload a PDF file to start")

if pdf_files is not None and len(pdf_files) > 0:
    images = load_image.load_image(pdf_files)

    if len(images) > 1:

        st.sidebar.download_button(
            label="Download all images",
            data=generate_zip.generate_zip(images),
            file_name="images.zip",
            mime="application/zip"
        )

    for image in images:
        with st.container():
            sx, dx = st.columns(2, gap="medium", vertical_alignment="center")

            with sx:
                st.image(image.image, use_container_width=True)

            with dx:
                st.header(f"{image.name}, Page: {image.page}")

                st.download_button(
                    label="Download",
                    data=image.image,
                    file_name=f"{image.name}_page{image.page}.png",
                    mime="image/png"
                )
