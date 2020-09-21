# 알고리즘 스터디

- 참가자: [Jinho Lee](https://github.com/justzino), [Minjeong Jeon](https://github.com/ummjevel)
- 커리큘럼: [백준](https://code.plus/course/41), [블로그](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0) 문제
- 제출방법: GitHub 이용. 메인 Repository, 각자 Branch 생성
- 모임: 주 2회(월, 금 오후 2시)
- 패널티:  
불참 - 1000원 (이유 불문- 교통사고 나도 지불)  
문제당 - 100원
- 리뷰: 모임 때... 
- 회고: 각자

## 기초알고리즘
쉬운 것도 무시하지 말고 기초부터 다시.

### 1 회차
- 기한: 8/3(월) ~ 8/10(월) 
- 진도: [입출력](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
- 입출력 : 2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992

### 2 회차
- 기한: 8/10(월) ~ 8/17(월)
- 진도 : [자료구조1](https://code.plus/course/41)
- 자료구조1 : 10828, 9093, 9012, 1874, 1406, 10845, 1158, 10866, 17413, 10799

### 3 회차
- 기한: 8/17(월) ~ 8/24(월)
- 진도 : [자료구조1](https://code.plus/course/41)
- 자료구조 : 17298, 17299, 1935, 1918, 10808, 10809, 10820, 2743, 11655, 10824, 11656

### 4 회차
- 기한: 8/24(월) ~ 8/31(월)
- 진도 : [수학1](https://code.plus/course/41)
- 수학1 : 10430, 2609, 1978, 6588, 10872, 1676, 2004, 9613, 17087, 1373, 1212, 2089, 17103, 11005, 2745, 11576, 1463

### 5 회차
- 기한: 8/31(월) ~ 9/7(월)
- 진도 : [DP1](https://code.plus/course/41)
- DP1 : 1463, 11726, 11727, 9095, 11052, 16194, 15990, 10844, 2193, 11053, 14002, 1912, 1699, 2225, 15988 

### 6 회차
- 기한: 9/7(월) ~ 9/21(월)
- 진도 : [DP1](https://code.plus/course/41)
- dp1 : 1149, 1309, 9465, 2156 

### 7 회차
- 기한: 9/21(월) ~ 9/28(월)
- 진도 : [DP1](https://code.plus/course/41)
- dp1 : 1932, 11055, 11722, 11054, 13398, 2133, 1309, 17404, 2225


#### 협업용 깃헙 정리
[협업 과정](https://gmlwjd9405.github.io/2018/05/12/how-to-collaborate-on-GitHub-3.html), [오리지널 저장소의 변경 내역 최신화 하기 - fetch, pull, merge](https://playinlion.tistory.com/29),
 [참고](http://www.notforme.kr/archives/1631), [원격 저장소 branch 확인](https://junwoo45.github.io/2019-07-16-git_remote_branch/)
1. upstream 에 대한 이해
- $ git remote add upstream [https://github.com/ummjevel/algorithm.git] : upstream [주소] remote
- $ git branch -r : -r 붙이면 원격 저장소의 branch list 확인
- $ git remote -v
- $ git fetch upstream : upstream 저장소에 있는 변경사항들을 로컬로 가져오면서 새로운 branch 생성
- $ git checkout [master] : [내 브랜치] 로 현재 가리키는 branch 업데이트
- $ git merge [upstream/master] : [upstream/branch]를 내 현재 branch 로 merge
- $ git push [origin] [master] : 내 원격 repo로 push 해주면 끝

2. PR (Pull Request)
- 이렇게 upstream repository 와 동기화 한 내 레포를 upstream 레포로 PR을 보냄
- upstream에서 conflict가 없을시 PR 승인
- 다른 협업자들은 본인의 변경사항으로 PR하기 전에 다시 1.의 과정을 통해 본인의 레포를 upstream의 레포와 동기화 한후 PR
 