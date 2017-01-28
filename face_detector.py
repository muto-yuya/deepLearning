#! /usr/bin/python
# -*- coding: utf-8 -*-
u"""dlibによる顔画像検出."""
import cv2
import dlib
from make_face_extracted import checkFileNum

# 画像ファイルパスを指定
person = 'other'
input_dir = '/Users/mutouyuuya/deepLearningContest/'+person
out_put_dir = '/Users/mutouyuuya/deepLearningContest/'+person+'_detected_learning'
start_num = 704

def facedetector_dlib(img, image_path):
    try:
        detector = dlib.get_frontal_face_detector()
        # RGB変換 (opencv形式からskimage形式に変換)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # frontal_face_detectorクラスは矩形, スコア, サブ検出器の結果を返す
        dets, scores, idx = detector.run(img_rgb, 0)
        # 矩形の色
        color = (0, 0, 255)
        s = ''
        if len(dets) > 0:
            # 顔画像ありと判断された場合
            for i, rect in enumerate(dets):
                # detsが矩形, scoreはスコア、idxはサブ検出器の結果(0.0がメインで数が大きい程弱い)
                # print rect, scores[i], idx[i]
                cv2.rectangle(img, (rect.left(), rect.top()), (rect.right(), rect.bottom()), color, thickness=10)
                s += (str(rect.left()) + ' ' + str(rect.top()) + ' ' + str(rect.right()) + ' ' + str(rect.bottom()) + ' ')
            s += image_path
        # 矩形が書き込まれた画像とs = 'x1 y1 x2 y2 x1 y1 x2 y2 file_name'
        # 顔が無ければ s='' が返る
        return img, s
    except:
        # メモリエラーの時など
        return img, ""


def getFaces(input_image):
    detector = dlib.get_frontal_face_detector()
    results = []
    height, width = input_image.shape[:2]
    rects, scores, types = detector.run(input_image,0)
    for i, rect in enumerate(rects):
        top, bottom, left, right = rect.top(), rect.bottom(), rect.left(), rect.right()
        if min(top, height - bottom - 1, left, width - right - 1) < 0:
            continue
        results.append(input_image[top : bottom, left : right],)
    return results

if __name__ == '__main__':
    # img = cv2.imread(sample_img_path)
    # img, s = facedetector_dlib(img, sample_img_path)
    # cv2.imwrite('output_' + sample_img_path, img)
    # f = open('./rect.txt', 'w')
    # f.write(s)
    # f.close()

    for i in range(start_num,checkFileNum(input_dir)-1):
        input_image = cv2.imread(input_dir+"/"+person+str(i)+'.jpg')
        images_array = getFaces(input_image)
        count = 0
        for image in images_array:
            image = cv2.resize(image,(112,112))
            cv2.imwrite(out_put_dir+'/'+person+str(i)+'_'+str(count)+'.jpg',image)
            count += 1
