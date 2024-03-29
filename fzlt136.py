import cv2

img = cv2.imread('image.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)


def dodge(x, y):
    return cv2.divide(x, 255-y, scale=256)


final_img = dodge(img_gray, img_smoothing)

cv2.imwrite('img.jpg', final_img)
