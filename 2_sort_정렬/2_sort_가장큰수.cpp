// title: 정렬 > 가장 큰 수
// link: https://programmers.co.kr/learn/courses/30/lessons/42746

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b) {
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    vector<string> strings;
    for (auto num:numbers) 
        strings.push_back(to_string(num));
    sort(strings.begin(), strings.end(), compare);
    if (strings.at(0) == "0") return "0"; // 예외 처리
    string answer = "";
    for (auto str:strings)
        answer += str;
    return answer;
}