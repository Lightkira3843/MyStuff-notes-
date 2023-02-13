#include <stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = -n + 1; i <= n - 1; i++) {
        for (int j = -n + 1; j <= n - 1; j++) {
            int abs_i = i < 0 ? -i : i;
            int abs_j = j < 0 ? -j : j;
            int min_ij = abs_i < abs_j ? abs_i : abs_j;
            printf("%d ",  n-min_ij  );
        }
        printf("\n");
    }

    return 0;
}
