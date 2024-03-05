import cv2
import numpy as np

img = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)

#rows : số hàng, cols : số cột, ch : số kênh màu
rows, cols = img.shape[0:2] #lấy số hàng và số cột của ảnh, 0 là hàng, 1 là cột, 2 là kênh màu, không có kênh màu thì chỉ lấy 2 số đầu

#Tạo ma trận biến đổi
# Ảnh gốc : input_mt là ma trận tọa độ 3 điểm ảnh góc trên bên trái, góc trên bên phải, góc dưới bên trái
input_mt = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]]) #tọa độ 3 điểm ảnh góc trên bên trái, góc trên bên phải, góc dưới bên trái
# Ảnh đích : output_mt là ma trận tọa độ 3 điểm ảnh góc trên bên trái, góc trên bên phải, góc dưới bên trái
output_mt = np.float32([[0, 0], [cols/2, 0], [cols/2, rows - 1]]) #tọa độ 3 điểm ảnh góc trên bên trái, góc trên bên phải, góc dưới bên trái

#Tạo ma trận biến đổi
M = cv2.getAffineTransform(input_mt, output_mt)
dst = cv2.warpAffine(img, M, (cols, rows))

#Hiển thị ảnh gốc và ảnh biến đổi
final = cv2.hconcat([img, dst])
cv2.imshow('Affine Transformation', final)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tạo ma trận biến đổi 2
output_mt_2 = np.float32([[cols - 1, 0], [0, 0], [cols - 1, rows - 1]])
M_2 = cv2.getAffineTransform(input_mt, output_mt_2)
dst_2 = cv2.warpAffine(img, M_2, (cols, rows))

final_2 = cv2.hconcat([img, dst_2])
cv2.imshow('Affine Transformation', final_2)
cv2.waitKey(0)
cv2.destroyAllWindows()