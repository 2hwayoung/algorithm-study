// title: 프로그래머스>기능개발
// link: https://programmers.co.kr/learn/courses/30/lessons/42586
// 분류: stack/queue

#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> periods;
    for (int i=0; i < progresses.size(); i++) {
        int period = ceil((double)(100 - progresses[i])/speeds[i]);
        periods.push_back(period);
        cout << period << " ";
    }
    vector<int> ::iterator iter = periods.begin();
    for (int i = 0; i < periods.size(); i++) {
        int count = 1;
        iter = periods.begin() + i;
        cout << i <<":" << periods.size()<<"\n";
        for (int j = i+1; j < periods.size(); j++) {
            iter ++;
            if (periods[j] <= periods[i]) {
                count ++;
                periods.erase(iter);
            }
        }
        periods.erase(periods.begin() + i);
        answer.push_back(count);
    }
    return answer;
}