import indicoio
import numpy as np
import matplotlib.pyplot as plt
indicoio.config.api_key = '929ac1b1d3eac44546d60bf0a359816a'

# single example                                                                                                               
lx=[]
angry=[];sad=[];neutral=[];surprise=[];happy=[];fear=[];
for i in range(1,5):
        lx.append(i)
for i in range(1,5):
        print("example("+str(i)+")")
        tmp = indicoio.fer("imgs/face_"+str(i)+".jpg")
        print(tmp)
	angry.append(tmp[u'Angry']);sad.append(tmp[u'Sad']);neutral.append(tmp[u'Neutral']);surprise.append(tmp[u'Surprise']);
	happy.append(tmp[u'Happy']);fear.append(tmp[u'Fear']);

plt.figure(1)
plt.plot(lx,angry, 'ro', linewidth=2.0)
plt.axis([0,5, 0, 1])

plt.subplot(220)
plt.plot(lx,sad, 'bo', linewidth=2.0)
plt.axis([0, 5, 0, 1])

plt.subplot(222)
plt.plot(lx,neutral, 'go', linewidth=2.0)
plt.axis([0, 5, 0, 1])

plt.subplot(223)
plt.plot(lx,surprise, 'yo', linewidth=2.0)
plt.axis([0, 5, 0, 1])

plt.subplot(224)
plt.plot(lx,happy, 'mo', linewidth=2.0)
plt.axis([0, 5, 0, 1])

plt.subplot(225)
plt.plot(lx,fear, 'ko', linewidth=2.0)
plt.axis([0, 5, 0, 1])
plt.show()
