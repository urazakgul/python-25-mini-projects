# Bu proje, sıralanmış bir listede bir öğeyi aramak için ikili arama algoritmasını uygulayan bir program oluşturmayı içerir.
# (This project involves creating a program that implements the binary search algorithm to search for an item in a sorted list.)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


arr = [int(target) for target in input("Enter a sorted list of numbers separated by commas: ").split(",")]
target = int(input("Enter the target value: "))

result = binary_search(arr, target)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")