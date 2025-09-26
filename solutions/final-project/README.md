# Final Project: Random User Generator

## Overview

This is the culminating project for the Modern Front-End Web Development course, demonstrating all the skills learned throughout labs 1-17.

## Features

- **Fetch API Integration**: Retrieves data from the RandomUser.me API
- **Async/Await**: Modern JavaScript async handling
- **Dynamic DOM Manipulation**: Creates user cards dynamically
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful handling of network errors
- **Loading States**: Visual feedback during API calls
- **Interactive Controls**: Options for multiple users and nationality filtering
- **Modern CSS**: Grid, Flexbox, animations, and gradients
- **Accessibility**: Keyboard navigation and semantic HTML

## Technologies Used

- HTML5 (semantic markup)
- CSS3 (Grid, Flexbox, animations, custom properties)
- JavaScript ES6+ (async/await, fetch, arrow functions, template literals)
- RandomUser.me API

## Skills Demonstrated

### From Lab 01 (Command Line)

- Project structure and file organization

### From Lab 02 (VSCode)

- Code organization and formatting

### From Lab 03 (Git)

- Version control principles (project ready for Git)

### From Lab 04-05 (npm)

- Modern JavaScript modules and package management concepts

### From Lab 06 (Vite)

- Modern build tool concepts (project can be enhanced with Vite)

### From Lab 07-08 (DevTools)

- Debugging-ready code with console logging and error handling

### From Lab 09 (HTML Forms)

- Form controls (checkboxes, select elements)

### From Lab 10 (CSS Selectors)

- Advanced CSS selectors and pseudo-classes

### From Lab 11 (CSS Layout)

- CSS Grid and Flexbox for responsive layout

### From Lab 12 (JavaScript Variables)

- Modern variable declarations (const, let)

### From Lab 13 (Console)

- Console logging for debugging and information

### From Lab 14 (JavaScript Methods)

- Array methods, string manipulation

### From Lab 15 (JavaScript Objects)

- Object manipulation and destructuring

### From Lab 16 (DOM Manipulation)

- Dynamic element creation and event handling

### From Lab 17 (jQuery comparison)

- Modern vanilla JavaScript alternatives to jQuery

## How to Run

1. **Simple HTTP Server** (if you have Python installed):

   ```bash
   python -m http.server 8000
   ```

   Then visit http://localhost:8000

2. **Live Server** (VSCode extension):

   - Right-click on `index.html`
   - Select "Open with Live Server"

3. **Node.js http-server**:
   ```bash
   npx http-server
   ```

## API Usage

This project uses the [RandomUser.me API](https://randomuser.me/):

- Endpoint: `https://randomuser.me/api/`
- Parameters:
  - `results`: Number of users to generate (1-5)
  - `nat`: Nationality filter (us, gb, ca, au, de, fr, es, br)

## Future Enhancements

Ideas for extending this project:

- Add user favorites/bookmarking
- Implement local storage for user history
- Add more filtering options (age range, gender)
- Include data visualization charts
- Add user search functionality
- Implement pagination for large datasets
- Add print/export functionality
- Include accessibility improvements (ARIA labels)

## Course Integration

This project demonstrates the progression from basic command-line skills to building a complete, interactive web application using modern front-end technologies and best practices.
