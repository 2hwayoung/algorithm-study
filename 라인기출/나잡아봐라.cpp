//link: https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/

// 코니의 위치: C+t(t+1)/2
// 브라운 : B-1, B+1, 2*B
// 0 <= x <= 200000
// 브라운은 범위를 벗어날 수 없고 코니가 벗어나면 끝!

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int solve(int conyPosition, int brownPosition) {
    int time = 0;
    bool visit[200001][2];
    queue<pair<int, int>> queue;

    memset(visit, 0, sizeof(visit));
    queue.push(make_pair(brownPosition, 0));

    while (true) {
        conyPosition += time;

        if (conyPosition > 200000) return -1;
        if (visit[conyPosition][time % 2]) return time;

        for (int i=0, size=queue.size(); i<size; i++) {
            int currentPosition = queue.front().first;
            int newTime = (queue.front().second + 1) % 2;
            int newPosition;

            queue.pop();

            newPosition = currentPosition - 1;
            if (newPosition >= 0 && !visit[newPosition][newTime]) {
                visit[newPosition][newTime] = true;
                queue.push(make_pair(newPosition, newTime));
            }

            newPosition = currentPosition + 1;
            if (newPosition < 200001 && !visit[newPosition][newTime]) {
                visit[newPosition][newTime] = true;
                queue.push(make_pair(newPosition, newTime));
            }

            newPosition = currentPosition * 2;
            if (newPosition < 200001 && !visit[newPosition][newTime]) {
                visit[newPosition][newTime] = true;
                queue.push(make_pair(newPosition, newTime));
            }
        }
        time ++;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int C, B;

    cin >> C >> B; 
    
    int result = solve(C, B);
    cout << result;
}