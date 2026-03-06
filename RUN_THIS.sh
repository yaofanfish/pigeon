#!/bin/sh
if [ 1 ]; then
	echo -e "\033[36mRemoving .git\033[0m"
	rm -r .git
fi
echo -e "\033[36metting up git\033[0m"
./git_setup.sh
echo -e "\033[36mInitialising git\033[0m"
git init
echo -e "\033[32mDone with basic setup! Would you like to use github-cli to make this a real repository? \033[0m (Y/n)"
read x
if [ "$x" == "Y" ] || [ "$x" == "y" ]; then
	echo "Creating repo; what name? "
	read x
	gh repo create "$x" --source=. --public --confirm --remote=origin --push
	echo -e "\033[32mCreated repo, done! \033[0m"
else
	echo -e "\033[32mNot creating repository, done! \033[0m"
fi
echo bye
