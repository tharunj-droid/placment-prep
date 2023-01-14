class bst:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=bst(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=bst(data)
    def iot(self):
        elements=[]

        if self.left:#visit left tree
            elements+=self.left.iot()
        #visit root node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.iot()

        return elements

    def post(self):
        elements=[]
        if self.left:#visit left tree
            elements+=self.left.iot()
        #visit root node
        

        #visit right tree
        if self.right:
            elements+=self.right.iot()

        elements.append(self.data)
            
        return elements

    def pre(self):
        elements=[self.data]
        if self.left:#visit left tree
            elements+=self.left.iot()
        #visit root node
        

        #visit right tree
        if self.right:
            elements+=self.right.iot()
        return elements




    def search(self,val):
        if self.data==val:
            return True
        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def find_min(self):
        if self.left is None:
            return self.left
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.right
        return self.right.find_max()
    
    def find_sum(self):
        left_sum=self.left.find_sum() if self.left else 0
        right_sum=self.right.find_sum() if self.right else 0
        return self.data+left_sum+right_sum

    def del_val(self,value):
        if self.data is None:
            return self.data
            
        if value<self.data:
            if self.left:
                self.left=self.left.del_val(value)
        if value>self.data:
            if self.right:
                self.right=self.right.del_val(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            
            # min_value=self.right.find_min()
            # self.data=min_value
            # self.right=self.right.delete(min_value)

            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.del_val(max_val)
        return self







def build_tree(elements):

    root=bst(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__=="__main__":
    number_tree=build_tree([1,2,3,4,5,6])
    # print(number_tree.find_sum())
    # print(number_tree.pre())
    # print(number_tree.post())
    print(number_tree.iot())
    number_tree.del_val(1)
    print(number_tree.iot())


        

        