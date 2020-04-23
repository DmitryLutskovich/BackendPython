import configparser  
import cv2
import os
import string
import base64
import socket
import msvcrt

from findmethod import findmethod
find = findmethod()

#a = input()
print('If you want to run, then press the spacebar')
input_char = msvcrt.getch().decode("utf-8") 
while input_char != " ":
    input_char = msvcrt.getch().decode("utf-8") 

sock = socket.socket()
sock.bind(('', 9080))
sock.listen(1)
conn, addr = sock.accept()

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг
route = config["Route"]["Path1"]  
count = 1
count2 = 1
diction = {0: 'Vlad',
          1: 'Dima',
          2: 'Unknown'}

for f in os.listdir(route):
    file_name = os.path.join(route, f) # путь фотографи
    if not os.path.isfile(file_name):
        continue
    image = cv2.imread(file_name) #фотография
    #cv2.imshow("image", image)
    #cv2.waitKey (0)
    #print (image)
    results = find.find_face(file_name)
    
    #if results == ():
    #    print ('Nothing')
    #else :
    if results != ():
        for (x, y, w, h) in results:
                #x, y, w, h = res['box']
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  
                roi_color = image[y:y + h, x:x + w] 
                #вызов нейронки для определения лица 
                #получение ключа и вероятность
                kort = (0,90)
                key = kort[0]
                proc = str(kort[1])
                name = diction.get(key)
                text = name + '-' + proc
                #res = {0: '90%'}
                #for k in res:
                #    key = k
                #proc = res.get(key)
                #name = diction.get(key)
                #text = name + '-' + proc
                #print(name, proc)
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imwrite(os.path.join("photoface", "image"+str(count) + ".jpeg"), roi_color)
                count = count + 1
                #cv2.putText(image, "Hello world!", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
            # Сохраняем лицо
        
        cv2.imwrite(os.path.join("photokadr", "image"+str(count2) + ".jpeg"), image)
        img = os.path.join("photokadr", "image"+str(count2) + ".jpeg")
        count2 = count2 + 1
        way = img.encode('utf-8')
        conn.send(way)
        print(way)
conn.close()