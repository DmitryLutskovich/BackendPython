import configparser  
import cv2
import os
#from ImageDetector import ImageDetector

a = input()

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг
route = config["Route"]["Path1"]  

for f in os.listdir(route):
    file_name = os.path.join(route, f)
    if not os.path.isfile(file_name):
        continue
    image = cv2.imread(file_name)
    cv2.imshow("image", image)
    cv2.waitKey (0)
    #print (image)










