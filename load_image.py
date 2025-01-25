from os import remove
from io import BytesIO
from pdf2image import convert_from_path


class Image:
    def __init__(self, name, page, image):
        """
        Parameters
        ----------
        name : str
            The name of the image without the extension.
        page : int
            The page number of the image.
        image : str
            The path to the image.
        """

        self.name = name
        self.page = page
        self.image = image


def load_image(pdf_files):
    """
    Parameters
    ----------
    pdf_files : list
        A list of PDF files to be converted into images.

    Returns
    -------
    list
        A list of Image objects, containing the name, page number, and image path of each image generated from the PDFs.
    """

    images_list = []

    for pdf_file in pdf_files:
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.getbuffer())

        images = convert_from_path("temp.pdf")

        for i, image in enumerate(images):
            buffer = BytesIO()

            image.save(buffer, format="PNG")

            image_bytes = buffer.getvalue()

            image = Image(pdf_file.name[:-4], i + 1, image_bytes)

            images_list.append(image)

        remove("temp.pdf")

    return images_list
