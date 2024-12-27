import os
import cv2
import numpy as np

def extract_word(name: str, itr: int):
    noext_name = name.replace(".png", "").split("/")[0]

    image = cv2.imread(f'media/{name}')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, 157, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (8, 4))  
    dilated = cv2.dilate(binary, kernel, iterations=itr)

    contours, _ = cv2.findContours(
        dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    word_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 30 and h > 10:  
            word_boxes.append((x, y, w, h))

    word_boxes.sort(key=lambda box: (box[1], box[0]))  # (y, x)

    row_threshold = 17 
    rows = []
    current_row = []
    last_y = None

    for box in word_boxes:
        x, y, w, h = box

        if last_y is None or abs(y - last_y) <= row_threshold:
            current_row.append(box)
        else:
            rows.append(current_row)
            current_row = [box]

        last_y = y

    if current_row:
        rows.append(current_row)

    output_dir = f'media/{noext_name}'
    os.makedirs(output_dir, exist_ok=True)
    words = []  

    for row_index, row in enumerate(rows, start=1):
        row.sort(key=lambda box: box[0])

        for word_index, (x, y, w, h) in enumerate(row, start=1):
            word_image = image[y:y + h, x:x + w]
            route = f'{output_dir}/{row_index}_{word_index}.png'
            cv2.imwrite(route, word_image)

            words.append(route)

    words = sorted(words)
    text = []
    for j in range(1, len(rows)+1):
        t = [i for i in words if i.replace(f'{output_dir}/', '')[0] == str(j)]
        text.append(t)
    return text


def extract_letters(image_path, w_index: int):
    image = cv2.imread(image_path)

    folder = image_path.split('/')[1]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

    sure_bg = cv2.dilate(opening, kernel, iterations=1)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.25 * dist_transform.max(), 255, 0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    _, markers = cv2.connectedComponents(sure_fg)

    markers = markers + 1

    markers[unknown == 255] = 0

    markers = cv2.watershed(image, markers)

    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    os.makedirs(f'media/{folder}/letters', exist_ok=True)

    letters = []
    for c_index, contour in enumerate(contours, start=1):
        x, y, w, h = cv2.boundingRect(contour)

        if w >2 and h>2:
            letter = image[y:y+h, x:x+w]
            
            route = f'media/{folder}/letters/letter{c_index}_{w_index}.png'
            cv2.imwrite(route, letter)
            letters.append(route)

    return letters