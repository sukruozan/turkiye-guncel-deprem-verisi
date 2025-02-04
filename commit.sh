#!/bin/bash

# Check if a commit message was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: ./commit.sh 'Your commit message'"
  exit 1
fi

# Set variables
COMMIT_MESSAGE="$1"

# Navigate to the repository's root directory (optional if running in the repo directory)
# cd /path/to/your/repo
cd /home/GitHub/deprem

# Stage all changes (including deletions and new files)
git add .

# Commit the changes with the provided message
git commit -m "$COMMIT_MESSAGE"

# Push the changes to the default branch
git push

# Print success message
echo "Changes committed and pushed successfully!"
