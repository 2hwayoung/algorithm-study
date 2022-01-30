// https://programmers.co.kr/learn/courses/30/lessons/42576

#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string, int> m;

    for(string comp : completion) {
        m[comp] += 1;
    }

    for (string part : participant) {
        m[part] -= 1;
        if (m[part] < 0) return part;
    }
}