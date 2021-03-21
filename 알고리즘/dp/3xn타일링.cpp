// link: https://programmers.co.kr/learn/courses/30/lessons/12902
// 분류: dp (점화식)

#include <string>
#include <vector>

using namespace std;
int MOD = 1000000007;
vector<long long> dp;

int solution(int n) {
    int answer = 0;
    long long dp[5001];
    if (n % 2 == 1) return 0;
    if (n == 2) return 3;
    if (n == 4) return 11;
    dp[0] = 1;
    dp[2] = 3;
    for (int i = 4; i <= n; i += 2) {
        dp[i] = dp[i-2] * 3;
        for (int j=i-4; j>= 0; j-= 2) {
            dp[i] += dp[j] * 2;
        }
        dp[i] %= MOD;
    }
    return answer;
}