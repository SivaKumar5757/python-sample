str1=input("enter a first name:")
str2=input("enter second name:")
str1.lower()
str2.lower()
namelist=[x for x in str1]
namelist2=[x for x in str2]
namelist3=namelist+namelist2
set1=set()
set1.update(namelist3)
namelist3=sorted(set1)
flames=0
for i in namelist3:
    count1=namelist.count(i)
    count2=namelist2.count(i)
    if count1>count2:
        point = count1-count2
        flames+=point
    elif count2>count1:
        point=count2-count1
        flames+=point
print ("this pair flames score is",flames)
FLAMES=["F","L","A","M","E","S"]

if flames==1:
 FLAMES=['S']
elif flames==2 or flames==4:
 FLAMES=['E']
elif flames==6:
 FLAMES=['M']
elif flames==5:
 FLAMES=['F']
elif flames==3:
 FLAMES=['F']
else:

 if flames>6:
    flamesscore=flames%6
 ko=0

 for x in range(5):
     co=0
     go=len(FLAMES)
     co=go
     flamesscore+=ko
     
     print(co)
     if flamesscore>co:
        flamesscore=flamesscore%co
     FLAMES.pop(flamesscore-1)
     if x==1:
        ko=flamesscore
     if x>1:
         ko+=1
   
    
print(FLAMES)
print("their relationship is")
if "E"in FLAMES:
   print("enemy")
if "F"in FLAMES:
   print("frineds")
if "L"in FLAMES:
   print("love")
if "A"in FLAMES:
   print("affection")
if "M"in FLAMES:
   print("mariage") 
if "S"in FLAMES:
   print("sister or brother")
