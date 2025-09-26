# Lab 13: Using Chrome DevTools – JavaScript Console

## Objectives

- Run JavaScript directly in the console.
- Read error messages and fix issues.
- Use `console.*` for debugging.

## Duration

30–40 minutes

## Materials Needed

- Google Chrome
- Sample page

## Instructions

1. **Create Files in `labs/lab13/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Console Practice</title>
       <script src="script.js" defer></script>
     </head>
     <body>
       <h1>Console Practice</h1>
       <p>Open DevTools → Console</p>
     </body>
   </html>
   ```

   `script.js` (with an error to fix):

   ```js
   // Intentional error:
   console.log(somethingiswrong);

   // Some data to explore:
   const people = [
     { name: 'Ada', role: 'Engineer' },
     { name: 'Grace', role: 'Scientist' },
     { name: 'Linus', role: 'Hacker' },
   ];

   // Try in console:
   // console.table(people);
   ```

2. **Open Console and Read the Error**

   - You'll see `ReferenceError: somethingiswrong is not defined`.

3. **Fix the Error**

   - Option A: define the variable:

   ```js
   const somethingiswrong = 'Nope, all good now!';
   console.log(somethingiswrong);
   ```

   - Option B: treat as string:

   ```js
   console.log('somethingiswrong');
   ```

   - Option C: remove the line.

4. **Explore Advanced Console Methods**

   ```js
   // Basic console methods
   console.log('Hello from console.log');
   console.error('This is an error message');
   console.warn('This is a warning');
   console.info('This is an info message');

   // Data display methods
   console.table(people);
   console.dir(people); // shows object structure

   // Grouping methods
   console.group('User Information');
   console.log('Name: Alice');
   console.log('Age: 25');
   console.log('Role: Developer');
   console.groupEnd();

   // Timing methods
   console.time('Performance Test');
   // Simulate some work
   for (let i = 0; i < 100000; i++) {
     Math.random();
   }
   console.timeEnd('Performance Test');

   // Trace method
   function functionA() {
     functionB();
   }
   function functionB() {
     console.trace('Call stack trace:');
   }
   functionA();
   ```

## Discussion and Sharing

- How did the console help identify the exact problem?
- When is `console.table` handy?
- How do `console.group()` and `console.time()` improve debugging?
- What information does `console.trace()` provide?
- Which console methods are most useful for different debugging scenarios?
