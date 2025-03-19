def selection_sort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        print(f"{[min_idx]},{[i]}|| {min_idx} || {i}  ||  {arr}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        count += 1

    print(count)

    # for i in arr:
    #     print(i)


def main():
    l = []
    try:
        while True:
            s = input().strip()
            if s :
                l.append(s)
    except:
        selection_sort(l)    
# main()
# s = "KASUGANTIVENKATAMOKSHITHRAO"
# s = "22222222222"
# s = [1,2,3,4,5,6,7,8,9,10]
# s = [10,9,8,7,6,5,4,3,2,1]
# s = [1,2,3,4,5,10,9,8,7,6,5]
s = [5,2,0,22,7,15,22]
# s = "kurmaanilkumar"c

selection_sort(list(s))