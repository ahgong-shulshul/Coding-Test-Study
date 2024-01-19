def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid - 1)
        quick_sort(array, mid + 1, right)

# 피벗 기준 작은 값은 왼쪽으로 큰 값은 오른쪽으로 분리해주는 함수
# 바뀐 피벗의 인덱스를 리턴


def partition(array, left, right):
    low = left + 1
    high = right
    pivot = array[left]

    while low <= high:
        while low <= right and array[low] <= pivot:
            low += 1
        while high >= left and array[high] > pivot:
            high -= 1
        # 피벗 기준 왼쪽에서 큰 값과 피벗 기준 오른쪽에서 작은 값의 위치 바꿈
        if low < high:
            array[low], array[high] = array[high], array[low]

    # low와 high 위치가 바뀐 경우 high와 pivot의 위치를 바꾼다.
    array[left], array[high] = array[high], array[left]

    return high
