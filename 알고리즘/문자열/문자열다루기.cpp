// link : https://programmers.co.kr/learn/courses/30/lessons/12918
// 분류: 문자열

#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(string s) {
    
    if (s.size() != 4 && s.size() != 6){
        return false;
    }
    for (int i=0; i<s.size(); i++) {
        int temp = s[i] - '0';
        if (temp<0||temp>9) return false;
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    string s;
    cin >> s;
    bool result = solution(s);
    cout << result << "\n";
}