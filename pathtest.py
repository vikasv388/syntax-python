
from pathlib import Path

BASE_DIR = Path("uploads")


def read_uploaded_file(filename):
    file_path = BASE_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    filename = input("Enter filename: ")
    print(read_uploaded_file(filename))
