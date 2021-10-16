# Ticket to Branch

## What's up with this script?

### A little bit of history
At my previous job we used to have a pretty cool plug-in for our board tickets that would create the branch name based on the board ticket title and number, but I couldn't find a similar plug-in for the ticket board that I'm currently using.

### TLDR
Simple string manipulation that receives two strings does some replacements and outputs formatted strings.
- Input #1: should be the Board Ticket Number
- Input #2: should be the Board Ticket Title
- Output #1: branch name
- Output #2: branch name prefixed with feature (for those who use GitFlow)

### Execution and Output

```
~ % ticket2branch 
// Input 1
Enter ticket number (e.g. TKT-1234): tkt2345
// Input 2
Enter ticket name: Not Super Cool Feature That I wanted
// Output 1
-----------------------------------------------------
-
	Branch: tkt2345-not_super_cool_feature_that_i_wanted
-
-----------------------------------------------------
// Output 2
-----------------------------------------------------
-
	Branch: feature/tkt2345-not_super_cool_feature_that_i_wanted
-
-----------------------------------------------------
```

### Extra 
Don't forget to add an alias so you can call this without any extra effort:

```
alias ticket2branch="python3 ~/Repositories/AutomationEndevours/001-ticket-2-branch/ticket-2-branch.py"
```