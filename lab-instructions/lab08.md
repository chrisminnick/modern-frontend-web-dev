# Lab 08: Using Chrome Developer Tools – Sources Panel (JavaScript Debugging)

## Objectives

- Set breakpoints and step through code.
- Inspect variables and call stack.
- Use the Console alongside the debugger.

## Duration

40–50 minutes

## Materials Needed

- Google Chrome
- VSCode + Live Server (or Vite)

## Instructions

1. **Create Files in `labs/lab08/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Countdown Bug</title>
     </head>
     <body>
       <h1>JavaScript Rocket Launcher</h1>
       <button id="launch">Start the Countdown!</button>
       <p>Time remaining: <span id="timer">10</span></p>
       <script src="script.js"></script>
     </body>
   </html>
   ```

   `script.js` (with a bug):

   ```js
   const launchBtn = document.getElementById('launch');
   const timerEl = document.getElementById('timer');

   function startTimer(start = 10) {
     let timer = start;
     const id = setInterval(() => {
       // BUG: we decrement before checking, which skips 0 properly
       timer--; // <-- suspect line
       timerEl.textContent = timer; // shows updated time
       if (timer === 0) {
         // may never hit as expected
         clearInterval(id);
         console.log('🚀 Lift off!');
       }
     }, 1000);
   }

   function init() {
     launchBtn.addEventListener('click', startTimer);
   }

   init();
   ```

2. **Open DevTools → Sources**

   - Set a line‑of‑code breakpoint on the `timer--` line.
   - Click **Start the Countdown!**; execution pauses.

3. **Step Through**

   - Use **Step Over / Step Into / Step Out** buttons.
   - Observe **Scope** variables; run quick tests in **Console**:

   ```js
   timer; // what is its value now?
   ```

4. **Fix In DevTools**

   - Edit code (temporarily) in Sources to check first, then decrement:

   ```js
   if (timer === 0) {
     clearInterval(id);
     console.log('🚀 Lift off!');
   }
   timer--;
   ```

   - Resume and verify behavior, then apply the same fix in `script.js` using VSCode and save.

5. **Advanced Debugging Features**
   - Try conditional breakpoints: right-click on line number, set condition like `timer < 5`
   - Add watch expressions in the **Watch** panel to monitor variables
   - Explore the **Call Stack** to understand function execution flow

## Discussion and Sharing

- How do breakpoints compare to `console.log` debugging?
- When would you step **into** vs **over**?
- How do conditional breakpoints improve debugging efficiency?
- What's the benefit of watch expressions over console logging?
