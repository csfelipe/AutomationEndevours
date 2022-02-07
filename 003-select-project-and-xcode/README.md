# Select Project and Xcode

## What's up with this script?

### TLDR
Search for a project, select a Xcode version and use that Xcode to open the given project

### A little bit of history
Have you ever wanted to use a command to select your Xcode and Project? Look no further, fam. I gotchu.
I was working in 2 different projects at once and each one needed a specific version of Xcode, so sometimes I would open a given project in the wrong Xcode version, so I decided to simplify things and make a script for it.

### Preconditions
If you don't want to send the `-dir` parameter then you should update the `default_repository_directory` value in the file

### Execution and Output

```
~ % xcodestart
Type in your project search term and press <Enter>: cool


Choose which directory: 
	(0): /Users/your_user/Repositories/#CoolProject
	(1): /Users/your_user/Repositories/#CoolProject1
	(2): /Users/your_user/Repositories/CarCoolant
	(3): /Users/your_user/Repositories/CoolProject
Choose which directory and press <Enter>: 3
Directory (1) was selected /Users/your_user/Repositories/CoolProject]


Choose which project file:
	(0): /Users/your_user/Repositories/CoolProject/Pods/Pods.xcodeproj
	(1): /Users/your_user/Repositories/CoolProject/CoolProject.xcodeproj
	(2): /Users/your_user/Repositories/CoolProject/CoolProject.xcworkspace
	(3): /Users/your_user/Repositories/CoolProject/CoolProject.xcodeproj/project.xcworkspace
Choose which project file and press <Enter>: 2
Project file (2) was selected [/Users/your_user/Repositories/CoolProject/CoolProject.xcworkspace]


Choose which Xcode you would like to use:
	(0): 13.0
	(1): 12.0.1
	(2): 12.4
	(3): 12.5.1
	(4): 12.5
Select option and press <Enter>: 3
Selected: Xcode 12.5.1
```

### Extra 
Don't forget to add an alias so you can call this without any extra effort:

```
alias xcodestart="sh /Users/your_user/Documents/Development/Scripts/xcode_selection.sh --dir=/Users/your_user/Repositories"
```