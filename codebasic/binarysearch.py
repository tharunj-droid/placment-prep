from util import time_it


def linear_search(numbers_list,number_to_find):
    for index,element in enumerate(numbers_list):
        if element==number_to_find:
            return index

    return -1

def binary_search(numbers_list,number_to_find):
    left_index=0
    right_index=len(numbers_list)-1
    mid_index=0
    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=numbers_list[mid_index]

                
        if mid_number==numbers_list[right_index]:
            return right_index
        
        if mid_number==number_to_find :
            return mid_index

        if mid_number==numbers_list[left_index]:
            return left_index

        if mid_number<number_to_find:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    return-1


def rec_bin_search(numbers_list,number_to_find,left_index,right_index):
    if right_index<left_index:
        return -1
    mid_index=(left_index+right_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number=numbers_list[mid_index]
    if mid_number==number_to_find:
        return mid_index
    if mid_number<number_to_find:
            left_index=mid_index+1
    else:
         right_index=mid_index-1

    rec_bin_search(numbers_list,number_to_find,left_index,right_index)

if __name__ =="__main__":
    # numbers_list=[1,3,1213,534,5674,32]
    # numbers_to_find=12131
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    numbers_to_find = 15  
    print(binary_search(numbers_list,numbers_to_find))
   