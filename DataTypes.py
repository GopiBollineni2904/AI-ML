'''
there are 6 datatypes:
1) String-Str 
2)Bytes-bytes
3)byteArray-bytearray 
4)List-list 
5)Tuple-tuple 
6)Range-range
7)Set-set
8)Dictionary-dict
'''

print("This is an example of STRING DataType")
#STRING DataType-->(not mutable but slicing,indexing and reverse indexing are possible)
 #they are enclosed in single or double quotes ore triple-single or triple-double quotes
s='Welcome to CORE PYTHON!!!' #STRING
#slicing
print(s[0:])
print(s[11:22])
#indexing
print(s[0],s[8])
#ReverseIndexing
print(s[-1])
print(type(s))
print("\n")
print("This is an example of BYTES DataType")
#BYTES DataType-->(immutable,and slicing and indexing are also not possible)
 #A bytes array can store numbers from 0 to 255 and no -ve numbers.
elements=[10,20,0,40,15] #List of byte numbers
x=bytes(elements) #converting the list into bytes array
print(x[4]) #display element
for i in x:
    print(i)
print("\n")
print(type(x))
print("This is an example of BYTEARRAY DataType")
#BYTEARRAY DataType-->(Mutable but slicing and indexing cannot be done)
 #it is similar to the bytes datatype but this one can be modified(mutable)
y=bytearray(elements)
for i in y:
    print(i)
print("\n")
y[2]=30;y[4]=50;
for i in y:
    print(i)
print("\n")
print(type(y))
print("This is an example of LIST DataType")
#LIST DataType-->(Mutable,Slicing and Indexing are also possible)
 #It is same as an array in any other language but any data of different datatypes can be stored in this.
lst=[1,2,3,4,5,6]
#displaying list
for i in lst:
    print(i)
print(lst[3]) #indexing
print(lst[-4])#ReverseIndexing
print(lst[2:4])#Slicing
print(lst*2)
print(type(lst))
print("\n")
print("This is an example of TUPLE DataType")
#TUPLE DataType-->(Immutable but Slicing and Indexing are possible)
 #It is similar to a LIST DataType, the only difference is that a TUPLE is IMMUTABLE and this uses PARENTHESIS()
t=(99,88,77,66,55,44,33,22,11)
for i in t:
    print(i)
print(t[4])#Indexing
print(t[-2])#reverseIndexing
print(t[0:5])#slicing
print(t*2)
print(type(t))
print("\n")
print("This is an example of RANGE DataType")
#RANGE DataType-->(Immutable,no concept of Slicing and Indexing)
 #It is used to specify a 'Range',It can also be used in a for loop to control the number of times the loop is generated.
 #It can also be used in the case of generating sequential numbers.
r=range(10)
for i in r:
    print(i)
r1=range(20,40,2)#this will create a range object with starting number-20 and ending number=39 and step=2
for i in r1:
    print(i)
lst1=[range(10)];t1=(range(10))
for i in lst1: print(i)
for i in t1: print(i)
print(type(lst1))
print(type(r1))
print("\n")
print("This is an example of SET DataType")
#SET DataType-->(IMMUTABLE, no concept of slicing and indexing)
 #Elements within a created SET can be modified using update() & remove()
 #The elements in a set are unordered and therefore cannot be indexed or sliced
 #Duplicate elements are neglested while storing or displaying a SET,rather the duplicates are stored as an instance of the original
set1={10,20,30,40,50,60,70,80,90}
print(s)
#it can also be used to convert any set of data into a SET DataType
ch=set('HELLO')
print(ch)
set1.update([100,110])
print(set1)
set1.remove(110); print(set1)
print(type(set1))
print("\n")
print("This is an example of FROZENSET DataType")
#FROZENSET DataType-->(same as SET DataType but the elem=ents in this are IMMUTABLE)
 #a FROZENSET can only be created by passing a SET to the frozenset() function
s1={10,20,30,40,50,60,70,80,90}
fs=frozenset(s1)
print(fs)
fs1=frozenset('example')
print(fs1)
print("\n")
print("This is an example of Mapping/DICTIONARY DataType")
#DICTIONARY DataType-->(it represents data in the form of "key value pairs" so that when the key is given we can retrieve the value from it)
 #the key and the value are sperated by colon(:) and every pair should be seperated by a comma.And all the elements should be enclosed inside curly braces{}
 #this datatype is completely modifiable and this can be done by storing new values into the dict. and values can be remover using the 'del' module.
dic={1:'A',2:'B',3:'C',4:'D',5:'E'}
print(dic)
print(dic.keys())#to retrieve only the keys from the dictionary
print(dic.values())
del dic[2]#deleting an entry from the dict.
print(dic)
d={}#empty DICTIONARY
d[10]='LUCIFER';d[20]='Alexander';#Storing values into the dict.
print(d)
print(type(dic))
print("="*20)
print("END OF THE DATATYPES PROGRAM")
print("="*20)