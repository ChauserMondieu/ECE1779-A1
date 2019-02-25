import cv2 as cv


def it_function(photo_address, photo_thumbnail_address):
    img = cv.imread(photo_address)
    img = cv.resize(img, (192, 108), interpolation=cv.INTER_CUBIC)
    cv.imwrite(photo_thumbnail_address, img)
