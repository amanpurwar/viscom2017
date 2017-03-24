import indicoio
import numpy as np
import matplotlib.pyplot as plt
indicoio.config.api_key = '929ac1b1d3eac44546d60bf0a359816a'

# single example                                                                                                               
lx=[]
angry=[];sad=[];neutral=[];surprise=[];happy=[];fear=[];
for i in range(1,30):
        lx.append(i)
for i in range(1,30):
        print("example("+str(i)+")")
        print(indicoio.fer("imgs/face_"+str(i)+".jpg"))
        tmp = indicoio.fer("imgs/face_"+str(i)+".jpg")
        angry.append(tmp[u'Angry']);sad.append(tmp[u'Sad']);neutral.append(tmp[u'Neutral']);surprise.append(tmp[u'Surprise']);\
happy.append(tmp[u'Happy']);fear.append(tmp[u'Fear']);

plt.figure(1)
plt.plot(lx,angry, 'ro')
plt.axis([0, 30, 0, 1])

plt.figure(2)
plt.plot(lx,sad, 'bo')
plt.axis([0, 30, 0, 1])

plt.figure(3)
plt.plot(lx,neutral, 'go')
plt.axis([0, 30, 0, 1])

plt.figure(4)
plt.plot(lx,surprise, 'yo')
plt.axis([0, 30, 0, 1])

plt.figure(5)
plt.plot(lx,happy, 'mo')
plt.axis([0, 30, 0, 1])

plt.figure(6)
plt.plot(lx,fear, 'ko')
plt.axis([0, 30, 0, 1])
plt.show()
