def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i, 0 ,-1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    for i in arr:
        print(i)


def main():
    l = []
    try:
        while True:
            s = input().strip()
            if s :
                l.append(s)
    except:
        insertion_sort(l)    
main()

