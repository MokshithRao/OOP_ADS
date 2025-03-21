def partition(a, lo, hi):  
    i = lo + 1
    j = hi
    v = a[lo]

    while True:
        while i <= j and a[i] <= v:
            i += 1

        while i <= j and a[j] >= v: 
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i] 
        else:
            break

    a[lo], a[j] = a[j], a[lo]  
    return j


def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        
        quick_sort(a, lo, p - 1)  
        quick_sort(a, p + 1, hi)  

def sort(a):
    quick_sort(a, 0, len(a) - 1)
    return a


def main():
    lst = []
    try:
        while True:
            s = input().strip()
            if s:
                lst.extend(s.split())
    except:
        sort(lst)
        for i in lst:
            print(i)
        
main()