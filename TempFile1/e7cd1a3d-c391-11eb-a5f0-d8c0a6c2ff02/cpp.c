#include <stdio.h>
int main() {
    int n, i;
  	scanf("%d", &n);
    printf("Enter an integer: %d\n\n",n);
    
    for (i = 1; i <= 10 ++i) {
        printf("%d * %d = %d \n", n, i, n * i);
    }
    return 0;
}