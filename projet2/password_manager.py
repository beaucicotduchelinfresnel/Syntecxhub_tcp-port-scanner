import json
import os
import base64
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken

VAULT_FILE = "vault.enc"
ITERATIONS = 390000


def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    return base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )


def load_vault(master_password: str):
    if not os.path.exists(VAULT_FILE):
        salt = os.urandom(16)
        key = derive_key(master_password, salt)
        return {}, salt, key

    with open(VAULT_FILE, "rb") as f:
        data = f.read()

    salt = data[:16]
    encrypted = data[16:]

    key = derive_key(master_password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted)
        vault = json.loads(decrypted.decode())
        return vault, salt, key
    except InvalidToken:
        print("❌ Master password incorrect.")
        exit(1)


def save_vault(vault: dict, salt: bytes, key: bytes):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(json.dumps(vault).encode())

    with open(VAULT_FILE, "wb") as f:
        f.write(salt + encrypted)


def add_entry(vault):
    site = input("Site: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    vault[site] = {
        "username": username,
        "password": password
    }
    print("✅ Entry added.")


def retrieve_entry(vault):
    site = input("Site: ")
    entry = vault.get(site)

    if entry:
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")
    else:
        print("❌ Entry not found.")


def delete_entry(vault):
    site = input("Site: ")
    if site in vault:
        del vault[site]
        print("🗑️ Entry deleted.")
    else:
        print("❌ Entry not found.")


def search_entries(vault):
    keyword = input("Search: ").lower()
    results = [s for s in vault if keyword in s.lower()]

    if results:
        print("🔍 Matches:")
        for r in results:
            print(f"- {r}")
    else:
        print("❌ No matches.")


def main():
    master_password = getpass.getpass("Master password: ")
    vault, salt, key = load_vault(master_password)

    while True:
        print("\n1. Add")
        print("2. Retrieve")
        print("3. Delete")
        print("4. Search")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_entry(vault)
        elif choice == "2":
            retrieve_entry(vault)
        elif choice == "3":
            delete_entry(vault)
        elif choice == "4":
            search_entries(vault)
        elif choice == "5":
            save_vault(vault, salt, key)
            print("🔒 Vault saved. Bye.")
            break
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
