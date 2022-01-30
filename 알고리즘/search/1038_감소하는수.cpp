// link: https://www.acmicpc.net/problem/1038
// 분류: brute-force algorithm

#include <iostream>
#include <queue>

using namespace std;

const int MAX = 1000000;

int N;
int idx = 9;
queue <long long> q;
long long descending[MAX+1];

void solve() {
    while (idx <= N) {
        if (q.empty()) return ;
        long long descendingNum = q.front();
        q.pop();
        int lastNum = descendingNum % 10;
        for (int i=0; i<lastNum; i++) {
            q.push(descendingNum*10 + i);
            descending[++idx] = descendingNum*10 + i;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    for (int i = 0; i<10; i++) {
        q.push(i);
        descending[i] = i;
    }
    solve();

    if (!descending[N] && N) cout << -1 << endl;
    else cout << descending[N] << endl;

    return 0;   
    
}