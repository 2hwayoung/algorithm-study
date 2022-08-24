from collections import defaultdict

def solution(survey, choices):
    types = defaultdict(int)
    ## RT, CF, JM, AN
    # 점수 높은 순, 같다면 사전 순
    for i in range(len(survey)):
        score = abs(choices[i] - 4)
        selectedType = survey[i][0] if choices[i] < 4 else survey[i][1]
        types[selectedType] += score

    answer = ''
    answer += 'R' if types['R'] >= types['T'] else 'T'
    answer += 'C' if types['C'] >= types['F'] else 'F'
    answer += 'J' if types['J'] >= types['M'] else 'M'
    answer += 'A' if types['A'] >= types['N'] else 'N'
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5,3,2,7,5]))
print(solution(["TR", "RT", "TR"], 	[7, 1, 3]))