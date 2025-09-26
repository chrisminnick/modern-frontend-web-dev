# Lab 03: Controlling Your Versions with Git

## Objectives

- Understand the Git workflow: init, add, commit, branch, merge.
- Use branches to isolate work.
- (Optional) Push to GitHub.

## Duration

45–60 minutes

## Materials Needed

- Visual Studio Code
- Git installed
- GitHub account (optional)
- Course project folder

## Instructions

1. **Verify Git**

   ```bash
   git --version
   ```

2. **Initialize a Repo**

   ```bash
   cd labs/lab03
   git init
   ```

3. **Create & Commit a README**

   ```bash
   echo "# Lab 03: Controlling Your Versions with Git" > README.md
   git status
   git add README.md
   git commit -m "Initial commit with README"
   ```

4. **View History and Check Status**

   ```bash
   git status    # check current state (use this frequently!)
   git log       # view commit history
   git log --oneline  # compact view
   # press 'q' to quit log view
   ```

5. **Create and Use a Branch**

   ```bash
   git checkout -b feature-hello

   # add a file
   echo 'console.log("Hello, Git!");' > hello.js

   git add hello.js
   git commit -m "Add hello.js with greeting"
   ```

6. **Merge to Main**

   ```bash
   # if 'main' doesn't exist yet, create/switch to it
   git checkout -B main

   # merge feature branch
   git merge feature-hello

   # delete the branch
   git branch -d feature-hello
   ```

7. **View Differences Between Commits**

   ```bash
   # See what changed between commits
   git diff HEAD~1 HEAD    # compare last two commits
   git diff                # see unstaged changes
   git diff --staged       # see staged changes
   ```

8. **(Optional) Push to GitHub**
   ```bash
   # create an empty repo on GitHub (no README)
   git remote add origin https://github.com/YOUR-USERNAME/lab03.git
   git push -u origin main
   ```

## Discussion and Sharing

- How do branches protect `main` from unstable code?
- When should you make a new branch?
- How does `git diff` help you understand what changed?
- Why is `git status` considered essential for daily Git usage?
- Share your GitHub link if you pushed your repo.
