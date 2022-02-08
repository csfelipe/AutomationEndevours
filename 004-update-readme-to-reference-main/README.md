# Update Main README to reference main

## What's up with this script?

### TLDR
Replace develop for main in the main `README` file

### A little bit of history
When doing a release I want to make sure that the index links are pointing to the expected branch.
Up until adding the first 3 scripts everything was just in the `develop` branch but now we'll have releases and I want to be redirected to `main` if I'm reading the `README` file from the `main` branch.


### Execution and Output

```
~ % python3  /Users/your_user/Repository/AutomationEndevours/004-update-readme-to-reference-main/update-readme-to-references-main.py 

Do you need a custom directory path? (y/n) n
Selected directory is: /Users/your_user/Repository/AutomationEndevours/
Do you need a custom file name? (y/n) n
File name is: README.md
Full path: /Users/your_user/Repository/AutomationEndevours/README.md
Thanks for using this script! Check you repo updates. Au revoir!
```