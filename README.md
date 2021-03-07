# Algorithm/DataStructure

파이썬 알고리즘/자료구조 공부

- 문제 출처: programmers, baekjoon
- 사용 언어: python, c++
- 난이도 기준: level 0 ~ 5 or 백준 [solved.ac](https://solved.ac/)

#

### 0. 기본 수학

|                       제목                        |                   풀이                   |  난이도   | 포인트                                |
| :-----------------------------------------------: | :--------------------------------------: | :-------: | :------------------------------------ |
| [2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)  | [c++](알고리즘/기본수학/2016년.cpp) | level 1 | .                   |
| [사칙연산](https://www.acmicpc.net/problem/10869) |     [c++](1_기본수학/1_사칙연산.cpp)     | 브론즈 V | 표준 입력 함수 cin은 공백을 무시한다. |
|    [합](https://www.acmicpc.net/problem/8393)     | [c++](./2_sort_정렬/2_sort_가장큰수.cpp) | 브론즈 V | .                                     |
#

### 1. 문자열
|                       제목                        |                   풀이                   |  난이도   | 포인트                                |
| :-----------------------------------------------: | :--------------------------------------: | :-------: | :------------------------------------ |
| [문자열다루기](https://programmers.co.kr/learn/courses/30/lessons/12918) |     [c++](알고리즘/문자열/문자열다루기.cpp)     | level 1 | char를 int로 바꿀때 -'0'해야 한다. |
| [튜플](https://programmers.co.kr/learn/courses/30/lessons/64065#) |     [c++](알고리즘/문자열/튜플.cpp)     | level 2 | endl보다 '\n'으로 쓰는게 좋고, set은 중복값을 제외하고 자동 정렬해준다. |
| [압축](https://programmers.co.kr/learn/courses/30/lessons/17684) |     [c++](알고리즘/문자열/압축.cpp)     | level 2 | string(1, 'A'+i) // char -> string 변환 |

#

## Algorithm (알고리즘)

### 1. Sort (정렬)

|                             제목                             |                  풀이                  | 난이도 | 포인트                                              |
| :----------------------------------------------------------: | :------------------------------------: | :----: | :-------------------------------------------------- |
| [K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748?language=cpp) | [c++](2_sort_정렬/1_sort_k번째수.cpp)  |  level 1  | sort()는 <algorithm> 헤더파일에 속해있다.           |
| [가장큰수](https://programmers.co.kr/learn/courses/30/lessons/42746) | [c++](2_sort_정렬/2_sort_가장큰수.cpp) |  level 1  | sort()는 세번째 인자(함수)를 기준으로 정렬가능하다. |
| [후보 추천하기](https://www.acmicpc.net/problem/1713) | [c++](알고리즘/1_알고리즘_기초/후보추천하기.cpp) | 실버 I |여러 vector에서 하나의 객체를 참조할 때 포인터를 신중히 써야 한다. 공부 필요! |

#

### 2. Search (탐색)

|           분류            |                        제목                        |                    풀이                     | 난이도   | 포인트 |
| :-----------------------: | :------------------------------------------------: | :-----------------------------------------: | :------- | ------ |
| binary search (이분 탐색) |    [게임](https://www.acmicpc.net/problem/1072)    |    [c++](알고리즘/2_시간복잡도/게임.cpp)    | 실버 III | .      |
| binary search (이분 탐색) | [나무자르기](https://www.acmicpc.net/problem/2805) | [c++](알고리즘/2_시간복잡도/나무자르기.cpp) | 실버 III | .      |
| binary search (이분 탐색) | [수 찾기](https://www.acmicpc.net/problem/1920) | [c++](알고리즘/2_시간복잡도/수찾기.cpp) | 실버 IV | . |
| DFS (깊이우선탐색) | [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165) | [c++](알고리즘/search_탐색/타겟넘버.cpp) | level 2| 함수의 파라미터에 저장되는 값은 &가 아닌 이상 value이다. |  
| DFS (깊이우선탐색) | Road Repair | [c++](알고리즘/search_탐색/RoadRepair.cpp) | basic | sort함수로 먼저 정렬해주었다. |  
| DFS (깊이우선탐색) | [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162) | [c++](알고리즘/search_탐색/네트워크.cpp) | level 3| .|  
| DFS (깊이우선탐색) | [단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163) | [c++](알고리즘/search_탐색/단어변환.cpp) | level 3| .|  
| DFS (깊이우선탐색) | [가르침](https://www.acmicpc.net/problem/1062) | [c++](알고리즘/1_알고리즘_기초/가르침.cpp) | 골드 IV| . |  


#

### 3. dp (동적프로그래밍)

|                             제목                             |                  풀이                  | 난이도 | 포인트                                              |
| :----------------------------------------------------------: | :------------------------------------: | :----: | :-------------------------------------------------- |
| [3xn 타일링](https://programmers.co.kr/learn/courses/30/lessons/12902) | [c++](알고리즘/dp_동적프로그래밍/3xn타일링.cpp)  |  level 2  | 간단한 dp!        |

#

## Data Structure (자료구조)

### Hash (해시)

|                      제목                      |                    풀이                    | 난이도  | 포인트                                             |
| :--------------------------------------------: | :----------------------------------------: | :-----: | :------------------------------------------------- |
| [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) | [c++](자료구조/hash_해시/완주하지못한선수.cpp) | level 1 | c++11부터 vector<pair<,>>와 map은 비슷하나 요소 추가 방식에서 차이가 있는 듯 |


### Stack (스택)

|                      제목                      |                    풀이                    | 난이도  | 포인트                                             |
| :--------------------------------------------: | :----------------------------------------: | :-----: | :------------------------------------------------- |
| [고스택](https://www.acmicpc.net/problem/3425) | [c++](알고리즘/1_알고리즘_기초/고스택.cpp) | 골드 II | 10e9를 넘어가는 사칙연산이 존재하면 long long 사용 |
| [올바른괄호](https://programmers.co.kr/learn/courses/30/lessons/12909) | [c++](자료구조/stack_스택/올바른괄호.cpp) | level 2 | . |
|  |   |   |  | 


### Queue (큐)
|                      제목                      |                    풀이                    | 난이도  | 포인트                                             |
| :--------------------------------------------: | :----------------------------------------: | :-----: | :------------------------------------------------- |
| [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584) | [c++](자료구조/queue_큐/주식가격.cpp) | level 2 | . |
| [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586) | [c++](자료구조/queue_큐/기능개발.cpp) | level 2 | . |
| [프린터](https://programmers.co.kr/learn/courses/30/lessons/42587) | [c++](자료구조/queue_큐/프린터.cpp) | level 2 | . |