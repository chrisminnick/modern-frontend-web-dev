# Lab 07: Using Chrome Developer Tools – Elements Panel

## Objectives

- Inspect and modify HTML/CSS live with DevTools.
- Understand temporary edits vs saved files.

## Duration

30–40 minutes

## Materials Needed

- Google Chrome
- VSCode + Live Server (or Vite)

## Instructions

1. **Create Files in `labs/lab07/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>DevTools Lab</title>
       <link rel="stylesheet" href="style.css" />
     </head>
     <body>
       <h1>Welcome to Modern Front-End Web Development</h1>
       <p>This is a practice page for exploring Chrome DevTools.</p>
     </body>
   </html>
   ```

   `style.css`:

   ```css
   body {
     font-family: Arial, sans-serif;
     background-color: #f4f4f4;
     padding: 20px;
   }
   h1 {
     color: darkblue;
   }
   p {
     font-size: 18px;
     color: gray;
   }
   ```

2. **Open with Live Server**

   - Right‑click `index.html` → **Open with Live Server**.

3. **Open DevTools**

   - **F12** or **Cmd+Opt+I / Ctrl+Shift+I**, then select **Elements**.

4. **Edit HTML & CSS in DevTools**

   - Right‑click `<h1>` → **Edit as HTML**, change text.
   - In **Styles** panel, change `color` to `crimson` and add:

   ```css
   text-transform: uppercase;
   ```

5. **Reload to Reset**
   - Refresh to revert changes (they're temporary).

## Discussion and Sharing

- How does live editing speed up troubleshooting?
- Why don't DevTools edits persist?
