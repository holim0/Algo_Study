#include <stdio.h>

int main(void)
{
	char input[100];
	int length, i, result = 0;
	scanf("%d", &length);
	scanf("%s", input);

	for (i = 0; i<length; i++)
		result += (input[i] - '0');

	printf("%d\n", result);

	return 0;
}