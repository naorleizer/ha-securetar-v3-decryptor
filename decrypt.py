#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from securetar import SecureTarFile

def main():
    parser = argparse.ArgumentParser(description="Decrypt Home Assistant SecureTar v3 backups.")
    parser.add_argument("password", help="The 32-character Emergency Recovery Key or backup password.")
    parser.add_argument("input", help="The path to the encrypted .tar.gz backup file.")
    parser.add_argument("output", help="The directory where the files should be extracted.")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)
        
    if not output_path.exists():
        output_path.mkdir(parents=True)

    print(f"Decrypting and extracting '{input_path.name}'...")
    
    try:
        # SecureTarFile handles the v3 Argon2id derivation and XChaCha20 decryption automatically
        with SecureTarFile(name=input_path, password=args.password) as tar:
            tar.extractall(path=output_path)
        print(f"\nExtraction complete! Files are in: {output_path.absolute()}")
        
    except Exception as e:
        print(f"\nDecryption/Extraction failed: {e}")
        print("\nPossible issues:")
        print("1. Incorrect key (it should be 32 characters, separated by dashes).")
        print("2. Filesystem limitations (run in WSL/Linux if extracting files with ':' in names).")
        sys.exit(1)

if __name__ == "__main__":
    main()
