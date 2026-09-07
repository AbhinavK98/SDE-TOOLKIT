"""Proxy Pattern - Bad Example

This file shows the bad example implementation in the Proxy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

import time


class HighResImage:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__image_data = None

        self._load_from_disk()

    def _load_from_disk(self):
        time.sleep(1)
        self.__image_data = f"[[Loaded image data of {self.__file_name}]]"
        print(f"Loaded {self.__file_name} from disk")

    def display(self):
        print(f"{self.__file_name} has image data of {self.__image_data}\n")


class PhotoGallery:
    def __init__(self):
        self.__images: list[HighResImage] = []

    def add_image(self, file_name: str):
        high_res_image = HighResImage(file_name)
        self.__images.append(high_res_image)

    def display_gallery(self):
        for image in self.__images:
            image.display()


photo_gallery = PhotoGallery()
photo_gallery.add_image("image1.png")
photo_gallery.add_image("image2.png")
photo_gallery.add_image("image3.png")
photo_gallery.add_image("image4.png")

# photo_gallery.display_gallery()

# Revision summary:
# - Part of the Proxy Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
