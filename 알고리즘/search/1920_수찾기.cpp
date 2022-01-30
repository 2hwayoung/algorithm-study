// title: [1920] 수 찾기
// link: https://www.acmicpc.net/problem/1920
// 분류: 알고리즘/탐색/이분 탐색

#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    
    cin >> N;

    int A[N];

    for (int i=0; i<N; i++) {
        int num;
        scanf("%d", &A[i]);
    }
    sort(A, A+N);

    cin >> M;
    
    int searchNum;
    int low = 0;
    int high = sizeof(A)/sizeof(A[0]);
    int mid = 0;

    for (int i=0; i<M; i++) {
        scanf("%d", &searchNum);
        int low = 0;
        int high = sizeof(A)/sizeof(A[0]);
        int mid = 0;
        while (low < high) {
            mid = (low + high) / 2;
            if (A[mid] == searchNum){
                printf("1 \n");
                break;
            } else if(A[mid] < searchNum) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        if (A[mid] != searchNum) {
            printf("0 \n");      
        }  
    }
    
}