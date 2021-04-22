# 복습

## Graph

- Node + Edge인 자료구조
- 서로 다른 개체(object)가 연결되어 있다 -> 가장 먼저 Graph 알고리즘 생각

## Tree

- Graph 자료구조 중 하나
- Dijkstra -> Priority Queue 이용 -> Min Heap / Max Heap 이용
  - Min Heap: 항상 부모노드가 자식 노드보다 작은 트리 자료 구조

## Graph vs Tree

|                    |         Graph         |       Tree       |
| :----------------: | :-------------------: | :--------------: |
|       방향성        |   방향 or 무방향 그래프  |    방향 그래프     |
|   순환성 (Cycle)    |     순환 및 비순환      |       비순환       |
|  루트 노드 존재 여부  |     루트 노드가 없음    |   루트 노드가 존재   |
|     노드간 관계성    |   부모와 자식 관계 없음   |  부모와 자식 관계   |
|      모델의 종류     |      네트워크 모델      |      계층 모델     |


## Graph 구현 방법

1. 인접 행렬 (Adjacency Matrix)
   - 2차원 배열 사용
2. 인접 리스트 (Adjacency List)
   - 리스트를 사용
- [구현 코드](This-is-Coding-Test-Book/DFS-BFS/Adjacency.py)

|                       | 인접 행렬 (Adjacency Matrix) | 인접 리스트 (Adjacency List) |
| :-------------------: | :-------------------------: | :------------------------: |
|          구현          |        2차원 배열 사용        |      1차원 리스트 사용       |
|       공간 복잡도       |            O(V^2)           |            O(E)            |
|   간선의 비용 검색 시간   |            O(1)             |            O(V)            |
|       사용 알고리즘      |         플로이드 워셜         |      다익스트라 알고리즘      |

# 그 외 그래프 알고리즘

## 서로소 집합 자료구조 (Disjoint Sets)
- 공통 원소가 없는 두 집합
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- Union & Find 연산
- 트리 자료구조를 이용하여 집합 표현
- 노드의 개수: V, find() or union() 개수: M
    - [구현 코드1](This-is-Coding-Test-Book/Graph/Disjoint-Set1.py) - O(VM)
    - [구현 코드2 - 경로 압축 기법](This-is-Coding-Test-Book/Graph/Disjoint-Set2.py) - 약 O(V + M logV)

## 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.
- cf. 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.

### Process
1. 각 edge 를 확인하며, 두 node 의 root node 를 확인한다.
    1. root node 가 서로 다르면 -> Union
    2. root node 가 서로 같으면 -> Cycle 발생!!
2. Graph 에 포함되어 있는 **모든 edge 에 대하여** 1번 과정을 반복

- [구현 코드](This-is-Coding-Test-Book/Graph/Cycle-Judge.py)
