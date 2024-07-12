#!/bin/bash

ignorefile=.gitignore

# Check if .gitignore file exists
if [ ! -f "$ignorefile" ]; then
  echo "Error: .gitignore file not found in the current directory."
  exit 1
fi

# Read the .gitignore file and generate the exclude pattern
exclude_pattern=$(grep -v '^#' "$ignorefile" | grep -v '^$' | sed 's:/$::' | tr '\n' '|' | sed 's/|$//')

# Run the tree command with the exclude pattern
tree -a -I "$exclude_pattern"
