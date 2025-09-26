# Lab 01: Working with the Command Line in VSCode

## Objectives

- Open and use the integrated terminal in Visual Studio Code.
- Practice basic command line navigation and file management.
- Build confidence with commands used later for Git, npm, and project setup.

## Duration

30–40 minutes

## Materials Needed

- Visual Studio Code installed
- Node.js installed
- Git installed
- Course project files (or any working directory)

## Instructions

1. **Open the Integrated Terminal**

   - VSCode → **Terminal > New Terminal**. The terminal opens at your workspace root.

2. **Check Your Current Directory**

   ```bash
   pwd
   ```

3. **List Files and Folders**

   ```bash
   ls
   # Windows alternative:
   dir
   ```

4. **Change Directories**

   ```bash
   cd labs/lab01
   ls
   ```

5. **Create, View, Copy, Move, and Delete Files**

   ```bash
   # create
   touch notes.txt

   # view
   cat notes.txt

   # copy
   cp notes.txt copy.txt

   # move/rename
   mv copy.txt renamed.txt

   # make a directory
   mkdir practice

   # move files into a folder
   mv notes.txt renamed.txt practice/

   # delete a file
   rm practice/renamed.txt
   ```

6. **Go "Up" a Directory**

   ```bash
   cd ..
   ```

7. **Tab Completion and Help**

   - Type `cat no` then press **Tab** to auto-complete `notes.txt` (if present).
   - Use `--help` for command help:

   ```bash
   ls --help
   ```

8. **Understanding Paths and Command History**
   - Learn about absolute vs relative paths:
   ```bash
   pwd                    # shows absolute path
   cd ../..              # relative path (go up two directories)
   cd /Users/yourname    # absolute path
   ```
   - View command history:
   ```bash
   history               # see previous commands
   # Use up/down arrows to navigate through history
   ```

## Discussion and Sharing

- Which commands were most useful?
- How does tab completion speed up your workflow?
- What's the difference between absolute and relative paths?
- Why do developers still rely on the command line with powerful GUIs available?
