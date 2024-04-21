import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()
        self.current_row_index = 0

    def __initialize_photos(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, count: int):
        pages = math.ceil(count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
        try:
            self.photos[self.current_row_index].append(label)

            return f"{label} photo added successfully on" \
                   f" page {self.current_row_index + 1}" \
                   f" slot {len(self.photos[self.current_row_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        result = '-'*11 + "\n"
        for page in self.photos:
            result += ' '.join(["[]" for picture in page]) + "\n"
            result += '-'*11 + "\n"

        return result