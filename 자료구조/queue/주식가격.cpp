// title: 프로그래머스>주식가격
// link: https://programmers.co.kr/learn/courses/30/lessons/42584
// 분류: stack/queue

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    for (int i = 0; i < prices.size(); i++) {
        int period = 0;
        for (int j=i+1; j < prices.size(); j++) {
            if (prices.at(j) < prices.at(i)) {
                period++;
                break;
            } else {period++;}
        }
        answer.push_back(period);
    }
    return answer;
}