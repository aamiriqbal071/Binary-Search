def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)-1
    steps = 0
    
    while(start<=end):
        print("Step", steps, ":" ,str(list[start:end+1]))
        steps = steps+1
        middle = (start + end) // 2
        
        if element == list[middle] :
            return middle
        if element < list[middle]:
            end = middle -1
            print(end)
        else:
            start = middle + 1
            print(start)

    return -1


my_list =[]
my_list=input("Enter the set of number :")
target = input("Enter the target number:")

binary_search(my_list, target)