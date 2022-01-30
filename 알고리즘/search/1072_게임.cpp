// title: [1072] 게임
// link: https://www.acmicpc.net/problem/1072
// 분류: 알고리즘/탐색/이분 탐색

#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
    long X, Y;
    scanf("%ld %ld", &X, &Y);
    long long score = 100 * Y / X;

    long long low = 0;
    long long high = 1000000001;
    long long mid = 0;
    long long newScore;
    long long result = -1;

    if (score >= 99) {
        printf("%lld", result);
        return 0;
    }
    while (low < high) {
        mid = (low + high) / 2;
        newScore = (100 * (Y + mid) / (X + mid));
        if (score >= newScore){
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    result = high;
    
    if (high > 1000000000) result = -1;
    printf("%lld", result);
}