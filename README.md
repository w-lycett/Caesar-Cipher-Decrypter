# Caesar-Cipher-Decrypter
A program for decrypting ciphertext encoded using a Caesar cipher with an unknown shift value, complete with a flexible GUI.

## Overview
I wanted to challenge myself with producing a small but useful application using the MVC architecture often used in industry. All processing is contained in 'decryptionModel.py' while all GUI formatting is contained in 'decryptionView.py', with neither of them interacting directly thanks to 'decryptionController.py'. The program has also been built robustly and won't terminate ungracefully, e.g., if no input has been given.

## Features
- Decrypt Caesar ciphertext instantly, without knowing the key used.
- GUI-based output with flexibility when resized.
- Access a help menu that explains the application.

## Requirements
- Python 3.13+
- (Optional) Virtual environment tool (venv)
- OS: Windows / macOS / Linux

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/w-lycett/Caesar-Cipher-Decrypter.git
   cd Caesar-Cipher-Decrypter
   ```

2. (Recommended) Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
   ```
   venv\Scripts\activate
   ```
   - macOS / Linux:
   ```
   source venv/bin/activate
   ```

4. Run the application from the controller:
   ```
   python -m decryptionController
   ```
   The GUI for the program should then appear.

5. When finished, exit the GUI window and deactive your virtual environment (if used):
   ```
   deactivate
   ```

## Contributing
Pull requests welcome.
