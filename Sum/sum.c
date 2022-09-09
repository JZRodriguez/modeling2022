#include <stdio.h>
#include <stdlib.h>

int main() {
  int i;
  int suma = 0;
  int n = 3;
  for(int i = 1; i <= n+1; i++) {
    suma = suma + i;
    if (i == n) {
      printf("%d ", (i));
      break;
    }
    printf("%d + ", (i));
  }
  printf("= %d \n", (suma));
  return 0;
}
