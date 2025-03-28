#!/bin/bash
set -e

# Initialize VOMS proxy (adjust parameters as needed)
voms-proxy-init --voms=cms --valid=168:00

# Define source and destination directories, and file names
SOURCE="eunsu@cms.knu.ac.kr:/u/user/eunsu/SE_UserHome/SKNano"
REMOTE_BASE="root://cluster142.knu.ac.kr//store/user/eunsu"
LOCAL_BASE="/gv0/Users/eunsu"
RSYNC_DIFF="rsync_diff.txt"
ROOT_FILES="root_files.txt"

# Remove existing diff files if they exist
if [ -f "$RSYNC_DIFF" ]; then
    rm "$RSYNC_DIFF" "$ROOT_FILES"
fi

# Step 1: Generate an incremental diff using rsync dry-run
rsync -avun "$SOURCE" "$LOCAL_BASE" > "$RSYNC_DIFF"

# Step 2: Filter the rsync diff for files ending with ".root"
grep '\.root$' "$RSYNC_DIFF" > "$ROOT_FILES"

# Define a function to transfer a single file using xrdcp
transfer_file() {
    local rel_path="$1"
    # Create destination directory based on the file's relative path
    local dest_dir="$LOCAL_BASE/$(dirname "$rel_path")"
    mkdir -p "$dest_dir"

    # Transfer the file with xrdcp
    echo "Transferring $rel_path..."
    xrdcp -f "$REMOTE_BASE/$rel_path" "$dest_dir/$(basename "$rel_path")"
}

# Export the function so that GNU Parallel can use it
export -f transfer_file
export LOCAL_BASE REMOTE_BASE

# Transfer files concurrently
parallel -j 16 transfer_file {} :::: "$ROOT_FILES"
