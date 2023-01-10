#order of hashtable alone without collision handling is O(1) with collision handling implemented using linked list it is O(n) 


class HashTable:
    def __init__(self):
        self.Max=100
        self.arr=[[] for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for char in key:
            h==ord(char)
        return h%self.Max

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found= True
                break
            if not found:
                self.arr[h].append((key,val))     

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h] 

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h] = None


t=HashTable()
t['march 9']=120
t['march 19'] = 1231
t['march 17'] = 459

t['dec 10']
print(t['march 9'])

del t['march 9']
print(t['march 9'])

