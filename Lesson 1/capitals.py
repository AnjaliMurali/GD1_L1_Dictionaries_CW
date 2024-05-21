capitals={}
capitals["India"]="New Delhi"
capitals["France"]="Paris"
capitals["UK"]="London"
print(capitals)
print(list(capitals.keys()))
print(list(capitals.values()))
#x=input("Enter country")
#y=capitals[x]
#print("The capital of " + x + " is " +y)
capitals["USA"]="Washington, D.C."
print(capitals)
del(capitals["USA"])
print(capitals)
#print(capitals["USA"]) #creates error as key doesn't exist
print(capitals.get("USA","Unknown"))
print(len(capitals))
print("UK" in capitals)
countries=[]
for k in capitals:
    countries.append(k)
countries.sort()
print(countries)