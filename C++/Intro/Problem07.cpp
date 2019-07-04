#include <iostream>
using namespace std;

void update(int *a,int *b) {
    int sum = *a + *b;
    int absDiff;
    if (*a-*b>0){
        absDiff = *a-*b;
    }else{
        absDiff = -(*a-*b);
    }
    *a = sum;
    *b = absDiff;

}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

