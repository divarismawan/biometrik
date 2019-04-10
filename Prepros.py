import os
import cv2
import matplotlib as plt




url_class = 'face/'
classes   = os.listdir(url_class)

print("Jumlah Kelas : {}".format(len(classes)))
print("Nama Kelas : {}".format(classes))


for category in classes:
    path = os.path.join(url_class, category)
    print(category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img))
        gray      = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        cv2.imshow("asli",img_array)
        cv2.imshow("hasil",gray)
        cv2.waitKey(0)
        break
    break