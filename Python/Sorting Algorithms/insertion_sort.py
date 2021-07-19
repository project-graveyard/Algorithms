import time

#where a is our list of values
def isort(a):
    for x in range(1, len(a)):
        k = a[x]
        j = x - 1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
    
    return a
        
lst1 = input('Enter a list of values: ').split()
lst = [int(x) for x in lst1]

tic = time.perf_counter()
print(isort(lst))
toc = time.perf_counter()

#check and print runtime
print('\nruntime: ', f'{toc-tic:0.4f}')