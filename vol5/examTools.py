import numpy as np
from PIL import Image

def Projection_H(img, height, width):
    array_H = np.zeros(height)
    for i in range(height):
        total_count = 0
        for j in range(width):
            temp_pixVal = img[i, j]
            if (temp_pixVal == 0):
                total_count += 1
        array_H[i] = total_count

    return array_H


def Projection_V(img, height, width):
    array_V = np.zeros(width)
    for i in range(width):
        total_count = 0
        for j in range(height):
            temp_pixVal = img[j, i]
            if (temp_pixVal == 0):
                total_count += 1
        array_V[i] = total_count

    return array_V


def Detect_HeightPosition(H_THRESH, height, array_H):
    
    lower_posi = 0
    upper_posi = 0

    for i in range(height):
        val = array_H[i]
        if (val > H_THRESH):
            lower_posi = i
            break

    for i in reversed(range(height)):
        val = array_H[i]
        if (val > H_THRESH):
            upper_posi = i
            break

    return lower_posi, upper_posi


def Detect_WidthPosition(W_THRESH, width, array_V):
    char_List = np.array([])

    flg = False
    posi1 = 0
    posi2 = 0
    for i in range(width):
        val = array_V[i]
        if (flg==False and val > W_THRESH):
            flg = True
            posi1 = i

        if (flg == True and val < W_THRESH):
            flg = False
            posi2 = i
            char_List = np.append(char_List, posi1)
            char_List = np.append(char_List, posi2)

    return char_List

### RGB
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result