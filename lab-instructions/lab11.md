# Lab 11: Positioning with CSS (and Flexbox)

## Objectives

- Understand normal flow, relative/absolute/fixed positioning.
- Build a simple layout with Flexbox.

## Duration

45–60 minutes

## Materials Needed

- VSCode
- Live Server (or Vite)

## Instructions

1. **Create Files in `labs/lab11/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Positioning & Flexbox</title>
       <link rel="stylesheet" href="style.css" />
     </head>
     <body>
       <nav class="nav">My Fixed Nav</nav>

       <section class="stage">
         <img
           src="https://via.placeholder.com/150"
           alt="astronaut"
           class="pic pic-1"
         />
         <img
           src="https://via.placeholder.com/120"
           alt="dinosaur"
           class="pic pic-2"
         />
         <p class="blurb">This is a paragraph of text.</p>
         <div class="box">This is a div</div>
       </section>

       <div class="sticky-nav">Sticky Navigation - Scroll to see it stick!</div>

       <section class="flex-demo">
         <div class="card">Card 1 (Flexbox)</div>
         <div class="card">Card 2 (Flexbox)</div>
         <div class="card">Card 3 (Flexbox)</div>
       </section>

       <section class="grid-demo">
         <div class="grid-item">Grid Item 1</div>
         <div class="grid-item">Grid Item 2</div>
         <div class="grid-item">Grid Item 3</div>
         <div class="grid-item">Grid Item 4</div>
       </section>

       <!-- Add some content to make scrolling meaningful -->
       <div
         style="height: 1000px; padding: 2rem; background: linear-gradient(to bottom, #f8f9fa, #e9ecef);"
       >
         <h2>Scroll down to see the sticky navigation in action!</h2>
         <p>
           This section has extra height to demonstrate the sticky positioning.
         </p>
       </div>
     </body>
   </html>
   ```

   `style.css`:

   ```css
   body {
     margin: 0;
     font-family: system-ui, sans-serif;
   }

   /* fixed positioning */
   .nav {
     position: fixed;
     top: 0;
     left: 0;
     right: 0;
     height: 56px;
     background: #222;
     color: #fff;
     display: flex;
     align-items: center;
     padding: 0 1rem;
     z-index: 10;
   }

   .stage {
     margin-top: 72px;
     position: relative;
     min-height: 400px;
   }

   /* relative and absolute positioning */
   .pic {
     position: absolute;
     left: 50px;
   }
   .pic-1 {
     top: 50px;
   }
   .pic-2 {
     top: 140px;
     left: 220px;
   }

   .blurb {
     background: yellow;
     width: 220px;
     height: 100px;
     position: relative;
     top: 240px;
     left: 370px;
     padding: 0.5rem;
   }

   .box {
     background: red;
     width: 200px;
     height: 200px;
     position: relative;
     top: 150px;
     left: 40px;
     color: #fff;
     display: grid;
     place-items: center;
   }

   /* Flexbox layout */
   .flex-demo {
     display: flex;
     gap: 1rem;
     padding: 1rem;
     margin: 2rem 1rem;
     border-top: 1px solid #ccc;
     flex-wrap: wrap;
     justify-content: center;
   }

   .card {
     flex: 1 1 220px;
     min-height: 120px;
     background: #f5f5f5;
     border: 1px solid #ddd;
     border-radius: 0.5rem;
     display: grid;
     place-items: center;
   }

   /* CSS Grid example */
   .grid-demo {
     display: grid;
     grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
     gap: 1rem;
     padding: 1rem;
     margin: 2rem 1rem;
     border-top: 2px solid #333;
   }

   .grid-item {
     background: linear-gradient(45deg, #667eea, #764ba2);
     color: white;
     padding: 2rem;
     border-radius: 0.5rem;
     display: flex;
     align-items: center;
     justify-content: center;
     min-height: 100px;
   }

   /* Sticky positioning example */
   .sticky-nav {
     position: sticky;
     top: 56px; /* below the fixed nav */
     background: rgba(255, 255, 255, 0.9);
     backdrop-filter: blur(10px);
     padding: 0.5rem 1rem;
     border-bottom: 1px solid #ddd;
     z-index: 5;
   }

   @media (max-width: 600px) {
     .stage {
       min-height: 480px;
     }
   }
   ```

2. **Experiment**
   - Adjust `top/left` on absolutely positioned elements.
   - Observe how fixed nav stays during scroll.
   - Resize browser to see Flexbox responsiveness.
   - Scroll down to see sticky navigation behavior.
   - Compare CSS Grid vs Flexbox layouts.

## Discussion and Sharing

- When is absolute positioning appropriate?
- Why is Flexbox often preferred for modern layout?
- How does CSS Grid differ from Flexbox, and when would you use each?
- What's the difference between `position: sticky` and `position: fixed`?
- How does `backdrop-filter` enhance modern UI design?
