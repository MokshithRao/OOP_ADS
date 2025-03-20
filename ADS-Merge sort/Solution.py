def merge(arr, aux, mid, low, high):
    for i in range(low, high + 1):
        aux[i]=arr[i]

    j = mid + 1
    k = low

    for i in range(low, high + 1):
        if k > mid:
            arr[i] = aux[j]
            j += 1
        elif j > high:
            arr[i] = aux[k]
            k += 1
        elif aux[k] <= aux[j]:
            arr[i] = aux[k]
            k += 1
        else:
            arr[i] = aux[j]
            j += 1

def merge_sort(arr, aux, low, high):
    if high <= low:
        return
    
    mid = (low + high)//2
    merge_sort(arr, aux, low, mid)
    merge_sort(arr, aux, mid + 1, high)
    merge(arr, aux, mid, low, high)
    return arr

def main():
    lst = []
    try:
        while True:
            s = input().strip()
            if s == "":
                break
            else:
                if s:
                    lst.append(s)
    except EOFError:
        arr = lst[:]
        aux = [0]*len(lst)
        arr = merge_sort(arr, aux, 0, len(lst)-1)
        for i in arr:
            print(i)
main()