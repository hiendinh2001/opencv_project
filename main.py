import cv2

#----------------- Đọc ảnh màu -----------------#
# Đọc ảnh màu
image_color = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)
#image_color = cv2.imread('dog.jpg', 1)

# Hiển thị ảnh màu
cv2.imshow('Dog', image_color)

# Lưu ảnh màu
cv2.imwrite('dog_copy.jpg', image_color)
path = r"C:\Users\hien2\Downloads\github\opencv_project\test\dog_copy.jpg"
cv2.imwrite(path, image_color)

# waitKey(0) sẽ chờ đến khi có phím nào được nhấn
cv2.waitKey(0)
# destroyAllWindows() sẽ đóng tất cả các cửa sổ hiển thị ảnh
cv2.destroyAllWindows()

#----------------- Đọc ảnh xám -----------------#

# Đọc ảnh xám
image_gray = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
#image_gray = cv2.imread('dog.jpg', 0)

# Hiển thị ảnh xám
cv2.imshow('Dog', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------- Đọc ảnh màu với kênh alpha -----------------#

# Đọc ảnh màu với kênh alpha
image_alpha = cv2.imread('dog.jpg', cv2.IMREAD_UNCHANGED)
#image_alpha = cv2.imread('dog.jpg', -1)

# Hiển thị ảnh màu với kênh alpha
cv2.imshow('Dog', image_alpha)
cv2.waitKey(0)
cv2.destroyAllWindows()