// link: https://programmers.co.kr/learn/courses/30/lessons/12901
// 분류: 기본수학

#include <string>
#include <vector>

using namespace std;

string weeks[7] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
int months[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

string solution(int a, int b) {
    string answer = "";
    int count = 0;
    for (int i=0; i<a-1; i++) {
        count += months[i];
    }
    count += b-1;
    count %= 7;
    answer = weeks[count];
    return answer;
}