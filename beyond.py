import requests 
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

requests.packages.urllib3.disable_warnings()

def getAnalysis(API_Key,WavPath):
    res = requests.post("https://token.beyondverbal.com/token",data={"grant_type":"client_credentials","apiKey":API_Key})
    token = res.json()['access_token']
    headers={"Authorization":"Bearer "+token}
    pp = requests.post("https://apiv3.beyondverbal.com/v3/recording/start",json={"dataFormat": { "type":"WAV" }},verify=False,headers=headers)
    recordingId = pp.json()['recordingId']
    with open(WavPath,'rb') as wavdata:
        r = requests.post("https://apiv3.beyondverbal.com/v3/recording/"+recordingId,data=wavdata, verify=False, headers=headers)
        return r.json()


#json = getAnalysis("96828e31-dfe9-400f-904b-8d6cb5836c87","/home/amanpurwar/videoplayback.wav")
#print(json)
json ={u'status': u'success', u'recordingId': u'6d125d65-58be-4324-99ea-ec155957b828', u'result': {u'duration': u'105836.50', u'analysisSegments': [{u'duration': 14010, u'analysis': {u'AudioQuality': {u'Value': u'11.75'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Love, Happiness', u'Id': 8}, u'Secondary': {u'Phrase': u'Loneliness, Unfulfillment', u'Id': 7}}, u'Composite': {u'Primary': {u'Phrase': u'Friendship, joy, harmony and love.', u'Id': 242}, u'Secondary': {u'Phrase': u'Longing. Emotional void combining sadness and joy.', u'Id': 77}}}, u'Gender': {u'Group': u'female'}, u'Arousal': {u'Group': u'low', u'Value': u'0.85', u'Summary': {u'ModePct': 100, u'Mode': u'low', u'Mean': u'0.85'}}, u'Valence': {u'Group': u'positive', u'Value': u'88.98', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'88.98'}}, u'Temper': {u'Group': u'medium', u'Value': u'24.35', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'24.35'}}}, u'offset': 16}, {u'duration': 13690, u'analysis': {u'AudioQuality': {u'Value': u'12.47'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Leadership, Charisma', u'Id': 6}, u'Secondary': {u'Phrase': u'Love, Happiness', u'Id': 8}}, u'Composite': {u'Primary': {u'Phrase': u'Admiration, protection of inner convictions, patriotism.', u'Id': 185}, u'Secondary': {u'Phrase': u'Happiness, satisfaction, love.', u'Id': 197}}}, u'Gender': {u'Group': u'female'}, u'Arousal': {u'Group': u'low', u'Value': u'9.72', u'Summary': {u'ModePct': 100, u'Mode': u'low', u'Mean': u'5.29'}}, u'Valence': {u'Group': u'positive', u'Value': u'88.11', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'88.54'}}, u'Temper': {u'Group': u'medium', u'Value': u'24.46', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'24.40'}}}, u'offset': 14036}, {u'duration': 14250, u'analysis': {u'AudioQuality': {u'Value': u'10.42'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Love, Happiness', u'Id': 8}, u'Secondary': {u'Phrase': u'Creative, Passionate', u'Id': 1}}, u'Composite': {u'Primary': {u'Phrase': u'Happiness, satisfaction, love.', u'Id': 197}, u'Secondary': {u'Phrase': u'Action based on enthusiasm. Use of "positive imagination". Expression of empowering experience.', u'Id': 188}}}, u'Gender': {u'Group': u'male'}, u'Arousal': {u'Group': u'high', u'Value': u'96.67', u'Summary': {u'ModePct': u'66.67', u'Mode': u'low', u'Mean': u'35.75'}}, u'Valence': {u'Group': u'positive', u'Value': u'98.20', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'91.76'}}, u'Temper': {u'Group': u'medium', u'Value': u'37.01', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'28.60'}}}, u'offset': 27736}, {u'duration': 14120, u'analysis': {u'AudioQuality': {u'Value': u'11.87'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Love, Happiness', u'Id': 8}, u'Secondary': {u'Phrase': u'Love, Happiness', u'Id': 8}}, u'Composite': {u'Primary': {u'Phrase': u'Happiness, satisfaction, love.', u'Id': 197}, u'Secondary': {u'Phrase': u'Happiness, satisfaction, love, harmony, warmth.', u'Id': 200}}}, u'Gender': {u'Group': u'male'}, u'Arousal': {u'Group': u'low', u'Value': u'7.29', u'Summary': {u'ModePct': 75, u'Mode': u'low', u'Mean': u'28.63'}}, u'Valence': {u'Group': u'positive', u'Value': u'91.87', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'91.79'}}, u'Temper': {u'Group': u'medium', u'Value': u'23.06', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'27.22'}}}, u'offset': 41996}, {u'duration': 13570, u'analysis': {u'AudioQuality': {u'Value': u'6.41'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Leadership, Charisma', u'Id': 6}, u'Secondary': {u'Phrase': u'Supremacy, Arrogance', u'Id': 11}}, u'Composite': {u'Primary': {u'Phrase': u'Talkativeness, extroversion.', u'Id': 314}, u'Secondary': {u'Phrase': u'Missionary leadership. Stubbornness.', u'Id': 395}}}, u'Gender': {u'Group': u'male'}, u'Arousal': {u'Group': u'low', u'Value': u'13.75', u'Summary': {u'ModePct': 80, u'Mode': u'low', u'Mean': u'25.66'}}, u'Valence': {u'Group': u'positive', u'Value': u'71.87', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'87.80'}}, u'Temper': {u'Group': u'medium', u'Value': u'23.13', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'26.40'}}}, u'offset': 56126}, {u'duration': 14270, u'analysis': {u'AudioQuality': {u'Value': u'10.72'}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Creative, Passionate', u'Id': 1}, u'Secondary': {u'Phrase': u'Self-Control, Practicality', u'Id': 10}}, u'Composite': {u'Primary': {u'Phrase': u'Powerful emotions and desires. Imagination.', u'Id': 191}, u'Secondary': {u'Phrase': u'Cold, rational, level-headed, conservative.', u'Id': 158}}}, u'Gender': {u'Group': u'male'}, u'Arousal': {u'Group': u'low', u'Value': u'26.19', u'Summary': {u'ModePct': u'83.33', u'Mode': u'low', u'Mean': u'25.75'}}, u'Valence': {u'Group': u'positive', u'Value': u'85.78', u'Summary': {u'ModePct': 100, u'Mode': u'positive', u'Mean': u'87.47'}}, u'Temper': {u'Group': u'medium', u'Value': u'23.45', u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'25.91'}}}, u'offset': 69706}, {u'duration': 16100, u'analysis': {u'AudioQuality': {u'Value': 0}, u'Mood': {u'Group11': {u'Primary': {u'Phrase': u'Love, Happiness', u'Id': 8}, u'Secondary': {u'Phrase': u'Love, Happiness', u'Id': 8}}, u'Composite': {u'Primary': {u'Phrase': u'Blind admiration, blind love.', u'Id': 380}, u'Secondary': {u'Phrase': u'Happiness, love, restrained warmth.', u'Id': 239}}}, u'Gender': {u'Group': u'male'}, u'Arousal': {u'Group': u'high', u'Value': u'85.20', u'Summary': {u'ModePct': u'71.43', u'Mode': u'low', u'Mean': u'34.24'}}, u'Valence': {u'Group': u'neutral', u'Value': u'25.07', u'Summary': {u'ModePct': u'85.71', u'Mode': u'positive', u'Mean': u'78.55'}}, u'Temper': {u'Group': u'medium', u'Value': 25, u'Summary': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'25.78'}}}, u'offset': 89606}], u'analysisSummary': {u'AnalysisResult': {u'Arousal': {u'ModePct': u'71.43', u'Mode': u'low', u'Mean': u'34.24'}, u'Valence': {u'ModePct': u'85.71', u'Mode': u'positive', u'Mean': u'78.55'}, u'Temper': {u'ModePct': 100, u'Mode': u'medium', u'Mean': u'25.78'}}}, u'sessionStatus': u'Done'}}

