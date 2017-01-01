import face_detecter2
import os

person_name = "aragaki"

def checkFileNum(path):
    sep = "/"
    ch = os.listdir( path )
    counter = 0
    for c in ch:
        if os.path.isdir( path+c ):
            checkFileNum( path+c+sep )
        else:
            counter += 1
    return counter
def face_extract(person_name,first_num):
    error_num = 0
    print("file number:",checkFileNum(person_name)-1)
    for i in range(first_num,checkFileNum(person_name)-1):
        face_detecter2.detect_face_rotate(person_name+"/"+person_name+str(i)+".jpg",'.',person_name+'_detected')
        error_num += 1
    print("error num",error_num)

face_extract("aragaki",0)