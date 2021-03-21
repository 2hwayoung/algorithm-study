// link: https://programmers.co.kr/learn/courses/30/lessons/43162
// 분류: 탐색/깊이우선탐색

#include <string>
#include <vector>

using namespace std;

void dfs(int computer, vector<vector<int>>& computers, vector<bool>& visited, int n) {
    visited[computer] = true;

    for (int i=0; i<n; i++) {
        if (!visited[i] && computers[computer][i]) dfs(i, computers, visited, n);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);

    for (int i=0; i<n; i++) {
        if (!visited[i]) {
            answer++;
            dfs(i, computers, visited, n);
        }
    }

    return answer;
}