#!/bin/bash
#
# Preconditions:
#	- You have to have a stash in your local repo with your code signing and provisioning profile changes
#
# How to use
# 
# 1. Only use it with the default values:
#	- Change value of the "default_git_directory" variable to the path to your project git root
#	- Change values of the "default_stash_name" variable to the name of your stash
#
# 2. Use with parameters:
#	- Perform script using parameters: 
#		./code-signing-search-and-apply.sh -dir=/path/to/project -stash=name_of_stash
#		./code-signing-search-and-apply.sh -d=/path/to/project -s=name_of_stash
#		./code-signing-search-and-apply.sh --dir=/path/to/project --stash=name_of_stash
#
#	- Notes: 
# 		1. The order of the parameters does not matter
#		2. In case you don't put a specific parameter or misspell a parameter it will use the default values 
#

default_git_directory="/Users/your_user_here/Repositories/ThatAwesomeProject"
default_stash_name="stashed_dev_certs"

prettyEcho() { 
	echo "---------->" $1 
}

# Try to fetch parameters
for i in "$@"
do
case $i in
    -dir=*|--dir=*|-d=*)
    GIVEN_DIRECTORY="${i#*=}"
    ;;
    -stash=*|--stash=*|-s=*)
    GIVEN_STASH_NAME="${i#*=}"
    ;;
    *)
esac
done

# Check if the directory parameter was given other wise use default directory
if [ -z "$GIVEN_DIRECTORY" ]; 
then
git_directory=$default_git_directory
else
git_directory=$GIVEN_DIRECTORY
fi

# Check if the stash name parameter was given other wise use default directory
if [ -z "$GIVEN_STASH_NAME" ]; 
then
stash_name=$default_stash_name
else
stash_name=$GIVEN_STASH_NAME
fi

# 
# Actual code to get stash with code signing and provisioning profile changes
#

prettyEcho "Welcome to Code Signing Stash Automation"
prettyEcho "Let's find your code signing stash and update your settings"

cd $git_directory

stash=$(git stash list | grep -m 1 "$stash_name")
prettyEcho "Found stash: $stash"

stash_index=$(echo "$stash" | sed 's/.*stash@{//; s/}:.*//')
prettyEcho "Extracted stash index: $stash_index"

## Get all differences | Count all differences | Remove white spaces
number_of_differences=$(git diff HEAD --name-only | wc -l | tr -d '[[:space:]]')

if [ "$number_of_differences" -gt 0 ]; 
then
prettyEcho "Temporarily commiting all files to avoid conflicts\n(Possible) Git output: \n"
git commit -m "Temporary commit to avoid conflicts" --all 
fi

prettyEcho "Applying stash\n(Possible) Git output: \n"
git stash apply --index $stash_index

if [ "$number_of_differences" -gt 0 ]; 
then
prettyEcho "Undoing temporary commit\n(Possible) Git output: \n"
git reset --soft HEAD~1
fi
prettyEcho "Done"