import os
from PIL import Image
from datetime import datetime
def text_to_braille_image(text):
    # 모델 코드 구현
    braille_translation = ""
    for char in text:
        if char.isalpha():
            braille_char = char.lower() + ".jpg"
            braille_translation += braille_char + " "
        elif char == ' ':
            braille_translation += "space.jpg "

    braille_image_names = braille_translation.strip().split()
    braille_images = []
    for braille_image_name in braille_image_names:
        image_path = os.path.join("Team5_web/static/img/data/", braille_image_name)
        image = Image.open(image_path)
        braille_images.append(image)

    # 이미지 연결하여 하나의 이미지로 만들기
    concatenated_width = sum(img.width for img in braille_images)
    max_height = max(img.height for img in braille_images)
    concatenated_image = Image.new('RGB', (concatenated_width, max_height))

    x_offset = 0
    for img in braille_images:
        concatenated_image.paste(img, (x_offset, 0))
        x_offset += img.width
        # 이미지 저장
        concatenated_image.save(f"Team5_web/static/created_braille/braille_image{datetime.now()}.jpg")

    return concatenated_image



