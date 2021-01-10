// title: 정렬 > K번째수
// link: https://programmers.co.kr/learn/courses/30/lessons/42748?language=cpp

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int slice(vector<int> &array, vector<int> &sub_command) {
    vector<int> sub_array(sub_command[1]-sub_command[0]+1);
    copy(array.begin() + sub_command[0] - 1, array.begin() + sub_command[1], sub_array.begin());
    sort(sub_array.begin(), sub_array.end());
    return sub_array[sub_command[2]-1];
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (int i=0; i < commands.size(); i++)
        answer.push_back(slice(array, commands[i]));
    return answer;
}