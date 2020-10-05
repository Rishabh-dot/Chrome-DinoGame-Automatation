import pyautogui
import time
from PIL import Image, ImageGrab
# from numpy import asarray

def hit(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(455, 515):
        for j in range(233, 263):
            if data[i, j] == 83:
                return True
            elif 84 <= data[i, j] <= 225:
                        return True
                
                
    return False

# def downCollide(data):
#     for i in range(460, 515):
#         for j in range(210, 237):
#             if data[i, j] < 83:
#                 return True
#     return False

if __name__ == "__main__":
    print("Hey... Dino game is about to start in 3 seconds!")
    time.sleep(3)
    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        # if downCollide(data):
        #     hit("down")
        # print(asarray(image))

        # Draw the rectangle
        # for i in range(460, 515):
        #     for j in range(210, 237):
        #         data[i, j] = 200
        # for i in range(455, 515):
        #     for j in range(233, 263):
        #         data[i, j] = 0
    
        # image.show()

        # break