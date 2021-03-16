import os

correspondance = {
    ".arc": "track.arc",
    ".json": "minimap.json",
    ".ght": "staffghost.ght",
}

for root, directory, files in os.walk("./"):
    for name in files:
        _, ext = os.path.splitext(name)
        size = os.path.getsize(name)

        if ext in correspondance:
            os.rename(name, correspondance[ext])
        else:
            raise ValueError(f"extension : {ext} doesn't have correspondance")