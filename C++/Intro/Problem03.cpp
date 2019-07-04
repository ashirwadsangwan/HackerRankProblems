#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a;
    long b;
    char c;
    float f;
    double s;

    scanf("%d %ld %c %f %lf", &a, &b, &c, &f, &s);
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout.precision(3);
    cout << fixed << f << endl;
    cout.precision(9);
    cout << fixed << s << endl;
    return 0;
}

