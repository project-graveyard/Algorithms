import time

def merge(left, right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            #if it is ascending order, use(<=) else use(>=)
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result += left[i:]
    result += right[j:]
    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

lst1 = input("Enter sequence of numbers: ").split()
lst = [int(x) for x in lst1]

tic = time.perf_counter()
print(mergesort(lst))
toc = time.perf_counter()

#check and print runtime
print('\nruntime: ', f"{toc-tic:0.4f}")