# 🔒 Syntecxhub Password Manager

A secure, lightweight command-line password manager built with Python. This application encrypts and stores your passwords locally using military-grade encryption.

## ✨ Features

- **Military-Grade Encryption**: Uses Fernet symmetric encryption from the `cryptography` library
- **Master Password Protection**: Secure your entire vault with a single master password
- **Key Derivation**: PBKDF2 with SHA256 hashing (390,000 iterations) for strong key derivation
- **Local Storage**: All passwords stored encrypted locally in `vault.enc`
- **User-Friendly CLI**: Simple menu-driven interface for easy password management
- **Search Functionality**: Find passwords by site name
- **Secure Input**: Getpass module hides password input from terminal display

## 🔐 Security Features

- **Encryption Algorithm**: Fernet (symmetric encryption with AES)
- **Key Derivation Function**: PBKDF2-HMAC-SHA256 with 390,000 iterations
- **Salt**: 16-byte random salt for each vault
- **Secure Password Input**: Uses `getpass` module to hide user input
- **No Plain Text Storage**: Passwords are never stored unencrypted

## 📋 Requirements

- Python 3.7+
- `cryptography` library

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/beaucicotduchelinfresnel/Syntecxhub_Password-Manager.git
cd Syntecxhub_Password-Manager
```

2. Install dependencies:
```bash
pip install cryptography
```

3. Run the application:
```bash
python password_manager.py
```

## 📖 Usage

When you first run the application, you'll be prompted to create a master password:

```
Master password: ••••••••
```

Then you'll see the main menu:

```
1. Add        - Add a new password entry
2. Retrieve   - Retrieve a stored password
3. Delete     - Delete a password entry
4. Search     - Search for password entries
5. Exit       - Save and exit
```

### Example Workflow

**Adding a password:**
```
Choice: 1
Site: github.com
Username: myusername
Password: ••••••••
✅ Entry added.
```

**Retrieving a password:**
```
Choice: 2
Site: github.com
Username: myusername
Password: my_secure_password
```

**Searching for entries:**
```
Choice: 4
Search: git
🔍 Matches:
- github.com
```

**Deleting an entry:**
```
Choice: 3
Site: github.com
🗑️ Entry deleted.
```

## 🏗️ Architecture

### Core Components

- **`derive_key()`**: Generates encryption key from master password using PBKDF2
- **`load_vault()`**: Decrypts and loads password vault from encrypted file
- **`save_vault()`**: Encrypts and saves vault to disk
- **`add_entry()`**: Adds new password entry to vault
- **`retrieve_entry()`**: Retrieves and displays password
- **`delete_entry()`**: Removes password entry
- **`search_entries()`**: Searches vault by site name
- **`main()`**: Main loop handling user input

## 📁 File Structure

```
Syntecxhub_Password-Manager/
├── password_manager.py    # Main application
├── vault.enc              # Encrypted password vault (auto-generated)
└── README.md             # This file
```

## 🔑 Technical Details

### Encryption Flow

1. User enters master password
2. PBKDF2 derives a 32-byte encryption key from the master password
3. Fernet (AES-128) encrypts the vault JSON data
4. Salt + encrypted data saved to `vault.enc`

### Vault Storage Format

- **Bytes 0-15**: 16-byte salt (random)
- **Bytes 16+**: Fernet-encrypted JSON containing password entries

### Password Entry Structure

```json
{
  "github.com": {
    "username": "myusername",
    "password": "secure_password"
  },
  "gmail.com": {
    "username": "user@gmail.com",
    "password": "app_specific_password"
  }
}
```

## ⚠️ Security Considerations

- **Master Password**: Your master password is the key to all encrypted data. Choose a strong, unique password.
- **No Recovery**: There is no password recovery mechanism. If you forget your master password, all data is permanently inaccessible.
- **Secure Deletion**: When deleting entries, use secure file deletion tools for sensitive data.
- **Environment Security**: Run on a trusted, secure machine free from malware.
- **Backup**: Keep encrypted backups of `vault.enc` in a secure location.

## 🐛 Known Limitations

- Single master password (no multi-user support)
- CLI-only interface (no GUI)
- No password strength meter
- No automatic password generation
- No cloud sync capability
- No two-factor authentication

## 🚀 Future Enhancements

- [ ] GUI interface using PyQt or Tkinter
- [ ] Password strength meter
- [ ] Automatic password generation
- [ ] Master password change functionality
- [ ] Data export/import
- [ ] Cloud sync with end-to-end encryption
- [ ] Two-factor authentication
- [ ] Password expiration warnings
- [ ] Audit log

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Beaucicot Duchelinfresnel**
- GitHub: [@beaucicotduchelinfresnel](https://github.com/beaucicotduchelinfresnel)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

**Disclaimer**: This password manager is provided as-is for educational purposes. While it implements industry-standard encryption practices, use at your own risk. Always maintain secure backups of your passwords independently.
