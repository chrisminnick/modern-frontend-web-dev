# Lab 04: Initializing npm

## Objectives

- Initialize npm and explore `package.json`.
- Add scripts.
- Install and use a simple dependency.

## Duration

30–40 minutes

## Materials Needed

- Node.js (v20+)
- VSCode
- Project folder

## Instructions

1. **Initialize npm**

   ```bash
   cd labs/lab04
   npm init -y
   ```

2. **Set ESM (so you can use `import` in Node)**

   - Open `package.json` and add `"type": "module"` (if not present):

   ```json
   {
     "name": "lab04",
     "version": "1.0.0",
     "type": "module",
     "scripts": {
       "dev": "echo \"Running dev server...\""
     }
   }
   ```

3. **Run a Script**

   ```bash
   npm run dev
   ```

4. **Install a Package**

   ```bash
   npm install dayjs
   ```

5. **Use the Package**

   - Create `index.js`:

   ```js
   import dayjs from 'dayjs';

   console.log('The current date and time is:', dayjs().format());
   ```

   - Run:

   ```bash
   node index.js
   ```

6. **Understanding Dependencies and Versioning**

   ```bash
   # View dependency tree
   npm ls

   # Check package versions
   cat package.json | grep dayjs
   ```

   - Learn about semantic versioning (semver):
     - `1.2.3` = MAJOR.MINOR.PATCH
     - `^1.2.3` = compatible within major version
     - `~1.2.3` = compatible within minor version

## Discussion and Sharing

- Why is `package.json` important?
- How does npm simplify sharing a project?
- What's the difference between `^` and `~` in version ranges?
- How does semantic versioning help prevent breaking changes?
- What other scripts might you add later?
