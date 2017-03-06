import json
import webbrowser
from nltk.stem.porter import *
from word2vec_code import get_word2vec
def fun(image,fps):
	x=int(image)
	pos=x/float(fps)
	print pos
	URL="https://www.youtube.com/watch?v=xDMP3i36naA#t="+str(pos)+"s"
	print URL
	webbrowser.open(URL)

f=open('abc.txt','w')
tweets = []
for line in open('response.txt', 'r'):
    tweets.append(json.loads(line))

f.write(str(tweets[0]['result_final'][0]))


#for i in tweets[0]['result_final'][0]['results'][0]['tags']:
#	print i['tag'],i['confidence']



dict={}
n=len(tweets[0]['result_final'])
#print "n="+str(n)

cnt=0
for outer in tweets[0]['result_final']:
	cnt=cnt+1


 	if outer['results'][0]['image'].endswith('.jpg'):
		outer['results'][0]['image']=outer['results'][0]['image'][:-4]
	else:
		outer['results'][0]['image']=outer['results'][0]['image'][:-5]
	foo=outer['results'][0]['image'][45:]
	print "val="+foo+str(cnt)
	if foo=='':
		continue

	for j in outer['results'][0]['tags']:
		var= str(j['tag'])#,j['confidence']
		stemmer = PorterStemmer()
		var=stemmer.stem(var)
		if var in dict:

			dict[var]=min(int(foo),dict[var])
		else:
			dict[var]=int(foo)

	print
for i in dict:

	print i, dict[i]

q=raw_input("Enter a word")
stemmer = PorterStemmer()
stemmed_q=stemmer.stem(q)

if stemmed_q in dict:
	print dict[stemmed_q]
	fun(dict[stemmed_q],30)
else:
	li=get_word2vec(q)
	f=0
	for var in li:
		var=stemmer.stem(var)
		if var in dict:
			f=1
			#print dict[var]
			print var
			fun(dict[var],30)
			break
	if f==0:
		print "Object not found in the Video!"
