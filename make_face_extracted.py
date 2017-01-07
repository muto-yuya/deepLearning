import face_detecter2
import os


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
    print("file number:",checkFileNum(person_name)-1)
    for i in range(first_num,checkFileNum(person_name)-1):
        face_detecter2.detect_face_rotate(person_name+"/"+person_name+str(i)+".jpg",'.',person_name+'_detected')

if __name__ == '__main__':
    face_extract("other",0)