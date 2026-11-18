import os
import random
import numpy as np
import zipfile

from PIL import Image, ImageDraw, ImageFont

# ==================================
# CONFIGURATION
# ==================================

SIZE = 128
OUTPUT_SIZE = 32
BASE_DIR = "/content/dataset"

CLASSES = ["stop", "no_entry", "give_way", "turn_left"]

SPLITS = {
    "train": 800,
    "validation": 100,
    "test": 100
}

random.seed(42)
np.random.seed(42)

# ==================================
# DRAW TRAFFIC SIGNS
# ==================================

def create_sign(label):

    bg = random.choice([
        (225, 225, 225),
        (240, 240, 230),
        (210, 220, 225),
        (245, 245, 245)
    ])

    img = Image.new("RGB", (SIZE, SIZE), bg)
    draw = ImageDraw.Draw(img)

    # Random sign position and size
    sign_size = random.randint(78, 96)
    x = (SIZE - sign_size) // 2 + random.randint(-5, 5)
    y = (SIZE - sign_size) // 2 + random.randint(-5, 5)

    if label == "stop":

        points = [
            (x + sign_size * 0.30, y),
            (x + sign_size * 0.70, y),
            (x + sign_size, y + sign_size * 0.30),
            (x + sign_size, y + sign_size * 0.70),
            (x + sign_size * 0.70, y + sign_size),
            (x + sign_size * 0.30, y + sign_size),
            (x, y + sign_size * 0.70),
            (x, y + sign_size * 0.30)
        ]

        draw.polygon(points, fill=(210, 25, 35))
        draw.line(points + [points[0]], fill="white", width=5)

        font = ImageFont.load_default()
        draw.text(
            (SIZE // 2, SIZE // 2),
            "STOP",
            fill="white",
            font=font,
            anchor="mm"
        )

    elif label == "no_entry":

        draw.ellipse(
            (x, y, x + sign_size, y + sign_size),
            fill=(220, 20, 30),
            outline="white",
            width=4
        )

        draw.rectangle(
            (x + 10, y + sign_size * 0.42,
             x + sign_size - 10, y + sign_size * 0.58),
            fill="white"
        )

    elif label == "give_way":

        points = [
            (x, y),
            (x + sign_size, y),
            (x + sign_size // 2, y + sign_size)
        ]

        draw.polygon(
            points,
            fill="white",
            outline=(220, 20, 30)
        )

        draw.line(
            points + [points[0]],
            fill=(220, 20, 30),
            width=7
        )

    elif label == "turn_left":

        draw.ellipse(
            (x, y, x + sign_size, y + sign_size),
            fill=(20, 75, 190),
            outline="white",
            width=3
        )

        # Left arrow
        arrow = [
            (x + 17, y + 38),
            (x + 42, y + 17),
            (x + 42, y + 30),
            (x + 72, y + 30),
            (x + 72, y + 49),
            (x + 42, y + 49),
            (x + 42, y + 64)
        ]

        draw.polygon(arrow, fill="white")

    # Small rotation variation
    angle = random.uniform(-8, 8)
    img = img.rotate(
        angle,
        resample=Image.Resampling.BICUBIC,
        fillcolor=bg
    )

    # Resize to 32 x 32
    img = img.resize(
        (OUTPUT_SIZE, OUTPUT_SIZE),
        Image.Resampling.LANCZOS
    )

    return img

# ==================================
# GENERATE DATASET
# ==================================

for split, amount in SPLITS.items():

    for label in CLASSES:

        folder = os.path.join(BASE_DIR, split, label)
        os.makedirs(folder, exist_ok=True)

        for i in range(amount):

            img = create_sign(label)

            filename = f"{label}_{i:04d}.bmp"

            img.save(
                os.path.join(folder, filename),
                format="BMP"
            )

        print(f"{split}/{label}: {amount} images created")

print("\nDATASET GENERATION COMPLETE!")

# ==================================
# ZIP DATASET
# ==================================

zip_path = "/content/traffic_sign_dataset.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:

    for root, dirs, files in os.walk(BASE_DIR):

        for file in files:

            path = os.path.join(root, file)

            z.write(
                path,
                os.path.relpath(path, "/content")
            )

print("ZIP FILE CREATED:", zip_path)
