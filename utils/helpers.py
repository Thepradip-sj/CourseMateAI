import re

import hashlib


def create_collection_name(course_name):

    name = course_name.lower()

    name = re.sub(

        r"[^a-z0-9_-]",

        "_",

        name

    )

    name = name.strip("_-")

    name = name[:40]

    if len(name) < 3:

        name = "course_" + name

    return name


def get_file_hash(file_bytes):

    return hashlib.sha256(

        file_bytes

    ).hexdigest()


def safe_filename(filename):

    filename = re.sub(

        r"[^a-zA-Z0-9_.-]",

        "_",

        filename

    )

    return filename