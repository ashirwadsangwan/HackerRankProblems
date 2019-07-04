#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    string word[9] = {"one","two","three","four","five","six","seven","eight","nine"};
    int a;
    int b;
    scanf("%d %d", &a, &b);

    for (int i=a; i< b+1; i++){
        if (i>9 && i%2==0){
            cout << "even" << endl;
        }else if (i>9 && i%2 != 0){
            cout << "odd" << endl;
        }else{
            cout << word[i-1] << endl;
        }
    }
    return 0;
}

