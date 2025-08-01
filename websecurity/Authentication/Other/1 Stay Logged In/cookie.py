import hashlib
import base64

# Define the username
username = "carlos"

# Read passwords from a file
passwords_file = 'passwords.txt'  # Make sure this file exists and contains your passwords
output_file = 'passHash'  # File to write the results

# Open the file and read the passwords
with open(passwords_file, 'r') as file:
    passwords = file.read().splitlines()  # Read each line as a password

# Open the output file for writing
with open(output_file, 'w') as output:
    # Process each password
    for password in passwords:
        # Create MD5 hash of the password
        md5_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        
        # Combine username and hashed password
        combined = f"{username}:{md5_hash}"
        
        # Encode the combined string in Base64
        base64_encoded = base64.b64encode(combined.encode('utf-8')).decode('utf-8')
        
        # Write the result to the output file
        output.write(base64_encoded + '\n')  # Write each result on a new line

print(f"Base64 encoded hashes have been written to {output_file}.")
