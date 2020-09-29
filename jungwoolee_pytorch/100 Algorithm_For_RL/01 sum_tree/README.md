# Sum Tree
* sum tree는 binary tree 구조로 sampling에 있어서 ![equation](https://latex.codecogs.com/gif.latex?%5Clog%20N) 을 보장한다.
* ex) 1,000,000 개의 데이터일경우 마지막 data를 단순 서치하면 1,000,000 인데, ![equation](https://latex.codecogs.com/gif.latex?%5Clog%201000000%20%3D%206)이다.
* 재밌는 특징으로 단순히 leaf node까지의 search만으로 확률적 특성이 반영된 sampling이 가능하다.
- - -

### 1. Initialize
* replay buffer와 sum tree를 표현할 Array를 0으로 초기화 해준다.
* replay buffer의 size는 buffer_size. 
* sum tree의 size는 (buffer_size * 2) - 1. ex) buffer_size = 8, sum_tree size = 16 - 1 = 15 = 총 node 수.

- - -

### 2. Add
* replay buffer의 시작 index는 0 이다.
* sum tree의 시작 index는 buffer_size - 1 이다. (첫번째 leaf node의 index)
* 만약 둘다 정해준 maximum size에 도달한다면, replay buffer는 0으로, sum tree는 buffer_size - 1의 위치로 다시 이동한다.
* 코드상에서 현재 위치를 기록하는 self.buffer_index와 self.tree_index에 해당하는 위치에 data와 priority를 각각 저장한다.

- - -

### 3. Update
* 
