# Lab 17: Building a Movie Review Webpage with jQuery

## Objectives

- Learn the basics of jQuery for DOM manipulation.
- Build a simple interactive page with dynamic content.
- Compare jQuery with vanilla JavaScript solutions.

## Duration

60 minutes

## Materials Needed

- VSCode
- Live Server or Vite

## Instructions

1. Create `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <title>Movie Reviews</title>
       <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
     </head>
     <body>
       <h1>Movie Reviews</h1>
       <input id="movie" placeholder="Enter movie name" />
       <input id="review" placeholder="Enter your review" />
       <button id="add">Add Review</button>
       <ul id="reviews"></ul>
       <script src="app.js"></script>
     </body>
   </html>
   ```
2. Create `app.js`:

   ```javascript
   let reviewCounter = 0;

   $('#add').click(() => {
     const movie = $('#movie').val().trim();
     const review = $('#review').val().trim();

     if (movie && review) {
       reviewCounter++;
       const reviewItem = $(`
         <li data-id="${reviewCounter}" style="margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 4px;">
           <strong>${movie}:</strong> ${review}
           <button class="delete-btn" style="float: right; background: #dc3545; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">
             Delete
           </button>
         </li>
       `);

       $('#reviews').append(reviewItem);
       $('#movie').val('');
       $('#review').val('');
       $('#movie').focus();

       // Show success message
       $('body').append(
         '<div id="success-msg" style="position: fixed; top: 20px; right: 20px; background: #28a745; color: white; padding: 10px; border-radius: 4px;">Review added!</div>'
       );
       setTimeout(
         () => $('#success-msg').fadeOut(() => $('#success-msg').remove()),
         2000
       );
     } else {
       alert('Please enter both movie name and review!');
     }
   });

   // Delete functionality using event delegation
   $('#reviews').on('click', '.delete-btn', function () {
     if (confirm('Are you sure you want to delete this review?')) {
       $(this)
         .parent()
         .fadeOut(() => $(this).parent().remove());
     }
   });

   // Enter key support
   $('#movie, #review').keypress((e) => {
     if (e.which === 13) {
       // Enter key
       $('#add').click();
     }
   });
   ```

3. **Vanilla JavaScript Comparison** (explore the modern alternative):

   ```javascript
   // Modern vanilla JS equivalent:
   const addBtn = document.querySelector('#add');
   const movieInput = document.querySelector('#movie');
   const reviewInput = document.querySelector('#review');
   const reviewsList = document.querySelector('#reviews');
   let reviewCounter = 0;

   addBtn.addEventListener('click', () => {
     const movie = movieInput.value.trim();
     const review = reviewInput.value.trim();

     if (movie && review) {
       reviewCounter++;
       const li = document.createElement('li');
       li.innerHTML = `<strong>${movie}:</strong> ${review}
         <button class="delete-btn">Delete</button>`;

       reviewsList.appendChild(li);
       movieInput.value = '';
       reviewInput.value = '';
       movieInput.focus();
     }
   });

   // Event delegation for delete buttons
   reviewsList.addEventListener('click', (e) => {
     if (e.target.classList.contains('delete-btn')) {
       e.target.parentElement.remove();
     }
   });
   ```

## Discussion and Sharing

- Why was jQuery so popular historically?
- How would you do this today with vanilla JS or React?
- What benefits remain for using jQuery in 2025?
- **Enhanced Questions:**
  - What are the advantages of event delegation over individual event listeners?
  - How does jQuery's chaining syntax compare to vanilla JavaScript?
  - When might you still choose jQuery over vanilla JavaScript in modern development?
  - How do the file sizes and performance compare between jQuery and vanilla JS solutions?
