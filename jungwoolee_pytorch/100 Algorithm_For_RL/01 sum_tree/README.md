# Sum Tree
* sum tree는 binary tree 구조로 sampling에 있어서 ![equation](https://latex.codecogs.com/gif.latex?%5Clog%20N) 을 보장한다.
* ex) 1,000,000 개의 데이터일경우 마지막 data를 단순 서치하면 1,000,000 인데, ![equation](https://latex.codecogs.com/gif.latex?%5Clog%201000000%20%3D%206)이다.
* 재밌는 특징으로 단순히 leaf node까지의 search만으로 확률적 특성이 반영된 sampling이 가능하다.
- - -

### 1. Initialize
* replay buffer와 sum tree를 표현할 Array를 0으로 초기화 해준다.
* replay buffer의 size는 buffer_size. 
* sum tree의 size는 (buffer_size * 2) - 1. ex) buffer_size = 8, sum_tree size = 16 - 1 = 15 = 총 node 수.
```python
self.replay_buffer = [0 for i in range(buffer_size)] # set rplay buffer size.
self.array_tree = [0 for i in range((buffer_size * 2) - 1)] # set sum_tree size (double of buffer size)
```
<p align="center">
    <img src="/images/1_init_01.PNG" width="400">
    <img src="/images/1_init_02.PNG" width="400">
</p>

- - -

### 2. Add
* replay buffer의 시작 index는 0 이다.
* sum tree의 시작 index는 buffer_size - 1 이다. (첫번째 leaf node의 index)
```python
self.tree_index = buffer_size - 1 # define sum_tree leaf node index.
self.buffer_index = 0 # define replay buffer index.
```
* 만약 둘다 정해준 maximum size에 도달한다면, replay buffer는 0으로, sum tree는 buffer_size - 1의 위치로 다시 이동한다.
```python
if self.tree_index == (self.buffer_size * 2) - 1: # if sum tree index achive last index.
    self.tree_index = self.buffer_size - 1 # change frist leaf node index.
if self.buffer_index == self.buffer_size: # if replay buffer index achive last index.
    self.buffer_index = 0 # change first index (0 zero)
```
* 코드상에서 현재 위치를 기록하는 self.buffer_index와 self.tree_index에 해당하는 위치에 data와 priority를 각각 저장한다.
```python
self.replay_buffer[self.buffer_index] = data # append data at current replay buffer index.
self.array_tree[self.tree_index] = priority # append priority at current sum_tree leaf node index.

```

- - -

### 3. Update
* Add에서 새로운 data가 추가되면, sum tree의 leaf node중 변경된 leaf node로 부터 root까지 sum tree의 node들을 update해줘야 한다.
* leaf node의 parent node는 parent node = left node + right node의 수식으로 update 된다.
* root에 도달하면 종료된다. 여기서는 tree index가 0가 된다면 종료된다.

- - -

### 4. Search
* uniform distribution에서 선택된 value들을 바탕으로 leaf node가 가진 구간 범위(확률 값이다.)에 따라 sampling 된다.
* 이 코드의 예제에 따르면, 7,8번 node가 가진 5는 [0,1,2,3,4,5] [6,7,8,9,10]이 선택될 수 있다. (uniform의 범위 (0,99))
* 각각 6%, 5% 정도의 선택확률을 표현하는 예제이다. 전체 100개가 1번씩 무조건 나온다는 가정이므로, 위 0 ~ 10의 숫자가 나올 경우만 선택된다.
* uniform distribution에서 선택된 input 값은 아래 규칙에 의해 탐색을 한다.
* 1. 왼쪽 자식 node가 input보다 크거나 같다면, input 값 그대로 왼쪽 자식 node로 이동.
* 2. 왼쪽 자식 node가 input보다 작다면, input = input - left node 한 후, 오른쪽 자식 node로 이동.
* 3. leaf node에 도착한다면, 탐색 종료 후 해당하는 index 반환.
```python
index = 0 # always start from root index.
while True:
    left = (index * 2) + 1
    right = (index * 2) + 2
    if num <= self.array_tree[left]: # if child left node is over current value. 
        index = left                # go to the left direction.
    else:
        num -= self.array_tree[left] # if child left node is under current value.
        index = right               # go to the right direction.
    if index >= self.buffer_size - 1: # if current node is leaf node, break!
        break
```

