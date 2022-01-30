// link: https://programmers.co.kr/learn/courses/30/lessons/17684
// 분류 : 문자열+배열

#include <string>
#include <vector>

using namespace std;

int find(vector<string> &dic, string msg)
{
    int size = dic.size();
    for (int i = 1; i < size; i++) {
        if (msg == dic[i]) return i;
    }
    return -1;
}

vector<int> solution(string msg) {
    vector<int> answer;
    vector<string> dic = { "-1" };
    int len = msg.length();

    for (int i = 0; i < 26; i++) {
        dic.push_back(string(1, 'A' + i));
    }

    int currentId = 0;
    int wordsize = 1;
    int idx = -1;

    while (true) 
    {
        string word = msg.substr(currentId, wordsize);     
        int temp = find(dic, word);

        if (temp > 0)
        {
            idx = temp;
            wordsize++;
            if (currentId + wordsize - 1 == len) {
                answer.push_back(idx);
                break;
            }
        }
        else {
            answer.push_back(idx);
            dic.emplace_back(word);
            currentId += wordsize-1;
            wordsize = 1;
            idx = -1;
        }
    }
    return answer;
}