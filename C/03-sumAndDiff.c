#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a, b, sum_ab, diff_ab;
    float c, d, sum_cd, diff_cd;

    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);
    
    sum_ab  = a+b;
    diff_ab = a-b;
    sum_cd = c+d;
    diff_cd = c-d;


    printf("%d %d\n", sum_ab, diff_ab);
    printf("%.1f %.1f\n", sum_cd, diff_cd);

    return 0;
}

