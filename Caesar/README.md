# 🔐 Caesar Cipher

A modern, user-friendly GUI application for encrypting and decrypting messages using the Caesar Cipher algorithm.

## 📖 Description

The Caesar Cipher is one of the oldest and simplest encryption techniques. This application provides an intuitive graphical interface to encode and decode messages by shifting each letter in the alphabet by a specified number of positions.

## ✨ Features

- **Modern GUI Interface**: Clean, dark-themed interface built with Tkinter
- **Encode & Decode**: Easily encrypt or decrypt messages with a single click
- **Adjustable Shift**: Choose shift values from 1 to 25
- **Copy to Clipboard**: Quickly copy results with the built-in copy button
- **Case Insensitive**: Automatically handles uppercase and lowercase letters
- **Special Character Preservation**: Non-alphabetic characters remain unchanged

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone or download this repository to your local machine

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Simply run the main script:
```bash
python ceasar.py
```

## 🎮 Usage

1. **Enter your message** in the "Your Message" text box
2. **Set the shift amount** using the spinner (default is 3)
3. **Click ENCODE** to encrypt your message or **DECODE** to decrypt it
4. **View the result** in the output text box
5. **Copy the result** to clipboard using the 📋 button
6. **Clear all** fields using the "Clear All" button

### Example

**Original Message:** `hello world`  
**Shift:** `3`  
**Encoded Message:** `khoor zruog`

To decode, simply enter `khoor zruog` and click DECODE with the same shift value.

## 🔧 How It Works

The Caesar Cipher works by shifting each letter in the message by a fixed number of positions in the alphabet:
- For encoding: each letter moves forward by the shift amount
- For decoding: each letter moves backward by the shift amount
- The alphabet wraps around (e.g., z + 1 = a)

## 📦 Project Structure

```
Caesar/
├── ceasar.py       # Main application file with GUI
├── README.md       # This file
└── requirements.txt # Python dependencies
```

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **Tkinter**: GUI framework (included with Python)
- **Pyperclip**: Clipboard operations

## 🎨 Color Scheme

The application uses a modern Catppuccin-inspired dark theme for comfortable viewing.

## 📝 Note

This is a simple encryption method meant for educational purposes and basic message obfuscation. It should **not** be used for securing sensitive information as it can be easily broken with frequency analysis or brute force attacks.

## 👨‍💻 Author

Created as part of a Udemy Python course project.

## 📄 License

This project is free to use for educational purposes.
