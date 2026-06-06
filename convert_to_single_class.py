from pathlib import Path

datasets = [
    "datasets/Aerial Garbage detection.yolov8",
    "datasets/Garbage detection.yolov8"
]

for dataset in datasets:
    for split in ["train", "valid", "test"]:
        label_dir = Path(dataset) / split / "labels"

        if not label_dir.exists():
            continue

        for txt_file in label_dir.glob("*.txt"):
            lines = []

            with open(txt_file, "r") as f:
                for line in f:
                    parts = line.strip().split()

                    if len(parts) >= 5:
                        parts[0] = "0"
                        lines.append(" ".join(parts))

            with open(txt_file, "w") as f:
                f.write("\n".join(lines))

print("All classes converted to garbage class (0)")