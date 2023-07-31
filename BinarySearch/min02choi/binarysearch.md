## 이진 탐색
* 이진 탐색의 시간 복잡도: O(log2n)
* 정렬된 리스트에 대해서, 특정 수를 탐색하는 경우 검색의 범위를 반으로 줄여가면서 탐색을 진행

### 이진 탐색 코드
~~~python
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:     # 탐색 성공
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None     # 탐색 실패
~~~
