// title: 프로그래머스>기능개발
// link: https://programmers.co.kr/learn/courses/30/lessons/42586
// 분류: stack/queue

#include <string>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> periods;
    queue<int> q;

    for (int i=0; i < progresses.size(); i++) {
        int period = ceil((double)(100 - progresses[i])/speeds[i]);
        periods.push_back(period);
    }
    
    q.push(periods.front());

    for (int i = 1; i < periods.size(); i++) {
        if (q.front() < periods[i]) {
            answer.push_back(q.size());
            while (!q.empty()) q.pop();
            q.push(periods[i]);
        } else {
            q.push(periods[i]);
        }
    }

    if (!q.empty()) {
        answer.push_back(q.size());
    }
    return answer;
}