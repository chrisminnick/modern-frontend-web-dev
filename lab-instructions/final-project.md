# Final Project: Interactive Web App with Fetch

## Objectives

- Apply all skills from the course: HTML5, CSS3, JavaScript, DOM, and Fetch API.
- Build a comprehensive interactive app that pulls data from a public API.
- Demonstrate mastery of responsive design, error handling, and modern JavaScript.

## Duration

2–3 hours

## Materials Needed

- VSCode
- Modern web browser
- Internet connection for API access

## Instructions

**Complete project files are available in `labs/final-project/`**

1. **Create the HTML Structure** (`index.html`):

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Random User Generator</title>
       <link rel="stylesheet" href="style.css" />
     </head>
     <body>
       <div class="container">
         <header>
           <h1>🎲 Random User Generator</h1>
           <p>Generate random user profiles from around the world!</p>
         </header>
         <main>
           <div class="controls">
             <button id="load" class="load-btn">
               <span class="btn-text">Load Random User</span>
               <span class="loading" style="display: none;">Loading...</span>
             </button>
             <div class="options">
               <label>
                 <input type="checkbox" id="multiple" />
                 Load 5 users at once
               </label>
               <select id="nationality">
                 <option value="">Any nationality</option>
                 <option value="us">United States</option>
                 <option value="gb">United Kingdom</option>
                 <option value="ca">Canada</option>
                 <option value="au">Australia</option>
               </select>
             </div>
           </div>
           <div id="output" class="output">
             <div class="placeholder">
               <p>
                 👆 Click the button above to generate your first random user!
               </p>
             </div>
           </div>
         </main>
       </div>
       <script src="main.js"></script>
     </body>
   </html>
   ```

2. **Add Modern CSS Styling** (`style.css`):

   - Responsive grid layout using CSS Grid and Flexbox
   - Gradient backgrounds and smooth animations
   - Mobile-first responsive design
   - Loading states and hover effects

3. **Implement JavaScript Functionality** (`main.js`):

   ```javascript
   const loadBtn = document.getElementById('load');
   const output = document.getElementById('output');
   const multipleCheckbox = document.getElementById('multiple');
   const nationalitySelect = document.getElementById('nationality');

   async function loadUsers() {
     try {
       setLoadingState(true);

       const isMultiple = multipleCheckbox.checked;
       const results = isMultiple ? 5 : 1;
       const nationality = nationalitySelect.value;

       let apiUrl = `https://randomuser.me/api/?results=${results}`;
       if (nationality) apiUrl += `&nat=${nationality}`;

       const response = await fetch(apiUrl);
       if (!response.ok)
         throw new Error(`HTTP error! status: ${response.status}`);

       const data = await response.json();
       displayUsers(data.results);
     } catch (error) {
       showError('Failed to load users. Please try again.');
     } finally {
       setLoadingState(false);
     }
   }

   function displayUsers(users) {
     // Dynamic DOM manipulation to create user cards
     // (Complete implementation in final-project/main.js)
   }

   loadBtn.addEventListener('click', loadUsers);
   ```

4. **Test and Run**:

   - Use Live Server or run `python -m http.server` in the project directory
   - Test responsive design in different screen sizes
   - Verify error handling by disconnecting internet

5. **Enhanced Features Included**:
   - Loading animations and user feedback
   - Error handling for network failures
   - Responsive design for mobile and desktop
   - Keyboard navigation support
   - Multiple user generation option
   - Nationality filtering
   - Modern CSS animations and effects

## Skills Demonstrated

This project showcases mastery of all course concepts:

- **Labs 1-3**: Project structure, version control ready
- **Labs 4-6**: Modern development workflow concepts
- **Labs 7-8**: Debug-ready code with proper error handling
- **Lab 9**: Form controls and user input handling
- **Lab 10**: Advanced CSS selectors and styling
- **Lab 11**: Responsive layout with Grid and Flexbox
- **Lab 12**: Modern JavaScript variable handling
- **Lab 13**: Console logging and debugging
- **Lab 14**: Array methods and data transformation
- **Lab 15**: Object manipulation and destructuring
- **Lab 16**: Dynamic DOM manipulation and events
- **Lab 17**: Modern vanilla JavaScript (no jQuery needed)

## Discussion and Sharing

- Which part of the course helped you the most in completing the project?
- How did using Fetch and async/await simplify working with data?
- What challenges did you face with responsive design?
- How does error handling improve user experience?
- What modern JavaScript features made development easier?
- How might you expand this project further?

## Extension Ideas

- Add user favorites with localStorage
- Implement data visualization
- Add more filtering options
- Include user search functionality
- Add print/export features
- Implement accessibility improvements
