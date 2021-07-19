import time

def bubblesort(a):
    #a is the list
    b = len(a) - 1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
    return a

lst1 = input("Enter a sequence of numbers: ").split()
lst = [int(x) for x in lst1]


toc = time.perf_counter()
print(bubblesort(lst))
tic = time.perf_counter()

#check and print runtime
print('\nruntime: ', f"{tic-toc:0.4f}")
