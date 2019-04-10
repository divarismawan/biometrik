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
        img_array = cv2.imread(os.path.join(path,img),0)

        # gray      = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        gaussian = cv2.GaussianBlur(img_array, (3, 3), 0)

        lapl = cv2.Laplacian(gaussian, cv2.CV_16S, 3)

        abs_dst = cv2.convertScaleAbs(lapl)

        cv2.imshow("asli",img_array)
        cv2.imshow("hasil grayscale",gaussian)
        cv2.imshow("hasil laplacian", abs_dst)

        cv2.waitKey(0)
        break
    break
