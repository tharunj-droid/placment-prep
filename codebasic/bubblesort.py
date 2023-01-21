def bubble_sort(elements):
    size=len(elements)

    for i in range(size-1):
        swapped=False
        for j in range(size-1):
            if elements[j]>elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=True

        if not swapped:
            break


if __name__ =='__main__':
    elements=[213,3,4345,754,867,2,31324,5]
    bubble_sort(elements)
    print(elements)