import indicoio
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

'''
import numpy as np
import time
import cv2
cap = cv2.VideoCapture('a.mp4')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cv2.waitKey(500);
#time.sleep(5)
count=1
#print("f;akdf")
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame',gray)
    cv2.imwrite("imgs/face_"+str(count)+".jpg")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

'''

indicoio.config.api_key = '929ac1b1d3eac44546d60bf0a359816a'

# single example                                                                                                               
lx=[]
angry=[];sad=[];neutral=[];surprise=[];happy=[];fear=[];max_emo=[];emo_colour=[]
for i in range(1,10):
        lx.append(i)

i=1
#for i in range(1,10):
while (i<10):
        print("example("+str(i)+")")
        try:
                tmp = indicoio.fer("imgs/face_"+str(i)+".jpg")
        except:
                print("connection refused")
                sleep(2)
                continue
        print(tmp)
	angry.append(tmp[u'Angry']);sad.append(tmp[u'Sad']);neutral.append(tmp[u'Neutral']);surprise.append(tmp[u'Surprise']);
	happy.append(tmp[u'Happy']);fear.append(tmp[u'Fear']);
        sleep(2)
        i=i+1
        emo=max(tmp.items(), key=lambda k: k[1])
        if(emo[0]=="Angry"):
                emo_colour.append('r')
                max_emo.append(emo[1])
        elif(emo[0]=="Sad"):
                emo_colour.append('b')
                max_emo.append(emo[1])
        elif(emo[0]=="Neutral"):
                emo_colour.append('g')
                max_emo.append(emo[1])
        elif(emo[0]=="Surprise"):
                emo_colour.append('y')
                max_emo.append(emo[1])
        elif(emo[0]=="Happy"):
                emo_colour.append('m')
                max_emo.append(emo[1])
        elif(emo[0]=="Fear"):
                emo_colour.append('k')
                max_emo.append(emo[1])

print max_emo
print emo_colour
plt.figure(1)
ax=plt.subplot(221)
ax.set_title("angry")
plt.plot(lx,angry, 'ro-', linewidth=2.0)
plt.axis([0,10, 0, 1])

ax=plt.subplot(222)
ax.set_title("sad")
plt.plot(lx,sad, 'bo-', linewidth=2.0)
plt.axis([0, 10, 0, 1])

ax=plt.subplot(223)
ax.set_title("neutral")
plt.plot(lx,neutral, 'go-', linewidth=2.0)
plt.axis([0, 10, 0, 1])

ax=plt.subplot(224)
ax.set_title("surprise")
plt.plot(lx,surprise, 'yo-', linewidth=2.0)
plt.axis([0, 10, 0, 1])

plt.figure(2)
ax=plt.subplot(221)
ax.set_title("happy")
plt.plot(lx,happy, 'mo-', linewidth=2.0)
plt.axis([0, 10, 0, 1])

ax=plt.subplot(222)
ax.set_title("fear")
plt.plot(lx,fear, 'ko-', linewidth=2.0)
plt.axis([0, 10, 0, 1])

plt.figure(3)
plt.scatter(lx,max_emo,color=emo_colour)

plt.show()
