# XCAsset Structure Validation

## What's up with this script?

### TLDR
Make sure that there's only image and icon assets in the root-level of a given XCAsset folder and it also flags images that have spaces in their name.

### A little bit of history
This script was created to be able to validate if a given XCAsset folder has anything beside image and icon sets.
If there's any sub-directory or any images that have spaces in their names then this script will throw an error informing how many directories and/or assets are not conforming to expectation.

### Execution and Output

1. Open `Xcode`
2. Tap on the `Project Navigator`
3. Tap on your `Target`
4. Tap on `Build Phase`
5. Tap on the `+` button and select `New Run Script Phase`
6. Fill in the editor with this script:
- Use only script content: copy and paste everything from this script in that small editor space
- Use a separate script file: 
    - (1) place your script file in your project directory; 
    - (2) in the editor space you want to reference the path to the script file (e.g. $SRCROOT/SpecialProject/Scripts/xcasset-structure-validation.sh)
7. Output:
- Success:
```
    All sub-directories are valid
```
- Failure:
    - There will be an error in Xcode and it will stop running
```
    XCAsset Structure violation
	Number of invalid sub-directories in the XCAsset folder: 12
	You can address this issue by: (1) moving new assets in sub-directories into the root level folder; (2) renaming asset files without spaces
	Invalid assets/directories:
    123-category
    RebrandImages
```