n = len(json)
Temper=[]
Valence=[]
Arousal=[]
TemperVal=[]
print(json['result']['analysisSegments'][0])
print(json['result']['analysisSegments'][2])
temo_color=[]
temo_value=[]
vemo_color=[]
vemo_value=[]
aemo_color=[]
aemo_value=[]

for j in json['result']['analysisSegments']:	
	Temper.append((j['analysis']['Temper']['Group'],j['analysis']['Temper']['Value']))
	t=j['analysis']['Temper']['Group']
	if (t=='low'):
		temo_color.append('r')
	elif(t=='medium'):
		temo_color.append('b')
	else:
		temo_color.append('y')
	TemperVal.append(j['analysis']['Temper']['Value'])
	Valence.append((j['analysis']['Valence']['Group'],j['analysis']['Valence']['Value']))
	v=j['analysis']['Valence']['Group']
	if (v=='positive'):
		vemo_color.append('r')
	elif(v=='neutral'):
		vemo_color.append('y')
	else:
		vemo_color.append('g')
	
	Arousal.append((j['analysis']['Arousal']['Group'],j['analysis']['Arousal']['Value']))
	a=j['analysis']['Arousal']['Group']
	if (a=='low'):
		aemo_color.append('r')
	else:
		aemo_color.append('b')
	
	

lx=[]
tmp=0
ValenceVal=[i for (s,i) in Valence]
ArousalVal=[i for (s,i) in Arousal]

for j in json['result']['analysisSegments']:
	tmp+=j['duration']
	lx.append(tmp)
print(tmp)

temo_value=TemperVal
aemo_value=ArousalVal
vemo_value=ValenceVal



plt.figure(1)
##ax=plt.subplot(221)
plt.suptitle("Temper")
plt.scatter(lx,temo_value,color=temo_color)
plt.axis([0,tmp+10000,0,100.0])

plt.figure(2)
##ax=plt.subplot(221)
plt.suptitle("Valence")
plt.scatter(lx,vemo_value,color=vemo_color)
plt.axis([0,tmp+10000,0,100.0])


plt.figure(3)
##ax=plt.subplot(221)
plt.suptitle("Arousal")
plt.scatter(lx,aemo_value,color=aemo_color)
plt.axis([0,tmp+10000,0,100.0])
plt.show()



	



	
	
