// title: 두 배열의 합
// link: https://www.acmicpc.net/problem/2143
// 분류 : 알고리즘/탐색/이분탐색 
// 하나는 오름차순, 다른 하나는 내림차순으로 정렬

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int compare(int n1, int n2) {
    return n1 < n2;
}

int compare_reverse(int n1, int n2) {
    return n1 > n2;
}

int main() {
    int T, n, m, temp;
    vector<int> A, B;
    cin >> T;
    cin >> n;
    for (int i=0; i<n; i++) {
        scanf("%d", &temp);
        A.push_back(temp);
    }
    cin >> m;
    for (int i=0; i<m; i++) {
        scanf("%d", &temp);
        B.push_back(temp);
    }
    sort(A.begin(), A.end(), compare); // 오름차순으로 정렬
    sort(B.begin(), B.end(), compare_reverse); // 내림차순으로 정렬

    int Astart = 0, Aend = 1, Bstart = 1, Bend = 0;
    long count = 0, sum = 0;

    while (true) {
        sum = 0; //초기화
        for (int i=Astart; i<Aend; i++)
            sum += A.at(i);
        for (int j=Bstart; j<Bend; j++)
            sum += B.at(j);
        if (sum < T) {
            Aend ++;
        }
    }
}