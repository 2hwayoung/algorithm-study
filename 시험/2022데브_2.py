# 행, 열  9 이하
# ? 9개 이하
# 목표 : 각 알파벳은 상하좌우로 연결
# a, b, c 가 전부

def solution(grid):
    # a, b, c가 모두 있는지 확인하고 없으면 available_alphas에 추가한다.
    # 그리드에서 ?를 차례대로 찾는다
    # ?의 상하좌우를 검색하여 인접한 알파벳이 존재하면 able_list에 추가하고 available_alphas도 추가한다.
    # 그리고 able_list를 for문으로 돌면서 
    answer = -1
    return answer



print(solution(["??b", "abc", "cc?"])) # result : 2
print(solution(["abcabcab","????????"])) # result : 0
print(solution(["aa?"])) # result : 3

 ?1 ?2 b
 a b c
 c c ?3 

 ?1의 후보 : a, b, c
 ?2의 후보 : 