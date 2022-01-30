// title : 가르침
// link : https://www.acmicpc.net/problem/1062
// 분류: 알고리즘/탐색/DFS(깊이우선탐색)

// hint: a,n,t,i,c 는 필수로 알아야 한다.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N, K;
vector<string> words;
vector<bool> visited;
int selectedCount = 0;
int maximum = 0;

int countWords() {
    int count = 0;
    for (int i=0;i<N;i++) {
        string word = words[i];
        bool isPossible = true;
        for (int j =0; j<word.length(); j++) {
            if (visited[(int)word.at(j) - 'a'] == false) {
                isPossible = false;
                break;
            }
        }
        if (isPossible == true) {
            count ++;
        }
    }
    return count;
}

void dfs(int index) {
    // 1. 체크인 -> visited[index] = true, selectedCount
    // 2. 목적지인가? -> selectedCount가 K에 도달했는가? -> max 갱신
    //  3. 연결된 곳을 순회 -> index + 1 ~ 26
    //   4. 갈 수 있는가? -> visited[next] == false
    //    5. 간다. -> dfs(next)
    // 6. 체크아웃 -> visited[index] = false, selectedCount
    visited[index] = true;
    selectedCount++;

    bool check = true;
    int subMax = 0;

    if (selectedCount == K) {
        // max 갱신
        maximum = max(countWords(), maximum);
    } else {
        for (int i=index + 1; i < 26; i++) {
            if (visited[i] == false) {
                dfs(i);
            }
        }
    }
    visited[index] = false;
    selectedCount--;
}

int main() {

    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    cin >> N >> K;

    // a, n, t, i, c default 필요
    words.assign(N, "");
    visited.assign(26, false);
    visited['a'-'a'] = true;
    visited['n'-'a'] = true;
    visited['t'-'a'] = true;
    visited['i'-'a'] = true;
    visited['c'-'a'] = true;
    selectedCount = 5;
    
    // words 입력
    for (int i = 0; i < N; i++){
        cin >> words[i];
        words[i].replace(words[i].begin(), words[i].begin()+4, "");
    }
    // K가 5보다 작은 값이 입력되면, 그 어떠한 단어도 읽을 수 없다.
    if (K < 5) {
        cout << 0 << endl;
        return 0;
    }
    maximum = countWords();
    for (int i=0; i < 26; i++) {
        if(visited[i] == false) {
            dfs(i);
        }
    }
    cout << maximum << endl;
    return 0;
}
