import cv2
import numpy as np
import os
import random
import imutils
import time
import glob

#import cuda # If use GPU
net = cv2.dnn.readNet("yolov4_last.weights", "yolov4.cfg")
# Name custom object
classesFile = "obj.names"

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

def detect_image(img):

    height, width, channels = img.shape
    # lol = [1932, 2301, 1905, 1812, 1800, 2223, 936, 1725, 2034, 1599, 2205, 2037,2700, 2040, 1620, 2160, 2880, 540, 960, 788, 800, 1536, 3024, 1668, 642, 2047, 1920, 640, 3072, 1440, 2000, 2039, 1529, 1241, 2048, 720, 686, 1381, 1296, 961, 853, 679, 1939, 1875, 370, 900, 1521, 4608, 1001, 512, 638, 945, 899, 1240, 785, 1528, 855, 842, 624, 521, 912, 315, 365, 539, 1441, 1000, 543, 726, 635, 1499, 1439, 400, 666, 597, 1527, 875, 600, 1526, 604, 589, 373, 864, 1824, 1596, 1826, 1512, 1530, 1667, 698, 1515, 718, 565, 768, 959, 901, 663, 355, 725, 300, 450, 1123, 482, 676, 939, 596, 1024, 678, 390, 1368, 1535, 1062, 148, 1483, 1541, 1767, 1264, 1339, 844, 314, 836, 534, 975, 1200, 595, 201, 700, 723, 266, 424, 527, 224, 1911, 500, 1280, 1500, 1600, 685, 816, 606, 671, 448, 916, 288, 360, 419, 1567, 660, 356, 1479, 913, 545, 958, 643, 917, 503]
    # cc = [2733, 4728, 2223, 2460, 2400, 2097, 2883, 1398, 2037, 1794, 2400, 2880, 2160, 960, 384, 940, 800, 4032, 1327, 2048, 2560, 1440, 4608, 1498, 1445, 2000, 1708, 1080, 1754, 540, 1616, 1944, 1280, 1439, 1458, 1707, 640, 961, 1876, 1875, 1600, 679, 3072, 678, 1000, 1024, 607, 1755, 636, 613, 595, 959, 1750, 751, 1954, 917, 851, 1603, 600, 1459, 915, 1696, 958, 720, 360, 843, 695, 794, 338, 1463, 859, 1561, 1559, 596, 426, 1460, 1167, 785, 864, 1824, 1816, 1576, 2016, 2040, 1667, 849, 601, 787, 466, 644, 703, 619, 400, 427, 1706, 1137, 1641, 1590, 1501, 148, 1441, 1362, 1476, 1887, 660, 707, 850, 1629, 693, 532, 1200, 421, 840, 1087, 300, 2047, 1540, 610, 1748, 724, 1510, 500, 1514, 1500, 448, 714, 913, 598, 900, 916, 1763, 1726, 626, 728]
    # if (height not in lol) and (width not in cc):
    #     return img, output_path

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)
    #print(outs)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            
            #writedown submit file
            #print(type(class_ids[i]),type(x),type(y),type(w+x),type(h+y))
            line = [out_img, str(class_ids[i]), str(x), str(y), str(x+w), str(y+h)]
            line = ', '.join(line) + '\n'
            submit.write(line)

            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label, (x, y-2), font, 2, color, 2)
    # output_image = img[y:(y+h), x:(x+w), :]
    
    # Store image
    cv2.imwrite(output_path, img)

    return img, output_path

def detect_video(video_path):
    # start detect video
    cap = cv2.VideoCapture(video_path)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    ret, frame = cap.read()
    WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter("output/Out_vid.avi",codec,15,(WIDTH,HEIGHT))
    cap.release()
    counts = 0
    cap = cv2.VideoCapture(video_path)
    while (True):
        ret, frame = cap.read()
        height, width, channels = frame.shape

        ####
        center = (width // 2, height // 2)
        M = cv2.getRotationMatrix2D(center, 180, 1.0)
        frame = cv2.warpAffine(frame, M, (width, height))
        ####

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    print(class_id)
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)  
                cv2.putText(frame, label, (x, y-2), font, 1, color, 2)
    
        counts += 1
        writer.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")
    
    #cuda.select_device(0)   # If use GPU

    # Detect video
    #detect_video('input/img1.MOV')

submit = open('submit.txt', "w+")

# inp_img = "INPUT/test.jpg"
# out_img = "test1.jpg"
# output_path = os.path.join("OUTPUT", out_img)
# img = cv2.imread(inp_img)
# image, image_path = detect_image(img)

for i in range(3):
    # Detec image
    index = i
    inp_img = "INPUT/test_%d.jpg" % (i)
    out_img = "test_%d.jpg" % (i)
    output_path = os.path.join("OUTPUT", out_img)
    img = cv2.imread(inp_img)
    image, image_path = detect_image(img)

submit.close()
#cuda.close()            # If use GPU
cv2.waitKey(0)