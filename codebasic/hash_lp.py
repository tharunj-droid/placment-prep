class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        idx=0
        for idx,element in enumerate(self.arr[h]):
            if idx==None:
                self.arr[idx]=element
            else:

         

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
              if element[0]==key:
                del self.arr[h][index]