print('FLAMES')
s=input('enter a name:')
s1=input(' enter a name: ')
flames=list('flames')
output=list(s)
put=list(s1)

y=list(s1)
for i in output:
    if i in put:
       
        put.remove (i)
for i in y:
    if i in output:
        output.remove (i)

res=len(output)+len(put)
print(res)
i=len(flames)
print(i)
while i >= 2:
   
    t= res%i
    flames.remove(flames[t-1])
    
    
    i-=1
d={'f':'friend',
   'l':'lover',
   'a':'affection',
   'm':'marriage',
   'e':'enemy',
   's':'sister'}
for i in flames:
    relation=i
print(relation)    

print(f' relastionship between {s} and {s1} is {d[relation] }')
