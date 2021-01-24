// title: [1713] 후보 추천하기
// link: https://www.acmicpc.net/problem/1713
// 분류: 알고리즘/정렬

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// 사람 구조체 생성
struct Person {
    int num;
    int count;
    int timeStamp;
    bool isIn;

    Person() {};
    Person(int _num, int _count, int _timeStamp, bool _isIn) 
    : num(_num), count(_count), timeStamp(_timeStamp), isIn(_isIn) {}; 
};

bool compare2(Person* o1, Person* o2) {
    // -1 = 내가 원하는 순서 = 바꾸지 않음
    if (o1->count < o2->count) {
        return true;
    }
    if (o1->count == o2->count) {
        if (o1->timeStamp < o2->timeStamp) {
            return true;
        } else {
            return false;
        }
    }
    // 1 = 내가 원하지 않는 순서 = 바꿈
    else {
        return false;
    }
}

bool compare(Person* o1, Person* o2) {
    return o1->num < o2->num;
}

int main() {

    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    // freopen("input.txt", "r", stdin);

    int N, K;
    int i = 1;
    
    vector<Person*> persons(101);
    vector<Person*> list;

    cin >> N >> K;
    int timeStamp = 1;

    for (int i=0; i<K; i++) {
        int num;
        cin >> num;
        if (!persons[num]) {
            persons[num] = new Person(num, 0, 0, false);
        }
        if (persons[num]->isIn == true) {
            persons[num]->count += 1;
        } else {
            if (list.size() == N) {
                sort(list.begin(), list.end(), compare2);
                persons[list.front()->num]->isIn = false;
                list.front()->count = 0;
                list.erase(list.begin());  
            }
            persons[num]->num = num;
            persons[num]->count = 1;
            persons[num]->isIn = true;
            persons[num]->timeStamp = timeStamp++;
            list.push_back(persons[num]);
        }
    }

    sort(list.begin(), list.end(), compare);

    for (int i = 0; i < N; i++) {
        cout << list[i]->num << " ";
    }

    vector<Person*>::iterator iter;
    for (iter=persons.begin(); iter != persons.end(); ++iter ){
        delete *iter;
    }
    persons.clear();
    list.clear();
}