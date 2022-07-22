### Deque
```
deque.rotate(-1) 음수이면 왼쪽으로 회전
```
### Counter
```
from collections import Counter

Counter(arr) 값, 빈도 딕셔너리

Counter('hello world').most_common() # [('l', 3), ('o', 2) ](값,빈도) 튜플 내림차순

Counter(arr).most_common(2) 가장 숫자가 많은 2개의 값들 
```
### 배열 속 원소 갯수
```
list.count(1) 
```
### 아스킷코드 변환
```
a=ord(A) # 문자 -> 아스킷 
chr(a) # 아스킷 -> 문자
```
## 출력
### 정수배열 고대로 출력
```
#given
arr = [1,2,3,4]

#when
print(*arr)

#then
1 2 3 4
```
### 문자열 거꾸로 만들기
```
#given
arr = "ABCD"

#when
1. arr.reverse()
2. inverse = arr[::-1]

#then
"DBCA"
```
### 입력
```
#given
1 2 3 4 5 6 이 들어올때

#when
N, *arr = map(int, input().split())

#then
N == 1
arr == [2,3,4,5,6]
```
### 정렬
```
new.sort(key=lambda x: len(x))
이렇게 하면 new가 직접 바뀜
내림차순 하고 싶으면 -len(x) 하면 됨
```

### strip 
```
strip("})하면 2개 지워진다
```
## 집합 연산

### 같은지 확인
```
set(a) == set(b)
```
### 합집합
```
a | b
```
### 차집합
```
a & b
```
### 차집합
```
a - b
```


### 

### 종복조합
 
```
from itertools import combinations_with_replacement
```

### 힙큐 - 오름차순

```
import heapq
arr=[]
heapq.heappush(arr, item) : item을 heap에 추가
heapq.heappop(arr) : 가장 작은 원소 pop 비어 있는 경우 IndexError가 호출됨.

arr=[1,3,6,4]
heapq.heapify(arr)
heapq.heappush(arr, item)
```

내림차순은 -item을 넣는다

## 리스트
###  거꾸로 - 124나라의 숫자
```
reversed(list)
```
