# Code Signing - Search and Apply

## What's up with this script?

### TLDR
Search for a git stash and apply it.

### A little bit of history
Sometimes you can't just invalidade all your provisioning profiles and start using Fastlane, am I right? 
In a project I participated there were 4 different targets that were always set to the AppStore certificates and profiles, so at least once or twice a day I had to change these certificates manually which could take a few minutes.
So initially I started with just stashing those changes and applying manually, but that also got boring and at last but not least the idea came to me to just have this script that could be applied for any project that had a certificate and profile stash opportunity.

### Preconditions
You have to have your certificate and profile changes stashed 

### Parameters
- directory (-dir or --dir): path to the project root
- stash (-stash or --stash): name of the stash

### Execution and Output

```
~ % updateCoolProjProfiles
----------> Welcome to Code Signing Stash Automation
----------> Let's find your code signing stash and update your settings
----------> Found stash: stash@{2}: On feature/other: cool_proj_profiles
----------> Extracted stash index: 2
----------> Temporarily commiting all files to avoid conflicts
(Possible) Git output: 

[feature/new_feature 36742221] Temporary commit to avoid conflicts
 1 file changed, 27 insertions(+)
 create mode 100644 CoolProject/CoolProject/Components/StoredValuesAccessor.swift
----------> Applying stash
(Possible) Git output: 

Auto-merging CoolProject/CoolProject.xcodeproj/project.pbxproj
On branch feature/new_feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   PersonalProtection/PersonalProtection.xcodeproj/project.pbxproj

no changes added to commit (use "git add" and/or "git commit -a")
----------> Undoing temporary commit
(Possible) Git output: 

----------> Done
```

### Extra 
Don't forget to add an alias so you can call this without any extra effort:

```
alias updateCoolProjProfiles="sh /Users/YOUR_USER/Documents/Development/Scripts/code_signing_automation.sh -dir=/Users/YOUR_USER/Repositories/CoolProject -stash=cool_proj_profiles"
```