import face_recognition

from PIL import Image, ImageDraw


# 画像の読み込み
image = face_recognition.load_image_file("1.jpg")

#画像から顔検出
face_locations = face_recognition.face_locations(image)

pil_image = Image(image)
draw = ImageDraw.Draw(pil_image)

# 検出した顔分ループする
for (top, right, bottom, left) in face_locations:
    #　顔の周りを四角で囲う
    draw(((left, top), (right, bottom)), outline=(255, 0, 0), width=2)
    
del draw

# 画像を表示
pil_image.show()
