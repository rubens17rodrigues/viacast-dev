#include <stdio.h>
#include <string.h>

void reverseString(char *in, char *out) {
    int i;
    int N = strlen(in);
    for (i = 0; i < N; ++i) {
        out[i] = in[N-i-1];
    }
    out[N] = '\0';
}

void reverseStringInPlace(char *in) {
    int i;
    int N = strlen(in);
    for (i = 0; i < N/2; ++i) {
        char c = in[i];
        in[i] = in[N -1 - i];
        in[N -1 -i] = c;
    }
    in[N] = '\0';
}

int main(int argc, char *argv[]) {
    char string_in[50];
    char stringReversed[50];
   
    printf("Enter the string to be reversed:\n>>");
    if (fgets(string_in, sizeof(string_in), stdin)){
        string_in[strcspn(string_in, "\n")] = '\0';
    }

    reverseString(string_in, stringReversed);
    printf("reversed = '%s'\n", stringReversed);

    reverseStringInPlace(string_in);
    printf("reversed in place = '%s'\n", string_in);

    return 0;
}
