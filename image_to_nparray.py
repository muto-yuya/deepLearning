import cv2
import numpy as np
from make_face_extracted import checkFileNum
person_name = "other"

def image_convert(filename):
    file = cv2.imread(filename)
    return file

samples_length = checkFileNum(person_name+"_detected_learning")
image_array=[]
for i in range(0,samples_length-1):
    print(samples_length)
    img = image_convert(person_name+"_detected_learning/"+person_name+"_face"+str(i)+".jpg")
    print(img)
    image_array.append(img)
if __name__ == '__main__':
    np.save(person_name+"_face.npy",image_array)