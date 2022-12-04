comparisons = 0

def read_txt(filename):
    with open(filename) as f:
        lines = f.readlines()
        nums = [int(line.split("\n")[0]) for line in lines]
    return nums

def find_median(arr, first, middle, last):
    a = arr[first]
    b = arr[middle]
    c = arr[last]
    mini = min(a,b,c)
    maxi = max(a,b,c)
    if mini != a and maxi != a: return first
    elif mini != b and maxi != b: return middle
    else: return last


def partition(arr, low, high, mode):
    global comparisons
    if mode == "first":
        pivot = low
    elif mode == "last":
        pivot = high
    else:
        pivot = find_median(arr, low, low + (high - low) // 2, high)

    arr[pivot], arr[low] = arr[low], arr[pivot]
    i = low + 1
    for j in range(low+1, high+1):
        if arr[j] < arr[low]:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i-1], arr[low] = arr[low], arr[i-1]
    comparisons += high - low
    return i-1

def quicksort(arr, low, high, mode):
    if low < high:
        pi = partition(arr, low, high, mode)
        quicksort(arr, low, pi-1, mode)
        quicksort(arr, pi+1, high, mode)


nums = read_txt('QuickSort.txt')
quicksort(nums, 0, len(nums) - 1, 'first')
print(comparisons)
nums = read_txt('QuickSort.txt')
comparisons = 0
quicksort(nums, 0, len(nums) - 1, 'last')
print(comparisons)
nums = read_txt('QuickSort.txt')
comparisons = 0
quicksort(nums, 0, len(nums) - 1, 'median')
print(comparisons)
