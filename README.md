# Home Assistant SecureTar v3 Decryptor

A simple utility to decrypt and extract modern Home Assistant backups (SecureTar v3 format).

> **Note:** This was swiftly vibe-coded and is provided as a reference only. Anyone is welcome to use, fork, and contribute!

## Why this exists?
Starting in early 2026 (HA 2026.4), Home Assistant upgraded its backup encryption to use **libsodium secretstream (XChaCha20-Poly1305)** and **Argon2id** key derivation. Most existing "SecureTar" decryption scripts online only support the older AES-CBC format and will fail with "Invalid Magic Bytes" on newer backups.

This script uses the official `securetar` library to ensure compatibility with the latest standards.

## Requirements
- Python 3.9+
- `securetar` library

## Installation
```bash
pip install securetar
```

## Usage
Provide your **32-character Emergency Recovery Key** (e.g., `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`) and the path to your backup file.

```bash
python decrypt.py "YOUR-EMERGENCY-KEY" backup.tar.gz ./extracted_output
```

## Troubleshooting
- **Permission Denied (Windows):** If you are on Windows, some internal HA files (like those with `:` in the name from Xiaomi integrations) cannot be extracted to the Windows filesystem. Run this script inside **WSL** (Linux) to extract those files successfully.
- **Invalid Key:** Ensure you are using the full 32-character key found in your Home Assistant Settings.
