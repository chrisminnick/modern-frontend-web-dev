# Lab 10: Using CSS Selectors

## Objectives

- Practice type, class, ID, attribute, and pseudo selectors.
- Style a page without changing its HTML.

## Duration

30–40 minutes

## Materials Needed

- VSCode
- Live Server (or Vite)

## Instructions

1. **Create Files in `labs/lab10/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Selectors Practice</title>
       <link rel="stylesheet" href="css/style.css" />
     </head>
     <body>
       <header>
         <h1 id="title">A Modest Practice</h1>
         <h3 class="subhead">by Jonathan Swift (1729)</h3>
         <h3 id="pubdate">1729</h3>
         <hr />
       </header>

       <main>
         <p>First paragraph. This one will be larger.</p>
         <p>Subsequent paragraphs should be indented.</p>
         <p>
           Another paragraph with a
           <a href="https://example.com" target="_blank">link</a>.
         </p>
         <ul class="items">
           <li>Alpha</li>
           <li>Beta</li>
           <li>Gamma</li>
         </ul>
       </main>
     </body>
   </html>
   ```

   `css/style.css`:

   ```css
   /* element selector */
   p {
     font-family: sans-serif;
   }

   /* class selector */
   .subhead {
     font-style: italic;
   }

   /* multiple selectors */
   h1,
   h2,
   h3 {
     text-align: center;
   }

   /* id selector */
   #pubdate {
     background-color: gray;
     color: white;
     width: 300px;
     margin-left: auto;
     margin-right: auto;
   }

   /* pseudo-class selector */
   p:first-of-type {
     font-size: 24px;
   }

   /* indent subsequent paragraphs */
   p:not(:first-of-type) {
     text-indent: 2em;
   }

   /* attribute selector */
   a[target='_blank'] {
     text-decoration: underline;
   }

   /* pseudo-element example: initial cap */
   p:first-of-type::first-letter {
     font-size: 200%;
     font-weight: bold;
   }

   /* center the hr */
   hr {
     width: 50%;
     margin: 1rem auto;
   }

   /* Advanced selectors - nth-child examples */
   .items li:nth-child(odd) {
     background-color: #f0f0f0;
   }

   .items li:nth-child(2) {
     font-weight: bold;
     color: darkblue;
   }

   /* Sibling combinators */
   h1 + h3 {
     margin-top: -10px; /* reduce space after h1 if followed by h3 */
   }

   h3 ~ hr {
     border-color: darkblue; /* style hr that comes after any h3 */
   }

   /* Modern :has() selector (where supported) */
   header:has(#pubdate) {
     border: 2px solid #ccc;
     padding: 1rem;
     border-radius: 8px;
   }
   ```

2. **Open with Live Server and Verify Styles**

3. **Update HTML to demonstrate advanced selectors**
   - Update the list items to show nth-child effects:
   ```html
   <ul class="items">
     <li>Alpha (odd - should be gray)</li>
     <li>Beta (even, 2nd child - should be bold blue)</li>
     <li>Gamma (odd - should be gray)</li>
     <li>Delta (even)</li>
     <li>Epsilon (odd - should be gray)</li>
   </ul>
   ```

## Discussion and Sharing

- Which selectors reduced the most HTML changes?
- How do pseudo-classes and pseudo-elements differ?
- What's the advantage of `:nth-child()` over adding classes?
- How do sibling combinators (`+` and `~`) help with styling relationships?
- What browser support considerations exist for modern selectors like `:has()`?
