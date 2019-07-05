#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;


/* Function to reverse arr[] from start to end*/
void reverse(int arr[], int start, int end) {
    while (start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}   

void printArray(int arr[], int size){
    for (int i=0; i < size; i++){
        cout << arr[i] << " ";
    }
}



int main() {
    int N,i=0;
    cin>>N;
    int *A = new int[N];
    while(cin>>A[i++] && (i < N));
    
    reverse(A, 0, N-1);
    printArray(A, N);
    return 0;
}
