
log_keys = ['team_name', 'application_name', 'error_level', 'message']

def isValid(log):
    # 로그의 길이가 100 이상이면 False
    if len(log) > 100:
        return False

    # 공백을 기준으로 나누었을 때 12개 구간이 생겨야 함
    tokens = log.split(' ')
    if len(tokens) != 12:
        return False

    for i in range(4):
        # 각 로그의 key : value 에서 key 가 유효하지 않은 경우 False
        if tokens[3 * i] != log_keys[i]:
            return False

        # key 와 value 가 ':'로 구분되어 있는지 체크
        if tokens[3 * i + 1] != ':':
            return False

        # 각 로그의 value 가 알파벳 소문자, 대문자로만 이루어져잇는지 체크
        if not tokens[3 * i + 2].isalpha():
            return False

    return True


def solution(logs):
    answer = 0
    for log in logs:
        if not isValid(log):
            answer += 1

    return answer