make:
	echo "Hello! please use make dependencies or make install. "
dependencies:
	echo "dependencies: binutils, python"
install:
	@if [ "$$EUID" != "0" ]; then \
		(cp ./pigeonify "$$HOME/.local/bin/pigeonify" && echo -e "\033[32msuccess! \033[0m") || (mkdir -p ~/.local/bin; cp ./pigeonify ~/.local/bin); \
	else \
		cp ./pigeonify /usr/local/bin/pigeonify || (echo "Please run as root"); \
	fi
uninstall:
	@if [ "$$EUID" != "0" ]; then \
		rm "$$HOME/.local/bin/pigeonify"; \
	else \
		rm /usr/local/bin/pigeonify; \
	fi
