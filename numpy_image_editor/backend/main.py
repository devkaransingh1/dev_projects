import cv2
krishna=cv2.imread(r"D:\krishnamovies\test.jpg")

cv2.imshow("test image by dev",krishna)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("image shape = ",krishna.shape)
print("image dtype = ",krishna.dtype)



















    