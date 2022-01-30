// title: [2517] 달리기
// link: https://www.acmicpc.net/problem/2517

// hink: Inversion Count = Merge Sort하면서 숫자가 뒤바뀌는 횟수
// 오름차순이 아니라 내림차순으로 Inversion Count를 하면 
// O(N^2)에서 O(NlogN)으로 시간복잡도를 줄일 수 있다.
// class Runner를 만들어서 value, position을 변수로 넣어주면 쉽다.


#include <stdio.h>
#include <iostream>

using namespace std;

int N, *nums, *temp, *ranks;

void mergeSort(int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        mergeSort(start, mid);
        mergeSort(mid+1, end);
        merge(start, mid, end);
    }
}

void merge(int start, int mid, int end) {
    int p1 = start;
    int p2 = mid + 1;
    int k = start;
    while (p1 <= mid && p2 <= end) {
        if (nums[p1] <= nums[p2]) {
            temp[k++] = nums[p1++];
        } else {
            temp[k++] = nums[p2++];
        }
    }
    while (p1 <= mid) {
        temp[k++] = nums[p1++];
    }
}
int main() {
    scanf("%d", &N);
    nums = new int[N];
    temp = new int[N];
    for (int i=0; i<N; i++) 
        scanf("%d", &nums[i]);
    
    mergeSort(0, N-1);

    delete[] nums;
    delete[] temp;
    delete[] ranks;
}