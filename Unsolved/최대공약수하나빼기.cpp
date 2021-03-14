// title: [14476] 최대공약수 하나 빼기
// link: https://www.acmicpc.net/problem/14476

#include <stdio.h>
#include <iostream>
using namespace std;

// gcd(a b) == gcd(b, r), r = a%b, b가 0이 되는 순간 => gcd
int gcd(int a, int b) {
    while(b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    cout << gcd(36, 24) << endl;
}