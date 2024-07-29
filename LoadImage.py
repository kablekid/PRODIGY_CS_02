import cv2 as cv
import numpy


def start(FILEPATH):
    image = cv.imread(FILEPATH)
    return image


if __name__ == "__main__":
    start('14.jpg')
    numpy.array(start('14.jpg'))
    



    