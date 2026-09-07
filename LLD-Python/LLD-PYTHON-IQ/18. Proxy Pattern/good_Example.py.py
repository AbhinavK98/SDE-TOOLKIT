"""Proxy Pattern - Good Example.Py

This file shows the Good Example.Py example in the Proxy Pattern section.
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


class ImageProxy:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__real_image = None

    def display(self):
        if self.__real_image is None:
            self.__real_image = HighResImage(self.__file_name)
        self.__real_image.display()


class PhotoGallery:
    def __init__(self):
        self.__images: list[ImageProxy] = []

    def add_image(self, file_name: str):
        image_proxy = ImageProxy(file_name)
        self.__images.append(image_proxy)

    def display_gallery(self):
        for image in self.__images:
            image.display()

    def show_image(self, index: int):
        self.__images[index - 1].display()


start_time = time.time()
photo_gallery = PhotoGallery()
photo_gallery.add_image("image1.png")
photo_gallery.add_image("image2.png")
photo_gallery.add_image("image3.png")
photo_gallery.add_image("image4.png")
end_time = time.time()
print(f"{end_time - start_time:.1f}")

photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
print("----------")
photo_gallery.show_image(2)
print("----------")

# Revision summary:
# - Part of the Proxy Pattern examples.
# - Shows the Good Example.Py example.
# - Use this file to review the pattern and understand its purpose.
