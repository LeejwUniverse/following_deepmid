# Sum Tree

- - -

#### 1. Initialize
* replay buffer와 sum tree를 표현할 Array를 0으로 초기화 해준다.
* replay buffer의 size는 buffer_size. 
* sum tree의 size는 (buffer_size * 2) - 1. ex) buffer_size = 8, sum_tree size = 16 - 1 = 15 = 총 node 수.

- - -

#### 2. Add
* replay buffer의 시작 index는 0 이다.
* sum tree의 시작 index는 buffer_size - 1 이다. (첫번째 leaf node의 index)
* 만약 둘다 정해준 maximum size에 도달한다면, replay buffer는 0으로, sum tree는 buffer_size - 1의 위치로 다시 이동한다.
