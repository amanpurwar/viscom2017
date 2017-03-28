import indicoio
import numpy as np
import matplotlib.pyplot as plt
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
angry=[];sad=[];neutral=[];surprise=[];happy=[];fear=[];
for i in range(1,10):
        lx.append(i)
for i in range(1,10):
        print("example("+str(i)+")")
        tmp = indicoio.fer("imgs/face_"+str(i)+".jpg")
        print(tmp)
	angry.append(tmp[u'Angry']);sad.append(tmp[u'Sad']);neutral.append(tmp[u'Neutral']);surprise.append(tmp[u'Surprise']);
	happy.append(tmp[u'Happy']);fear.append(tmp[u'Fear']);

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
plt.show()
