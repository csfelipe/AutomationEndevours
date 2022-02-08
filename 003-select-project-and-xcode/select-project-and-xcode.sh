default_repository_directory="/Users/your_user_here/Repositories/"

# Echos given input without being captured by function
output() {
	echo "$1" >&2
}

# Checks if the given input contains only numeric characters
is_input_only_digits() {
	if [[ $1 =~ ^[0-9]+$ ]]
	then
		echo "true"
	else
		echo "false"
	fi
}

# Exit Program when user enters (Qq)
exit_on_q() {
	case $1 in
		[Qq]* ) output "You requested to quit Xcode+Project selection. Goodbye!"; exit 1;;
	esac
}

# Ask for Search Term
ask_for_search_term() {
	local search_term
	read -p "Type in your project search term and press <Enter>: " search_term
	echo "$search_term"
}

# Find Directory
find_directory() {
	while true;
	do 
		local search_term=$(ask_for_search_term)
			
		exit_on_q $search_term
		
		local found_directories=($(ls $repository_directory | grep -iF "$search_term"))
		if [[ ${#found_directories[@]} -ne 0 ]];
		then
			break	
		else
			output "\nNo directory with search term \"$search_term\" was found. Try again or press (Q) to exit."
		fi	
				
	done

	output "\n\nChoose which directory: "
	for ((i = 0; i < "${#found_directories[@]}"; ++i)); 
	do
		output "\t($i): $repository_directory${found_directories[$i]}"
	done

	while true;
	do
		local selected_directory
		read -p "Choose which directory and press <Enter>: " selected_directory
		
		exit_on_q $selected_directory
		local is_valid_input=$(is_input_only_digits $selected_directory) 
		
		if [[ $is_valid_input == "false" ]];
		then
			output "\nYou entered an invalid input \"$selected_directory\". Try again or press (Q) to exit."		
		elif [[ $selected_directory -lt 0 || $selected_directory -ge ${#found_directories[@]} ]];
		then
			output "\nYou selected an invalid index \"$selected_directory\". Try again or press (Q) to exit."
		else
			break
		fi
	done

	local repository_full_path="$repository_directory${found_directories[$selected_directory]}"
	output "Directory ($selected_directory) was selected [$repository_full_path]"
	echo "$repository_full_path"
}

# Project Selection
find_available_project_directories() {
	local all_project_files=()
	xcodeprojs=($(find $1 -name "*.xcodeproj" -maxdepth 3))
	xcworkspaces=($(find $1 -name "*.xcworkspace" -maxdepth 3))

	for ((i = 0; i < "${#xcodeprojs[@]}"; ++i)); 
	do
		all_project_files+=("${xcodeprojs[$i]}")
	done

	for ((i = 0; i < "${#xcworkspaces[@]}"; ++i)); 
	do
		all_project_files+=("${xcworkspaces[$i]}")
	done

	output "\n\nChoose which project file:"
	for ((i = 0; i < "${#all_project_files[@]}"; ++i)); 
	do
		output "\t($i): ${all_project_files[$i]}"
	done
	
	while true;
	do
		local selected_project_file
		read -p "Choose which project file and press <Enter>: " selected_project_file
		
		exit_on_q $selected_project_file
		local is_valid_input=$(is_input_only_digits $selected_project_file) 
		
		if [[ $is_valid_input == "false" ]];
		then
			output "\nYou entered an invalid input \"$selected_project_file\". Try again or press (Q) to exit."		
		elif [[ $selected_project_file -lt 0 || $selected_project_file -ge ${#all_project_files[@]} ]];
		then
			output "\nYou selected an invalid index \"$selected_project_file\". Try again or press (Q) to exit."
		else
			break
		fi
	done

	output "Project file ($selected_project_file) was selected [${all_project_files[$selected_project_file]}]"
	echo "${all_project_files[$selected_project_file]}"
}

# Xcode Selection
select_xcode() {
	local xcodes=()
	local versions=()

	local ls_command=$(ls /Applications/ | grep Xcode)
	local xcodes=($ls_command) 

	for ((i = 0; i < "${#xcodes[@]}"; ++i)); 
	do
		versions+=($(mdls -name kMDItemVersion /Applications/${xcodes[$i]} | awk -F'"' '{print $2}'))
	done

	while true; do
		output "\n\nChoose which Xcode you would like to use:"
		for ((i = 0; i < "${#versions[@]}"; ++i)); 
		do
			output "\t($i): ${versions[$i]}"
		done

		read -p "Select option and press <Enter>: " selected_xcode

		local is_valid_option="false"

		exit_on_q $selected_xcode
	
		for ((i = 0; i < "${#versions[@]}"; ++i)); 
		do
			if [[ "$i" == "$selected_xcode" ]]; 
			then
				is_valid_option="true"
				break	
			fi
		done
		
		local is_valid_input=$(is_input_only_digits $selected_xcode)

		if [[ $is_valid_input == "false"  ]];
		then
			output "\nYou entered an invalid input \"$selected_xcode\". Try again or press (Q) to exit."
		elif [[ "$is_valid_option" == "true" ]]; 
		then
			output "Selected: Xcode ${versions[$selected_xcode]}"
			break
		else
			output "Try again. Your selection ($selected_xcode) wasn't valid. (Press (Q) to exit)"
		fi
	done
	echo "${xcodes[$selected_xcode]}"
}

# Open project file with given Xcode version
open_project() {
	local xcode="/Applications/$1"
	local project="$2"
	open -a $xcode $2
}

# Try to fetch parameters
for i in "$@"
do
case $i in
    -dir=*|--dir=*|-d=*)
    GIVEN_DIRECTORY="${i#*=}"
    ;;
esac
done

# Check if the directory parameter was given other wise use default directory
if [ -z "$GIVEN_DIRECTORY" ]; 
then
repository_directory=$default_repository_directory
else
repository_directory=$GIVEN_DIRECTORY
fi

# Add forward slash to the end of the path if it does not have it already
if [[ ${repository_directory: -1} != "/" ]];
then
repository_directory+="/"
fi 

path=$(find_directory)
project_directory=$(find_available_project_directories $path)
xcode_version=$(select_xcode)
open_project $xcode_version $project_directory