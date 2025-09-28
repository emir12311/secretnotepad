# Secure Notes 🗒️🔒

This is a simple **password-protected notes program** I made in Python.  
It lets you create an account, log in securely, and write or edit notes that are **stored in an encoded format**.

## How the program works
1. When you run it, you’re asked for a **username**.  
2. If the username exists:
   - You must enter your password (3 attempts maximum).  
   - If correct, access is granted.  
3. If the username doesn’t exist:
   - You’re prompted to **create a new account**.  
   - Your password is saved as a SHA-256 hash.  
4. Once logged in:
   - If no notes exist, you can **write a new note**.  
   - If notes exist, you can **view, overwrite, or append** them.  
5. Notes are **base64-encoded** before saving (simple obfuscation).  
6. Account info and notes are stored in `keys.json`.

## What I learned while making it
- Working with `json` for storing user data.  
- Hashing passwords securely with `sha256`.  
- Encoding and decoding notes with `base64`.  
- Organizing code into functions for login, account creation, and editing.  
- Handling multiple user accounts and persistent data.

### Note 📝
Like my other projects, this is the **first version only**.  
I’m not improving or rewriting it unless it’s a really special project.  
This GitHub is meant to show my growth over time, from my earliest code to whatever I make in the future.
