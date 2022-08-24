
# 재택근무 하는 사원 번호 리스트 
def solution(num_teams, remote_tasks, office_tasks, employees):
    
    employee_remotes = list()
    team_employees = [[] for _ in range((num_teams) + 1)]
    for i in range(len(employees)):
        infos = employees[i].split()
        team_employees[int(infos[0])].append(i+1)

        num_info = len(infos[1:])
        for info in infos[1:]:
            if info in remote_tasks:
                num_info -= 1
        if num_info == 0:
            employee_remotes.append(i+1)
    
    for team in team_employees:
        num_employee_in_team = len(team)
        if num_employee_in_team == 0:
            continue
        for employee in team:
            if employee in employee_remotes:
                num_employee_in_team -= 1
        if num_employee_in_team == 0:
            employee_remotes.remove(team[0])

    return employee_remotes


print(solution(3, ["development","marketing","hometask"], ["recruitment","education","officetask"], 
["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))