import zipfile

from io import BytesIO


def generate_zip(images):
    """
    Generate a zip file of images.

    :param images: A list of `Image` objects
    :return: The bytes of the zip file
    """

    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, False) as zip_file:
        for image in images:
            zip_file.writestr(f"{image.name}_page{image.page}.png", image.image)

    return zip_buffer.getvalue()
