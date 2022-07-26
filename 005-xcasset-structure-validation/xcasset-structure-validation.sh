# Build the path to the XCAssets folder
XCASSET_ROOT_FOLDER="${PROJECT_DIR}/SpecialProject/Assets.xcassets"
# List everything in the XCAssets directory
ASSETS=$(ls "${XCASSET_ROOT_FOLDER}")

declare -a INVALID_DIRECTORIES

# Loop through everything that has been listed
for ASSET in $ASSETS; do
    # We want to skip any folder that is an imageset and appiconset and the directory json
	if [[ "$ASSET" == *".imageset"* ]] || [[ "$ASSET" == *".appiconset"* ]] || [[ "$ASSET" == *".json"* ]] 
	then
		continue
    # Any other items is invalid and should be flagged
	else 
		INVALID_DIRECTORIES+=($ASSET)
	fi
done

# In case we hava invalid directories or items then we should raise an error
if [[ ${#INVALID_DIRECTORIES[@]} -gt 0 ]] 
then
    echo "error: XCAsset Structure violation"
	echo "Number of invalid sub-directories in the XCAsset folder: ${#INVALID_DIRECTORIES[@]}"
	echo "You can address this issue by: (1) moving new assets in sub-directories into the root level folder; (2) renaming asset files without spaces"
	echo "Invalid assets/directories:"
	echo $INVALID_DIRECTORIES
	exit 1
else
	echo "All sub-directories are valid"
fi
