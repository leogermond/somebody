import argparse
import random
import face_recognition.api as face_recognition
from PIL import Image, ImageDraw
import numpy as np

def anonymize_faces(img):
    faces = face_recognition.face_locations(img)
    im = Image.fromarray(img)
    draw = ImageDraw.Draw(im)

    if len(faces) == 1:
        show = -1
    else:
        show = int(random.uniform(0, len(faces)))

    for i, f in enumerate(faces):
        if i == show:
            continue
        fx = (f[3], f[1] + 1)
        fy = (f[0], f[2] + 1)
        fy = fy[0] - (fy[1] - fy[0]) // 4, fy[1]

        strike_sz = (fy[1] - fy[0]) // 3
        for oy in range(0, 3 * strike_sz, strike_sz):
            rx, ry = int(random.uniform(-15, 15)), int(random.uniform(-7, 7))
            draw.polygon(
                [(fx[0] + rx, fy[0] + oy),
                 (fx[0], fy[0] + oy + strike_sz),
                 (fx[1], fy[0] + oy + strike_sz + ry),
                 (fx[1] + rx, fy[0] + oy + ry)], fill = 0)
    return np.array(im)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('image')
    args = ap.parse_args()
    img = face_recognition.load_image_file(args.image)
    im = Image.fromarray(anonymize_faces(img))
    im.save('out.jpg')

if __name__  == "__main__":
    main()
