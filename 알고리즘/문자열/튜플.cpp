// link: https://programmers.co.kr/learn/courses/30/lessons/64065#
// 분류: 문자열

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

bool compare(vector<int> v1, vector<int> v2) {
    return v1.size() < v2.size();
}

vector<int> solution(string s) {
    // 1. s를 vector inputs로 바꾸기
    s = s.substr(1, s.size()-2);

    vector<vector<int>> inputs;
    vector<int> temp;
    string sub;
    for (int i=0; i<s.size(); i++) {
        if (s[i] == '{') {
            continue;
        } else if (s[i] == '}') {
            temp.push_back(stoi(sub));
            sub = "";
            inputs.push_back(temp);
            temp.clear();
            i++;
            continue;
        } else if (s[i] == ',') {
            temp.push_back(stoi(sub));
            sub = "";
        } else {
            sub += s[i];
        }
    }

    sort(inputs.begin(), inputs.end(), compare);

    vector<int> answer;
    // 2. inputs에서 하나씩 꺼내면서 node화시키기, 존재하는 원소 체크하기
    set<int> sets; // 중복값 제외
    for (vector<int> input: inputs) {
        for (int item: input) {
            bool issuccess = sets.insert(item).second;
            if (issuccess) {
                answer.push_back(item);
            }
        }
    }
    return answer;
}

int main() {
    ios_base::sync_with_stdio;
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input.txt", "r", stdin);

    string s;
    cin >> s;
    vector<int> result = solution(s);
    for (int i=0; i<result.size(); i++) {
        cout << result[i] << " ";
    }
    
}