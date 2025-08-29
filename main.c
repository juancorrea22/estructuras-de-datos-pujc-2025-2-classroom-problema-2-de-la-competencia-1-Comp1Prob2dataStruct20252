#include <stdio.h>
#include <stdlib.h>


int main() {

    long long n, i;
    long long *l;

    scanf("%lld", &n);

    l = (long long *) malloc(n*sizeof(long long));

    for (i = 0; i < n; i++) {
        scanf("%lld", l + i);

    }

    for (i = n - 1; i > -1 ; i--) {
        printf("%lld ", l[i]); 
    }
    return 0;
}
