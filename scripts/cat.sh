#!/bin/bash

# Check if .gitignore file exists
if [ ! -f ".gitignore" ]; then
    echo "Error: .gitignore file not found in the current directory."
    exit 1
fi

# Read the .gitignore file and generate the exclude pattern
exclude_pattern=$(grep -v '^#' .gitignore | grep -v '^$' | sed 's/$/|/' | tr -d '\n' | sed 's/|$//')

# Enable shell options for handling wildcards and hidden files
shopt -s nullglob dotglob

# Find all files in the current directory and its subdirectories, excluding files and directories from .gitignore
while IFS= read -r -d '' file; do
    # Check if the file is a regular file and not a binary file
    if [ -f "$file" ] && ! file --mime "$file" | grep -q 'binary'; then
        echo -e "\n********\nFilename: $file\nContent:\n"
        cat "$file"
    fi
done < <(find . -type f -print0 | grep -zZvE "$exclude_pattern")
