# Dijkstra 최단 경로 알고리즘
- **특정 노드**에서 출발 -> **다른 노드**로 가는 각각의 최단 경로를 구해주는 알고리즘
- '음의 간선' 이 없을 때 정상적으로 동작
- Greedy + DP : '가장 비용이 적은 노드'를 선택해서 임의의 과정을 반복 + '비용을 기록'
    1. 출발 노드를 설정한다.
    2. 최단 거리 테이블을 초기화 한다.
    3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
    5. 위 과정에서 3과 4번을 반복한다.

  
## 방법 1. 우선순위 큐 사용 - 중요
- 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
- 최단 거리 탐색에 우선순위 큐 사용
- V: Vertex(노드의 개수), E: Edge(간선의 개수)
- 시간 복잡도: O(E logV)
  - 최단 거리 탐색 - 우선순위 큐 사용 : O(logV)
  - 현재 노드와 연결된 노드를 매번 일일이 확인 : O(E)
- [구현 코드](This-is-Coding-Test-Book/Shortest-Path/Dijkstra1.py)



## 방법 2. 선형 탐색 사용
- 구현하기 쉽지만 느리게 동작하는 코드
- 최단 거리 탐색에 선형 탐색 사용
- 시간 복잡도: O(V^2) 
  - 최단 거리 탐색 - 선형 탐색 : O(V)
  - 현재 노드와 연결된 노드를 매번 일일이 확인 : O(V)
- [구현 코드](This-is-Coding-Test-Book/Shortest-Path/Dijkstra2.py)

# Floyd-Warshall 알고리즘
- **모든 지점**에서 **다른 모든 지점**까지의 최단 경로를 모두 구해야 하는 경우
- **2차원 리스트**에 '최단 거리' 정보를 저장 (DP)
- 노드의 개수: N개 일 때 시간 복잡도: O(N^3)
  - N번의 단계: O(N)
  - 현재 노드를 거쳐가는 모든 경로 고려 : O(N^2)
- [구현 코드](This-is-Coding-Test-Book/Shortest-Path/Floyd-Warshall.py)

  