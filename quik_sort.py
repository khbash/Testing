def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        bigger = [i for i in arr[1:] if i > pivot]
        smaller = [i for i in arr[1:] if i <= pivot]

        return quick_sort(bigger) + [pivot] + quick_sort(smaller)

a = list(map(int, input().split()))

result = quick_sort(a)
print(result)

