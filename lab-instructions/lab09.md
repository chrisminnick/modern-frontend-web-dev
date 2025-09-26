# Lab 09: Creating an HTML Form

## Objectives

- Create an accessible HTML5 form.
- Use semantic labels and input types.
- Leverage built‑in validation attributes.

## Duration

30–40 minutes

## Materials Needed

- VSCode
- Live Server (or Vite)

## Instructions

1. **Create Files in `labs/lab09/`**

   `index.html`:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Contact Us</title>
       <link rel="stylesheet" href="css/main.css" />
     </head>
     <body>
       <h1>Contact Us</h1>
       <p>Please fill out the following form and we'll get back to you.</p>

       <form action="#" method="post" novalidate>
         <div>
           <label for="contact-name">Your Name</label>
           <input
             id="contact-name"
             name="contact-name"
             type="text"
             placeholder="Enter your name"
             required
           />
         </div>

         <div>
           <label for="contact-phone">Phone Number</label>
           <input
             id="contact-phone"
             name="contact-phone"
             type="tel"
             placeholder="(555) 555-5555"
           />
         </div>

         <div>
           <label for="contact-email">Email</label>
           <input
             id="contact-email"
             name="contact-email"
             type="email"
             placeholder="you@example.com"
             required
           />
         </div>

         <div>
           <label for="contact-message">Message</label>
           <textarea
             id="contact-message"
             name="contact-message"
             rows="5"
             placeholder="How can we help?"
             required
           ></textarea>
         </div>

         <div>
           <label for="callback-time">Preferred Callback Time</label>
           <select id="callback-time" name="callback-time">
             <option value="">Select a time</option>
             <option value="morning">Morning</option>
             <option value="afternoon">Afternoon</option>
             <option value="evening">Evening</option>
           </select>
         </div>

         <div>
           <input type="submit" value="Submit" />
         </div>
       </form>
     </body>
   </html>
   ```

   `css/main.css` (optional starter):

   ```css
   body {
     font-family: system-ui, sans-serif;
     padding: 1.5rem;
   }
   form {
     display: grid;
     gap: 1rem;
     max-width: 480px;
   }
   label {
     display: block;
     font-weight: 600;
     margin-bottom: 0.25rem;
   }
   input,
   textarea,
   select {
     width: 100%;
     padding: 0.5rem;
   }
   input[type='submit'] {
     width: auto;
     cursor: pointer;
   }
   ```

2. **Open in Browser and Test Validation**
   - Try submitting with required fields empty.

## Discussion and Sharing

- Which HTML attributes improved accessibility?
- What validation do you get "for free" from HTML5?
