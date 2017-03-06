

li=""
with open('response.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    li=li+c

print li    
fn=""
for i in range(0,len(li)-2):
	fn+=li[i]
	if li[i+1]=='{' and li[i]=='}':
		fn+=','
	
f=open('response.txt','w')		
f.write(str(fn))		


		
		
