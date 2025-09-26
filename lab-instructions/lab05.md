# Lab 05: Using npm

## Objectives

- Install, update, and remove packages.
- Distinguish local vs global installs.
- Use `npx` to run tools without global installs.

## Duration

45–60 minutes

## Materials Needed

- Node.js (v20+)
- VSCode
- Project folder (`labs/lab05`), npm initialized with `"type": "module"`

## Instructions

1. **Verify npm**

   ```bash
   npm -v
   ```

2. **Local Install (lodash)**

   ```bash
   cd labs/lab05
   npm init -y
   # ensure ESM
   npm pkg set type=module

   npm install lodash
   ```

3. **Use lodash**

   - Create `index.js`:

   ```js
   import _ from 'lodash';

   const numbers = [10, 20, 30, 40, 50];
   console.log('Shuffled numbers:', _.shuffle(numbers));
   ```

   - Run:

   ```bash
   node index.js
   ```

4. **Dev Dependency (Prettier)**

   ```bash
   npm install --save-dev prettier
   ```

   - Run with `npx`:

   ```bash
   npx prettier --write index.js
   ```

5. **Update & Remove Packages**

   ```bash
   # Check for outdated packages
   npm outdated

   # Update packages
   npm update

   # Remove packages
   npm uninstall lodash
   ```

6. **Global vs Local Installs**

   ```bash
   # global (system-wide) example
   npm install -g http-server
   http-server

   # without global install
   npx http-server
   ```

## Discussion and Sharing

- Why prefer local installs for project dependencies?
- When would a global install be appropriate?
- How does `npm outdated` help maintain your project?
- What's the difference between `^1.2.3` and `~1.2.3` version ranges?
- Pros/cons of `npx` vs global tools?
