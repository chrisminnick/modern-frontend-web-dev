# Lab 06: Creating a New Project with Vite

## Objectives

- Scaffold a modern project with Vite.
- Use Vite's dev server and HMR.
- Explore project structure.

## Duration

45–60 minutes

## Materials Needed

- Node.js (v20+)
- VSCode

## Instructions

1. **Create the Project**

   ```bash
   cd labs/lab06
   npm create vite@latest my-vite-app
   # Choose: Framework = Vanilla, Variant = JavaScript
   cd my-vite-app
   npm install
   ```

2. **Explore Files**

   - `index.html`, `main.js`, `style.css`, `package.json`

3. **Run the Dev Server**

   ```bash
   npm run dev
   ```

   - Open the shown URL (e.g., `http://localhost:5173/`).

4. **Edit for HMR**

   - Open `main.js` and replace content:

   ```js
   document.querySelector('#app').innerHTML = `
     <h1>Hello Vite!</h1>
     <p>This is my first project using Vite 🚀</p>
   `;
   ```

5. **Build for Production (Optional)**
   ```bash
   npm run build
   npm run preview
   ```

## Discussion and Sharing

- How does HMR speed up development?
- What's the benefit of separate dev and build scripts?
