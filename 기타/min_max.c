#include <stdio.h>

#define INT_MAX 2147483647
#define INT_MIN (-2147483647 - 1)

int main() {
    int n;
    scanf("%d", &n);
    
    int l[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &l[i]);
    }
    
    int min = INT_MAX;
    int max = INT_MIN;
    
    for(int i = 0; i < n; i++) {
        if (l[i] < min) {
            min = l[i];
        }
        if (l[i] > max) {
            max = l[i];
        }
    }
    
    printf("%d %d\n", min, max);
    return 0;
}