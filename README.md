# PDF to PNG Converter

A Streamlit application that converts PDF files to PNG images.

## Disclaimer

This app is intended for personal or educational purposes **only**. It is **not recommended** for commercial or professional use. It is **not intended** for handling sensitive data.

### Key Features
 
 - Convert PDF files to PNG images
 - Supports files up to 10MB in size
 - Files are not stored, only buffered for processing
 - Download individual images or all images as a zip file

### How it Works
 
 1. Upload your PDF file
 2. The application will convert the PDF to PNG images
 3. Download the images individually or as a zip file

### Privacy

Your files are not stored on the servers. They are only buffered for processing and deleted after conversion. It respects your privacy and does not collect or store any data.

### Limitations
 
 - Maximum file size: 10MB
 - Only PDF files are supported (at the moment)

### Usage

Simply upload your PDF file and follow the prompts to download your converted images.

### License

The product is licensed under the MIT License

### Credits

 - [zipfile](https://github.com/python/cpython/tree/3.13/Lib/zipfile/)
 - [Streamlit](https://streamlit.io/)
 - [pdf2image](https://github.com/Belval/pdf2image)