#include <stdio.h>

int main()
{
    unsigned long n, m, a = 1;
    unsigned long na, ma, res = 0;
    
    scanf("%lu %lu %lu", &n, &m, &a);
    
    na = n/a;

    if (n%a != 0)
        na++;
    
    ma = m/a;

    if (m%a != 0)
        ma++;

    res = na * ma;

    printf("%lu", res);

    return 0;
}
