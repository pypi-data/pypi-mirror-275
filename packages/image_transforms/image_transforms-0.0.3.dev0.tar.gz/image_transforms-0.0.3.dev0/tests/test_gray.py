import pytest
from PIL import Image
from pathlib import Path
import imgtfs


@pytest.mark.parametrize(
    "transform",
    [x for x in dir(imgtfs.gray) if x.startswith("Gray")],
)
def test(transform: str):
    img_path: str = "images/lena.jpg"
    image = Image.open(img_path)
    image = getattr(imgtfs.gray, transform)()(image)
    Path("outputs").mkdir(parents=True, exist_ok=True)
    image.save(f"output/lena_{transform}.jpg")
