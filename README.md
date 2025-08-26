# 🔐 Caesar Cipher

A fun and interactive Python implementation of the classic Caesar Cipher encryption algorithm, complete with ASCII art! 🐼

## 🎯 What is Caesar Cipher?

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It's a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## ✨ Features

- 🎨 Beautiful ASCII art welcome screen
- � Interactive encryption and decryption
- 🔢 Custom shift values (1-25)
- 📝 Preserves spaces and special characters
- 🔁 Continuous operation mode
- 🎯 User-friendly command-line interface

## 🚀 How to Use

1. **Run the program:**
   ```bash
   python main.py
   ```

2. **Choose your operation:**
   - Type `encode` to encrypt your message
   - Type `decode` to decrypt your message

3. **Enter the shift number:**
   - Choose any number between 1-25
   - This determines how many positions each letter shifts

4. **Enter your message:**
   - Type the text you want to encrypt/decrypt
   - The program handles both uppercase and lowercase automatically

5. **Enjoy the output!** 🎉

6. **Continue or exit:**
   - Type `yes` to perform another operation
   - Type `no` to exit the program

## 📝 Example

```
Type 'encode' to ENCRYPT or 'decode' to DECRYPT:
encode
Type the shift number:
3
Type your Message:
hello world
Your encoded text is:  khoor zruog
```

## 🛠️ Requirements

- Python 3.x
- No additional dependencies required!

## 🎮 Just for Fun!

This project was created for educational purposes and fun! Perfect for:
- Learning about basic cryptography
- Understanding Caesar Cipher algorithm
- Python programming practice
- Having fun with secret messages! 🕵️‍♂️

## 📚 How it Works

The Caesar Cipher works by shifting each letter in the alphabet by a fixed number of positions:
- A → D (shift of 3)
- B → E (shift of 3)
- Z → C (shift of 3, wraps around)

The program maintains the original case and preserves non-alphabetic characters like spaces and punctuation.

Enjoy encoding and decoding your secret messages! 🎊
