# Algorithm/DataStructure

파이썬 알고리즘/자료구조 공부

- 문제 출처: programmers, baekjoon
- 사용 언어: python, c++
- 난이도 기준: level 0 ~ 5 or 백준 [solved.ac](https://solved.ac/)

#

#### 기본 수학 & 구현

|                                제목                                |                  풀이                  |  난이도  | 한줄                                  |
| :----------------------------------------------------------------: | :------------------------------------: | :------: | :------------------------------------ |
| [2016년](https://programmers.co.kr/learn/courses/30/lessons/12901) |       [c++](기본수학/2016년.cpp)       | level 1  | .                                     |
|         [사칙연산](https://www.acmicpc.net/problem/10869)          |      [c++](기본수학/사칙연산.cpp)      | 브론즈 V | 표준 입력 함수 cin은 공백을 무시한다. |
|             [합](https://www.acmicpc.net/problem/8393)             |         [c++](기본수학/합.cpp)         | 브론즈 V | .                                     |
|  (!)[최대공약수 하나 빼기](https://www.acmicpc.net/problem/14476)  | [c++](기본수학/최대공약수하나빼기.cpp) | 골드 II  | .                                     |

#

#### 문자열

[파이썬 문자열 처리 바로가기](문자열/파이썬%20문자열%20처리.md)

|                                             제목                                              |                      풀이                       |  난이도  | 한줄                                                                                                   |
| :-------------------------------------------------------------------------------------------: | :---------------------------------------------: | :------: | :----------------------------------------------------------------------------------------------------- |
|           [문자열다루기](https://programmers.co.kr/learn/courses/30/lessons/12918)            |         [c++](문자열/문자열다루기.cpp)          | level 1  | char를 int로 바꿀때 -'0'해야 한다.                                                                     |
|               [튜플](https://programmers.co.kr/learn/courses/30/lessons/64065#)               |             [c++](문자열/튜플.cpp)              | level 2  | endl보다 '\n'으로 쓰는게 좋고, set은 중복값을 제외하고 자동 정렬해준다.                                |
|               [압축](https://programmers.co.kr/learn/courses/30/lessons/17684)                |             [c++](문자열/압축.cpp)              | level 2  | string(1, 'A'+i) // char -> string 변환                                                                |
|                    [싸이버개강총회](https://www.acmicpc.net/problem/19583)                    |        [python](문자열/싸이버개강총회py)        |  실버 I  | dict에서 특정 key에 대한 value를 찾을 때 get() 메서드를 사용해야 not exist 경우 해결가능 (None return) |
|                         [HTML](https://www.acmicpc.net/problem/6581)                          |            [python](문자열/HTML.py)             |  실버 I  | split()는 한 개 이상의 공백문자/탭/개행문자 모두 포함                                                  |
|                      [문자열 폭발](https://www.acmicpc.net/problem/9935)                      |         [python](문자열/문자열폭발.py)          | 골드 IV  | list에서 인덱스를 뒤에서부터 읽는 것도 유용, 문자열 수가 커서 스택 사용해야 제한시간안에 성공가능      |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [python](문자열/LongestPalindromicSubstring.py) |  Medium  | dynamic programming 사용, 항상 문자 한 개부터 palindromic에 해당된다는 사실에서부터 시작한다           |
|                      [개](https://www.acmicpc.net/submit/10172/37850595)                      |          [python](문자열/10172_개.py)           | 브론드 V | 생각보다 어렵다.                                                                                       |

#

### Algorithm (알고리즘)

[C++ Tips 바로가기](알고리즘/C++Tips.md)

#### Sort (정렬)

|                                       제목                                       |                 풀이                  |   난이도    | 한줄                                                                          |
| :------------------------------------------------------------------------------: | :-----------------------------------: | :---------: | :---------------------------------------------------------------------------- |
| [K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748?language=cpp) |   [c++](알고리즘/sort/k번째수.cpp)    |   level 1   | sort()는 <algorithm> 헤더파일에 속해있다.                                     |
|       [가장큰수](https://programmers.co.kr/learn/courses/30/lessons/42746)       |   [c++](알고리즘/sort/가장큰수.cpp)   |   level 1   | sort()는 세번째 인자(함수)를 기준으로 정렬가능하다.                           |
|             (!)[후보 추천하기](https://www.acmicpc.net/problem/1713)             | [c++](알고리즘/sort/후보추천하기.cpp) |   실버 I    | 여러 vector에서 하나의 객체를 참조할 때 포인터를 신중히 써야 한다. 공부 필요! |
|                (!)[달리기](https://www.acmicpc.net/problem/2517)                 |    [c++](알고리즘/sort/달리기.cpp)    | 플래티넘 VI | inversion count 개념알게됨                                                    |

#

#### Search (탐색)

|     분류      |                                                     제목                                                      |                    풀이                    | 난이도   | 한줄                                                     |
| :-----------: | :-----------------------------------------------------------------------------------------------------------: | :----------------------------------------: | :------- | -------------------------------------------------------- |
| binary search |                                 [게임](https://www.acmicpc.net/problem/1072)                                  |      [c++](알고리즘/search/게임.cpp)       | 실버 III | .                                                        |
| binary search |                              [나무자르기](https://www.acmicpc.net/problem/2805)                               |   [c++](알고리즘/search/나무자르기.cpp)    | 실버 III | .                                                        |
| binary search |                                [수 찾기](https://www.acmicpc.net/problem/1920)                                |     [c++](알고리즘/search/수찾기.cpp)      | 실버 IV  | .                                                        |
| binary search |                            (!)[두 배열의 합](https://www.acmicpc.net/problem/2143)                            |   [c++](알고리즘/search/두배열의합.cpp)    | 골드 III | 오름차순, 내림차순 정렬 모두 필요                        |
|      DFS      |                     [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)                     |    [c++](알고리즘/search/타겟넘버.cpp)     | level 2  | 함수의 파라미터에 저장되는 값은 &가 아닌 이상 value이다. |
|      DFS      |                                                  Road Repair                                                  | [c++](알고리즘/search_탐색/RoadRepair.cpp) | basic    | sort함수로 먼저 정렬해주었다.                            |
|      DFS      |                     [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)                      |    [c++](알고리즘/search/네트워크.cpp)     | level 3  | .                                                        |
|      DFS      |                     [단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)                     |    [c++](알고리즘/search/단어변환.cpp)     | level 3  | .                                                        |
|      DFS      |                                [가르침](https://www.acmicpc.net/problem/1062)                                 |     [c++](알고리즘/search/가르침.cpp)      | 골드 IV  | .                                                        |
|      BFS      | (!)[나잡아봐라](https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/) |   [c++](알고리즘/search/나잡아봐라.cpp)    | .        | 2019 상반기 LINE 인턴 코딩테스트 문제                    |
|   완전탐색    |                              [감소하는수](https://www.acmicpc.net/problem/1038)                               |   [c++](알고리즘/search/감소하는수.cpp)    | 골드 V   | 어떻게 재귀함수를 쓰는가에 따른 자동 sort                |

#

#### DP (동적프로그래밍)

|                                  제목                                  |               풀이               | 난이도  | 한줄       |
| :--------------------------------------------------------------------: | :------------------------------: | :-----: | :--------- |
| [3xn 타일링](https://programmers.co.kr/learn/courses/30/lessons/12902) | [c++](알고리즘/dp/3xn타일링.cpp) | level 2 | 간단한 dp! |

#

### Data Structure (자료구조)

#### Hash (해시)

|                                      제목                                      |                   풀이                    | 난이도  | 한줄                                                                         |
| :----------------------------------------------------------------------------: | :---------------------------------------: | :-----: | :--------------------------------------------------------------------------- |
| [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) | [c++](자료구조/hash/완주하지못한선수.cpp) | level 1 | c++11부터 vector<pair<,>>와 map은 비슷하나 요소 추가 방식에서 차이가 있는 듯 |

#

#### Stack (스택)

|                                  제목                                  |                 풀이                 | 난이도  | 한줄                                               |
| :--------------------------------------------------------------------: | :----------------------------------: | :-----: | :------------------------------------------------- |
|             [고스택](https://www.acmicpc.net/problem/3425)             |   [c++](자료구조/stack/고스택.cpp)   | 골드 II | 10e9를 넘어가는 사칙연산이 존재하면 long long 사용 |
| [올바른괄호](https://programmers.co.kr/learn/courses/30/lessons/12909) | [c++](자료구조/stack/올바른괄호.cpp) | level 2 | .                                                  |
|                                                                        |                                      |         |                                                    |

#

#### Queue (큐)

|                                 제목                                 |                풀이                | 난이도  | 한줄 |
| :------------------------------------------------------------------: | :--------------------------------: | :-----: | :--- |
| [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584) | [c++](자료구조/queue/주식가격.cpp) | level 2 | .    |
| [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586) | [c++](자료구조/queue/기능개발.cpp) | level 2 | .    |
|  [프린터](https://programmers.co.kr/learn/courses/30/lessons/42587)  |  [c++](자료구조/queue/프린터.cpp)  | level 2 | .    |

#

#### Heap (힙)

|                                제목                                 |              풀이               | 난이도  | 한줄                                        |
| :-----------------------------------------------------------------: | :-----------------------------: | :-----: | :------------------------------------------ |
| [더 맵게](https://programmers.co.kr/learn/courses/30/lessons/42626) | [c++](자료구조/heap/더맵게.cpp) | level 2 | 우선순위큐는 데이터를 넣으면 자동 정렬된다. |
