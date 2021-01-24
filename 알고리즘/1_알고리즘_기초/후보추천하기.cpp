// title: [1713] 후보 추천하기
// link: https://www.acmicpc.net/problem/1713
// 분류: 알고리즘/정렬

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Person {
    int num;
    int count;
    int timeStamp;
    bool isIn;

    Person() {};

    Person(int _num, int _count, int _timeStamp, bool _isIn) 
    : num(_num), count(_count), timeStamp(_timeStamp), isIn(_isIn) {};

    int operator < (const Person & o) const {
        // -1 = 내가 원하는 순서 = 바꾸지 않음
        if (this->count < o.count) {
            return -1;
        }
        if (this->count == o.count) {
            if (this->timeStamp < o.timeStamp) {
                return -1;
            } else {
                return 1;
            }
        }
        // 1 = 내가 원하지 않는 순서 = 바꿈
        else {
            return 1;
        }
    }
};

int compare(Person o1, Person o2) {
    // -1 = 내가 원하는 순서 = 바꾸지 않음
    if (o1.num < o2.num) {
        return -1;
    }
    // 1 = 내가 원하지 않는 순서 = 바꿈
    else {
        return 1;
    }
}

int main() {

    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    freopen("input.txt", "r", stdin);

    int N, K;
    vector<Person> persons(101);
    vector<Person> list;

    cin >> N >> K;

    for (int i=0; i<K; i++) {
        int num;
        cin >> num;
        if (&persons[num] == nullptr) {
            persons[num] = Person(num, 0, 0, false);
        }
        if (persons[num].isIn == true) {
            persons[num].count++;
        } else {
            if (list.size() == N) {
                sort(list.begin(), list.end(), compare);
                list.front().isIn = false;
                list.erase(list.begin());
            }
            persons[num].count = 1;
            persons[num].isIn = true;
            persons[num].timeStamp = 1;
            list.push_back(persons[num]);
        }
    }

    sort(list.begin(), list.end(), compare);

    for (int i = 0; i < N; i ++) {
        cout << list[i].num << " ";
    }

}