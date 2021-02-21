// link: https://programmers.co.kr/learn/courses/30/lessons/43163
// 분류: 탐색/DFS

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;

    bool exist = false;
    for (int i=0; i < words.size(); i++) {
        if (target == words[i]) {
            exist = true;
            break;
        }
    }
    if (!exist) return 0;

    queue <pair <string, int>> q;
    vector<bool> visited(words.size(), false);

    q.push(make_pair(begin, 0));

    while (!q.empty()) {
        string word = q.front().first;
        int num = q.front().second;

        if (word.compare(target) == 0) {
            answer = num;
            break;
        }
        q.pop();
        int count;
        for (int i=0; i<words.size(); i++) {
            if (visited[i]) continue;

            count = 0;
            
            for (int j=0;j<word.size();j++) {
                if (word[j] != words[i][j]) count++;
            }

            if (count == 1) {
                visited[i] = true;
                q.push(make_pair(words[i], num +1));
            }
        }
    }

    return answer;
}