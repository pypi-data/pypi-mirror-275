import hashlib
import os
import pathlib

import file

IMG_TYPE = ["jpg", "jpeg", "png"]


# def list_file(f_path: str, f_ext: list[str]) -> list[str]:
#     files(f_path, f_ext)


def files(f_path: str, f_ext: list[str]) -> list[str]:
    return file.files(f_path, f_ext)


# def list_path(f_path: str, f_ext: list[str]) -> list[str]:
#     file_paths(f_path, f_ext)


def file_paths(f_path: str, f_ext: list[str]) -> list[str]:
    return file.file_paths(f_path, f_ext)


# def list_imgs(f_path: str, f_ext: list[str]) -> list[str]:
#     imgs(f_path, f_ext)


def imgs(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return file.imgs(f_path, f_ext)


def img_paths(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return file.file_paths(f_path, f_ext)


# def i_paths(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
#     if not os.path.exists(f_path):
#         return []
#     return list_path(f_path, f_ext)


def file_hash(file_path: str, hash_type: str) -> str:
    return file.file_hash(file_path, hash_type)
