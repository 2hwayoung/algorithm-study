// link: https://programmers.co.kr/learn/courses/30/lessons/43165
// 분류: 깊이 우선 탐색

#include <string>
#include <vector>

using namespace std;
int depth, sum, count;

void dfs(vector<int> numbers, int target, int depth, int sum) {
    // 마지막 숫자에 도달했을 때
    if (depth == numbers.size()) {
        if (target == sum) count++;
        return;
    }

    dfs(numbers, target, depth+1, sum + numbers[depth]);
    dfs(numbers, target, depth+1, sum - numbers[depth]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    depth = 0;
    sum = 0;
    count = 0;
    dfs(numbers, target, depth, sum);
    answer = count;
    return answer;
}