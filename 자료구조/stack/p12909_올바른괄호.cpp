// link: https://programmers.co.kr/learn/courses/30/lessons/12909
// 분류: 자료구조/스택

#include <string>
#include <iostream>
#include <stack>

using namespace std;
stack<char> pareStack;

bool solution(string s)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int count = 0;

    if (s[0] == ')') return false;

    for (int i=0; i<s.size(); i++) {
        if (s[i] == '(') {
            pareStack.push(s[i]);
        } else {
            if (pareStack.empty()) return false;
            if (pareStack.top() == '(') pareStack.pop();
        }
    }

    bool answer = true;

    if (!pareStack.empty())  answer = false;

    return answer;
}