import time

def selsort(lst, r):
    for x in range(r):
        min = x
        for y in range(x+1, r):
            if lst[y] < lst[min]:
                min = y
        lst[x], lst[min] = lst[min], lst[x]
    
    return lst

lst1 = input('Enter a list of values: ').split()
lst = [int(x) for x in lst1]
r = len(lst)

tic = time.perf_counter()
print(selsort(lst, r))
toc = time.perf_counter()

#checks and print runtime
print('\nruntime: ', f'{toc-tic:0.4f}')