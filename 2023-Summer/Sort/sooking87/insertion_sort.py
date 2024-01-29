def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # key 값 바로 앞부터 인덱스 0까지 중 key가 들어갈 자리 찾기

        while j >= 0 and arr[j] >= key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
