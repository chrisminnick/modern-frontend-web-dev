# Modern Frontend Web Development - Setup Guide

## Course Requirements

To complete the labs in this course, you will need:

- A computer with **macOS**, **Windows**, or **Linux**
- Access to the **Internet**
- A **modern web browser** (Chrome recommended)
- **Administrator privileges** to install software globally

---

## Setup Instructions

Follow these steps to set up your development environment:

### ✅ Step 1: Install Visual Studio Code

Install the free Visual Studio Code editor:

- **Download:** [https://code.visualstudio.com](https://code.visualstudio.com)
- **Installation:** Run the installer and follow the default options
- **Platform Notes:** Available for Windows, macOS, and Linux

### ✅ Step 2: Install Google Chrome

Ensure Google Chrome is installed and set as your default browser:

- **Download:** [https://www.google.com/chrome/](https://www.google.com/chrome/)
- **Set as Default:** Make Chrome your default browser for consistent development experience

### ✅ Step 3: Install Git

Install Git version control system:

**macOS:**

- Git comes pre-installed on macOS
- Verify installation: Open Terminal and run `git --version`

**Windows:**

- **Download:** [http://git-scm.com](http://git-scm.com)
- **Installation:** Select all default options during installation
- **Verify:** Open Command Prompt and run `git --version`

**Linux:**

```bash
sudo apt update
sudo apt install git
```

### ✅ Step 4: Install Node.js

Install Node.js version 20 or newer:

- **Download:** [https://nodejs.org/en/download](https://nodejs.org/en/download)
- **Version:** Choose the **LTS (Long Term Support)** version
- **Installation:** Run the installer and select all default options
- **Verify:** Open terminal/command prompt and run:
  ```bash
  node --version
  npm --version
  ```

### ✅ Step 5: Download Course Files

Open a terminal/command prompt in your home directory and clone the course repository:

```bash
git clone https://github.com/chrisminnick/modern-frontend-web-dev
```

**Platform-specific instructions:**

- **Windows:** Open Command Prompt or PowerShell
- **macOS/Linux:** Open Terminal

### ✅ Step 6: Open Project in VSCode

1. **Launch VSCode**
2. Select **File > Open Folder** from the menu
3. Navigate to and open the `modern-frontend-web-dev` folder you downloaded in Step 5

### ✅ Step 7: Install Recommended Extensions

When you open the project, VSCode should display a popup asking to install recommended extensions:

- **If popup appears:** Click **"Install All"**
- **If no popup:**
  1. Click the **Extensions** icon in the left sidebar (📦)
  2. Look for the **"Recommended"** section
  3. Install all recommended extensions

**Key Extensions Include:**

- Live Server
- Prettier - Code formatter
- ESLint
- Auto Rename Tag

### ✅ Step 8: Test Your Setup

1. **Open Terminal in VSCode:**

   - Select **Terminal > New Terminal** from the menu
   - Or use keyboard shortcut: `Ctrl+` `(Windows/Linux) or`Cmd+` ` (macOS)

2. **Navigate to test directory and run setup test:**

   ```bash
   cd setup-test
   npm install
   npm run dev
   ```

3. **Verify Success:**
   - You should see output similar to:
     ```
     ➜  Local:   http://localhost:5173/
     ➜  Network: use --host to expose
     ```
   - **Click the link** or copy `http://localhost:5173` into your browser
   - You should see a **"Success!"** message with a functional button

### ✅ Step 9: Stop the Development Server

When finished testing, stop the server:

- Press `Ctrl+C` (Windows/Linux) or `Cmd+C` (macOS) in the terminal

---

## Troubleshooting

### Common Issues and Solutions

**Problem:** `git` command not found

- **Solution:** Restart terminal/command prompt after Git installation
- **Windows:** Ensure Git was added to PATH during installation

**Problem:** `node` or `npm` command not found

- **Solution:** Restart terminal/command prompt after Node.js installation
- **Verify PATH:** Node.js should be added to system PATH automatically

**Problem:** Permission errors during `npm install`

- **Solution:** Ensure you have administrator/sudo privileges
- **macOS/Linux:** Try `sudo npm install` if needed

**Problem:** Port 5173 already in use

- **Solution:** Kill existing processes or use different port:
  ```bash
  npm run dev -- --port 3000
  ```

**Problem:** Extensions not installing

- **Solution:**
  1. Check internet connection
  2. Manually search and install extensions from VSCode marketplace
  3. Restart VSCode after installation

### Getting Help

- **Course Repository:** [https://github.com/chrisminnick/modern-frontend-web-dev](https://github.com/chrisminnick/modern-frontend-web-dev)
- **VSCode Documentation:** [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- **Node.js Documentation:** [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)

---

## Next Steps

Once your setup is complete:

1. **Explore the Project Structure:** Familiarize yourself with the course files
2. **Start Lab 01:** Working with the Command Line in VSCode
3. **Join Course Communications:** Connect with your instructor and classmates

**🎉 Congratulations! Your development environment is ready for modern frontend web development!**
