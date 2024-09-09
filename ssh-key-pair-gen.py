import os
import paramiko

# Function to generate ssh keyt pair


def generate_ssh_key_pair(key_dir, key_name):
    if not os.path.exists(key_dir):
        os.makedirs(key_dir)

    # Create RSA key object
    key = paramiko.RSAKey.generate(bits=2048)
    # Define the file paths for private and public keys
    private_key_path = os.path.join(key_dir, key_name)
    public_key_path = f"{private_key_path}.pub"

    # Write private key to filee
    with open(private_key_path, 'w') as private_key_file:
        key.write_private_key(private_key_file)
        print(f"Private key saved to: {private_key_path}")

    # Write public key to fiile
    with open(public_key_path, 'w') as public_key_file:
        public_key_file.write(f"{key.get_name()} {key.get_base64()}")
        print(f"Public key saved to: {public_key_path}")


# Main function
if __name__ == "__main__":
    key_dir = input("Enter the directory to save ssh key pair: ")
    key_name = input("Enter the name for the SSH key pair: ")
    generate_ssh_key_pair(key_dir, key_name)
