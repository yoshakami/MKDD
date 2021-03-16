import glob
import os
import os.path

bti = {
    43294: "track_big_logo.bti",
    5216: "track_small_logo.bti",
    23584: "track_image.bti",
    8224: "track_name.bti"
}

ext = {
    ".json": "minimap.json",
    ".ght": "staffghost.ght",
    "L.arc": "track_mp.arc",
    ".arc": "track.arc",
}

# Generic translation
for ext, new_name in ext.items():
    for path in glob.glob(f"**/*{ext}", recursive=True):
        os.rename(path, os.path.join(os.path.dirname(path), new_name))

# Translation of BTI files per size
for path in glob.glob("**/*.bti", recursive=True):
    new_name = bit.get(os.path.getsize(path), "track_name.bti")
    os.rename(path, os.path.join(os.dirname(path), new_name))

# Translation of AST files need to ensure no file is erased
for path in glob.glob("**/*.ast", recursive=True):
    try:
        old_file = os.path.join(os.path.dirname(path), "lap_music_normal.ast")
        new_file = os.path.join(os.path.dirname(path), "lap_music_fast.ast")
        if os.path.getsize(file) < os.path.getsize(path):
            os.rename(old_file, new_file)
    except FileNotFoundError:
        pass
    new_name = "lap_music_normal.ast"
    os.rename(path, os.path.join(os.path.dirname(path), "lap_music_normal.ast"))