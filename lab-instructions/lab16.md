# Lab 16: Performing DOM Manipulation

## Objectives

- Learn how to select and update DOM elements with JavaScript.
- Respond to user events like clicks.
- Compare DOM manipulation with jQuery and React.

## Duration

40–50 minutes

## Materials Needed

- VSCode
- Browser with Live Server or Vite

## Instructions

1. Create `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <title>DOM Lab</title>
     </head>
     <body>
       <h1 id="title">Original Title</h1>
       <button id="btn">Click Me</button>
       <p id="message"></p>
       <script src="main.js"></script>
     </body>
   </html>
   ```
2. Create `main.js`:

   ```javascript
   // Modern DOM selection methods (preferred over getElementById)
   const title = document.querySelector('#title');
   const btn = document.querySelector('#btn');
   const msg = document.querySelector('#message');

   btn.addEventListener('click', () => {
     title.textContent = 'You clicked the button!';
     msg.textContent = 'DOM updated successfully 🎉';
   });
   ```

3. **Advanced DOM Features** (explore these enhancements):

   Dynamic element creation:

   ```javascript
   function addNewSection() {
     const newSection = document.createElement('section');
     newSection.innerHTML = `
       <h2>Dynamically Created Section</h2>
       <p>This section was created with JavaScript!</p>
       <button class="remove-btn">Remove This Section</button>
     `;

     // Add styling
     newSection.style.cssText = `
       background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
       color: white;
       padding: 1rem;
       margin: 1rem 0;
       border-radius: 8px;
     `;

     document.body.appendChild(newSection);

     // Add event listener to remove button
     const removeBtn = newSection.querySelector('.remove-btn');
     removeBtn.addEventListener('click', () => {
       newSection.remove(); // Modern way to remove elements
     });
   }

   // Create button to add new sections
   const createBtn = document.createElement('button');
   createBtn.textContent = 'Create New Section';
   createBtn.addEventListener('click', addNewSection);
   document.body.appendChild(createBtn);
   ```

   Event delegation:

   ```javascript
   document.body.addEventListener('click', (event) => {
     if (event.target.matches('.remove-btn')) {
       console.log('Remove button clicked via delegation!');
     }
   });
   ```

4. **Comparison with jQuery and React**:
   - **jQuery**:
     ```javascript
     $('#btn').click(() => {
       $('#title').text('Updated with jQuery');
     });
     ```
   - **React (conceptual)**: React updates the DOM indirectly using components.

## Discussion and Sharing

- How does DOM manipulation make a page interactive?
- Why is direct DOM manipulation less common in large apps?
- How do libraries like React change the process?
- **Enhanced Questions:**
  - What's the difference between `querySelector` and `getElementById`?
  - When would you use event delegation instead of individual event listeners?
  - How does dynamic element creation compare to template-based approaches?
  - What are the performance implications of frequent DOM manipulation?
