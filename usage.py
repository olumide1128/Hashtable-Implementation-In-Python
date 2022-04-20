from Implementation import HashTable

t = HashTable() #Create an instance of Hashtable

#Add keys and values to the Hashtable
t["march 6"] = 130 
t["march 1"] = 20
t["dec 17"] = 40

print(t.arr) #View the modified arr after adding items

print(t["dec 17"]) #Get Value of key passed in from the Hashtable

del t["march 1"] #Delete this item with key

print(t.arr) #Print arr to view change
