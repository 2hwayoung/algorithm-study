
def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    step_dict = {}
    
    for i in range(len(names_one)):
        step_dict[names_one[i]] = [steps_one[i]]
    for i in range(len(names_two)):
        if not names_two[i] in step_dict:
            step_dict[names_two[i]] = [0]
        step_dict[names_two[i]].append(steps_two[i])
    for i in range(len(names_three)):
        if not names_three[i] in step_dict:
            step_dict[names_three[i]] = [0,0]
        elif len(step_dict[names_three[i]]) == 1:
            step_dict[names_three[i]].append(0)
        step_dict[names_three[i]].append(steps_three[i])
    
    sortedList = sorted(step_dict.items(), key = lambda item: (sum(item[1]), item[0]), reverse = True)
    answer = []
    for item in sortedList:
        answer.append(item[0])
    return answer