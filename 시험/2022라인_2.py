
from collections import defaultdict


def solution(sentences, n):
    history = list()
    sentences_scores = []
    history_scores = list()
    needs = defaultdict(int)
    for sentence in sentences:
        score = len(sentence)
        sentence = sentence.replace(" ", "")
        alpha_set = list(set(sentence))
        
        # n보다 필요한 키의 수가 크면 생략
        if len(alpha_set) > n:
            continue
        
        for i in range(len(alpha_set)):
            if alpha_set[i].isupper():
                alpha_set.append('shift')
                score += 1
            alpha_set[i] = alpha_set[i].lower()

        # 현재 문자열의 점수
        sentences_scores.append(score)

        key = frozenset(alpha_set) 
        for needs_key in needs.keys():
            if needs_key & key == key:
                needs[needs_key] += score
                print("a", key, needs_key, needs[needs_key])
                break
            elif needs_key & key == needs_key:
                needs[key] += score
                needs[key] += needs[needs_key]
                print("b", needs_key, key, needs[key])
                del needs[needs_key]
                break
        else:
            needs[key] += score
    #     # 필요한 키와 그에 대한 총 점수 계산
    #     if set(alpha_set) not in history:
    #         history.append(set(alpha_set))
    #         history_scores.append(score)
    #     else:
    #         history_scores[history.index(set(alpha_set))] += score

    # max_key_set_index = 0
    # for i in range(len(history)):
        
    return max([v for k, v in needs.items()])

print(solution(["line in line", "LINE", "in lion"], 5))
