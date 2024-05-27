from cryptography.fernet import Fernet

# Activation codes
activation_codes = [
    "lnepptl50sq6whk",
    "vky3sqvbhzxxn1d",
    "c4qfs60gpiptei3",
    "j4t4x3n7gy1jkov",
    "isaeou1oigrxa1k",
    "8g4m4ui19o80g7g",
    "7rpqln6u46zfurg",
    "cpwh9dne3qoz6m8",
    "d61g4t8feycv8og",
    "nfhhe4988vs4h6l",
    "mgw15c3b5r05xfy",
    "f0zu3u89jiwov2v",
    "vsmyh9laggpzqxo",
    "b558yvepufk1huh",
    "l3q9zw749gfbanq",
    "ILoveShankar123",
    "6l9rkavo4rr7260",
    "6ux9um7tcexawq2",
    "sly59kby5t3nnym",
    "s3791waa25q52n3"
]

# Generate a new encryption key
key = Fernet.generate_key()

# Create a Fernet cipher suite using the generated key
cipher_suite = Fernet(key)

# Convert the activation codes to a single string
activation_codes_str = "\n".join(activation_codes)

# Encrypt the activation codes
encrypted_codes = cipher_suite.encrypt(activation_codes_str.encode())

# Save the encrypted activation codes to a file
with open("activation_codes.enc", "wb") as file:
    file.write(encrypted_codes)

# Print the generated encryption key
print("Encryption Key:")
print(key.decode())