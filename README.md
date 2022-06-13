### 정렬
```
new.sort(key=lambda x: len(x))
이렇게 하면 new가 직접 바뀜
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

### 우선순위 큐 - 오름차순

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
