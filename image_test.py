import cv2
import numpy as np

file = np.load("other_face.npy")
print(file.shape)
cv2.imshow("test",file[100])
cv2.waitKey(0)
cv2.destroyAllWindows()