// title: [2805] 나무 자르기
// link: https://www.acmicpc.net/problem/2805

// hink: binary search

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

long long N, M;
vector<long long> trees;
long long low, hi, mid, result;


long long calc(long long value) {
    long long res = 0;
    for (int i = 0; i < N; i++) {
        if (trees[i] > value) {
            res += trees[i] - value;
        }
    }
    return res;
}


int main() {

    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    scanf("%lld %lld", &N, &M);
    long long maxH = 0;
    for (int i = 0; i < N; i++) {
        long long tmp;
        scanf("%lld", &tmp);
        trees.push_back(tmp);
        if (maxH < trees[i]) maxH = trees[i];
    }
    low = 0;
    hi = maxH;
    result = 0;
    long long sum = 0; 

    while (low <= hi) {
        mid = (low + hi) / 2;
        sum = calc(mid); // 수확 가능한 나무의 양
        if (sum == M) {
            result = mid;
            break;
        } else if (sum < M) {
            hi = mid - 1;
        } else {
            result = mid;
            low = mid + 1;
        }
    }
    printf("%d", result);
    return 0;
}