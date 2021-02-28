// link: https://programmers.co.kr/learn/courses/30/lessons/12902
// 분류: dp (점화식)

#include <string>
#include <vector>
#include <math.h>
#include <numeric> 

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> dp;
    
    if (n % 2 == 1) return 0;
    if (n == 2) return 3;
    if (n == 4) return 11;

    dp.push_back(0);
    dp.push_back(3);
    dp.push_back(11);

    int sum = 0;
    // n이 6 이상일때
    for (int i = 0; i < (n/2)-2; i++) {
        sum = accumulate(dp.begin(), dp.end(), -v.back());
        answer = dp[i+1]*3 + 2 + 2*sum;
        dp.push_back(answer);
    }

    return answer;
}