# Lab 02: Using Visual Studio Code Basics

## Objectives

- Create, open, and edit files in VSCode.
- Explore syntax highlighting, Emmet, and extensions.
- Learn Markdown syntax for documentation and note-taking.
- Customize VSCode for front-end development.

## Duration

45–60 minutes

## Materials Needed

- Visual Studio Code installed
- Course project folder opened in VSCode
- Recommended extensions: **Live Server**, **Prettier**, **ESLint**

## Instructions

1. **Open Your Project Folder**

   - **File > Open Folder…** → choose `modern-frontend-web-dev` (or your workspace).

2. **Create an HTML File**

   - In `labs/lab02/`, create `hello.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Hello VSCode</title>
     </head>
     <body>
       <h1>Hello, Visual Studio Code!</h1>
       <p>This is my first page created in VSCode.</p>
       <!-- Try Emmet below: type 'ul>li*3' and press Tab -->
     </body>
   </html>
   ```

3. **Preview with Live Server**

   - Right‑click `hello.html` → **Open with Live Server**.

4. **Use Emmet**

   - Inside `<body>`, type:

   ```
   ul>li*3
   ```

   - Press **Tab** to expand:

   ```html
   <ul>
     <li></li>
     <li></li>
     <li></li>
   </ul>
   ```

5. **Install & Use Extensions**

   - Extensions panel → install **Prettier** and **ESLint**.
   - Format document: **Right‑click > Format Document** (Prettier).

6. **Open the Integrated Terminal**

   ```bash
   ls    # or: dir
   ```

7. **Master Essential VSCode Features**

   - Open Command Palette: **Cmd+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows/Linux)
   - Try these useful shortcuts:
     - **Cmd+D** / **Ctrl+D**: Select next occurrence of current word
     - **Cmd+Shift+L** / **Ctrl+Shift+L**: Select all occurrences
     - **Cmd+/** / **Ctrl+/**: Toggle line comment
     - **Alt+Shift+Down** / **Shift+Alt+Down**: Duplicate line

8. **Learn Markdown for Documentation**

   - Install the **Markdown Preview Enhanced** extension
   - Create `notes.md` in your `labs/lab02/` folder:

   ````markdown
   # My VSCode Learning Notes

   ## What I Learned Today

   - How to use **Emmet** for faster HTML writing
   - VSCode shortcuts that save time
   - Installing and using extensions

   ## Useful Extensions

   1. **Live Server** - for previewing HTML files
   2. **Prettier** - for code formatting
   3. **Markdown Preview Enhanced** - for viewing Markdown files

   ## Code Example

   Here's some HTML I created with Emmet:

   ```html
   <ul>
     <li>Item 1</li>
     <li>Item 2</li>
     <li>Item 3</li>
   </ul>
   ```
   ````

   ## Next Steps

   - [ ] Try more Emmet shortcuts
   - [ ] Explore more VSCode extensions
   - [ ] Practice keyboard shortcuts

   > **Tip**: Use Markdown for all your project documentation!

   ```

   - Right-click `notes.md` → **Open Preview to the Side**
   - See your formatted Markdown in real-time!

   ```

9. **Markdown Syntax Reference**

   Practice these common Markdown elements:

   ````markdown
   # Heading 1

   ## Heading 2

   ### Heading 3

   **Bold text** and _italic text_

   - Unordered list item
   - Another item
     - Nested item

   1. Ordered list item
   2. Another ordered item

   [Link text](https://example.com)

   `inline code` and:

   ```javascript
   // Code block
   console.log('Hello, Markdown!');
   ```
   ````

   > Blockquote for important notes

   | Column 1 | Column 2 |
   | -------- | -------- |
   | Data 1   | Data 2   |

   ```

   ```

## Discussion and Sharing

- How do syntax highlighting and Emmet improve productivity?
- Which keyboard shortcuts do you find most useful?
- How does the Command Palette speed up your workflow?
- Which extensions do you find most helpful?
- Why is editor mastery important early on?
- **Markdown Questions:**
  - How could Markdown improve your project documentation?
  - What advantages does Markdown have over plain text or Word documents?
  - When would you use Markdown in web development projects?
