import shutil
from pathlib import Path

sources = [
    "datasets/Aerial Garbage detection.yolov8",
    "datasets/Garbage detection.yolov8"
]

target = Path("datasets/Garbage_Final")

for split in ["train", "valid", "test"]:
    (target / split / "images").mkdir(parents=True, exist_ok=True)
    (target / split / "labels").mkdir(parents=True, exist_ok=True)

for source in sources:
    source_name = Path(source).name.replace(" ", "_")

    for split in ["train", "valid", "test"]:
        img_dir = Path(source) / split / "images"
        lbl_dir = Path(source) / split / "labels"

        if not img_dir.exists():
            continue

        for img in img_dir.iterdir():
            new_name = f"{source_name}_{img.name}"
            shutil.copy(img, target / split / "images" / new_name)

        for lbl in lbl_dir.iterdir():
            new_name = f"{source_name}_{lbl.name}"
            shutil.copy(lbl, target / split / "labels" / new_name)

print("Datasets merged successfully!")