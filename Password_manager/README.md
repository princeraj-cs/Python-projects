# 🔐 Password Manager

A secure and user-friendly password manager built with Python and Tkinter that helps you generate strong passwords and store your credentials safely.

## ✨ Features

- 🎲 **Random Password Generator** - Creates strong, random passwords with letters, numbers, and symbols
- 💾 **Secure Storage** - Saves your passwords locally in an organized format
- 📋 **Auto-Copy to Clipboard** - Generated passwords are automatically copied for easy pasting
- ✅ **Input Validation** - Ensures no fields are left empty before saving
- 🖼️ **Clean GUI** - Simple and intuitive graphical user interface
- ⚠️ **Confirmation Dialogs** - Double-check before saving credentials

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You'll also need the following Python packages:

```bash
pip install pyperclip
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Python-projects.git
cd Python-projects/Password_manager
```

2. Ensure you have a `logo.png` file in the same directory as `main.py`

3. Run the application:
```bash
python main.py
```

## 🎮 How to Use

1. **Enter Website Name** - Type the website or service name for which you want to store credentials
2. **Enter Email/Username** - Your email or username (default: xyz@gmail.com)
3. **Generate Password** - Click "Generate Password" button to create a strong random password
4. **Save Credentials** - Click "Add" button to save your credentials
5. **Confirm** - Review the information in the confirmation dialog and click OK to save

## 🔑 Password Generation

The password generator creates strong passwords with:
- 8-10 random letters (uppercase and lowercase)
- 2-4 random numbers
- 2-4 random symbols
- All characters are shuffled for maximum security

## 📁 Data Storage

Credentials are stored in `password.txt` in the following format:
```
Website | Email | Password
```

## 🛡️ Security Note

⚠️ **Important**: This is a basic password manager that stores passwords in plain text. For production use, consider implementing:
- Password encryption
- Master password protection
- Database storage instead of text files
- Additional security measures

## 🖥️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework
- **pyperclip** - Clipboard functionality
- **random** - Password generation

## 📸 Screenshot

The application features a clean interface with:
- Logo image at the top
- Input fields for website, email, and password
- Generate Password button
- Add button to save credentials

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📝 License

This project is open source and available under the [MIT License](../LICENSE).

## 👨‍💻 Author

Created as part of a Python projects collection.

---

⭐ If you find this project helpful, please consider giving it a star!
