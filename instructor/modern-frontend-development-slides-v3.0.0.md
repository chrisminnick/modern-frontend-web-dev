# Modern Frontend Web Development

HTML5, CSS3, JavaScript, Tools, and Web APIs
for new web developers

Complete source code for all labs can be found at:
https://github.com/chrisminnick/modern-frontend-web-dev

Version 3.0.0, September 2025
by Chris Minnick

Copyright 2025, WatzThis?

https://www.watzthis.com

---

## Module 1: Introduction to Web Development Fundamentals

## Course Overview

**Modern Frontend Web Development**

**What You'll Learn:**

- HTML5 semantic markup and modern standards
- CSS3 with Grid, Flexbox, and responsive design
- JavaScript ES6+ with modern programming patterns
- DOM manipulation and event handling
- API integration and asynchronous programming
- Modern development tools and workflows
- React fundamentals and component architecture
- Testing, debugging, and deployment strategies

**Course Structure:** 8 modules, 17 hands-on labs, 1 final project

---

## The Modern Web Platform

**Evolution of Web Development:**

**Then (Early 2000s):**

- Static HTML pages
- Table-based layouts
- Inline styles and scripts
- Browser compatibility nightmares

**Now (2024):**

- Component-based architectures
- Mobile-first responsive design
- Modern JavaScript with ES6+ features
- Build tools and development workflows
- Progressive Web Applications (PWAs)

**Key Principles:** Semantic HTML, Separation of concerns, Progressive enhancement

---

## Client-Server Architecture

**How Web Applications Work:**

```
Client (Browser)          Server
     |                      |
     |-- HTTP Request ----→ |
     |                      |
     |← HTTP Response ------ |
     |                      |
```

**Client-Side (Frontend):**

- HTML structure and content
- CSS styling and layout
- JavaScript interactivity and logic
- User interface and experience

**Server-Side (Backend):**

- Data processing and storage
- Business logic and APIs
- Authentication and security
- Database management

---

## Understanding Web Protocols

**Internet Protocols enable web communication:**

**TCP/IP** - Transmission Control Protocol/Internet Protocol

- The Internet is a packet-switched network
- TCP collects and reassembles packets
- IP ensures packets reach the right destination

**DNS** - Domain Name System

- Converts between IP addresses and Domain Names
- Example: google.com → 142.250.191.14

**HTTP/HTTPS** - Hypertext Transfer Protocol

- Application-level protocol for web communication
- HTTPS adds security with SSL/TLS encryption

---

## Modern Development Environment

**Essential Tools for Front-End Development:**

**Code Editor:** Visual Studio Code

- Syntax highlighting, IntelliSense, extensions
- Integrated terminal and Git support

**Runtime:** Node.js and npm

- JavaScript runtime outside the browser
- Package manager for dependencies

**Build Tool:** Vite

- Fast development server with Hot Module Replacement
- Optimized production builds

**Version Control:** Git

- Track changes and collaborate effectively

---

## Lab 01: Working with the Command Line in VSCode

**Learning Objectives:**

- Open and use integrated terminal in VSCode
- Practice basic command line navigation
- Build confidence with commands for Git, npm, and project setup

**Key Commands:**

- `pwd` - Show current directory
- `ls` - List files and folders
- `cd` - Change directory
- `mkdir` - Create directory
- `touch` - Create file

---

## Module 2: Tools and Workflows

## Version Control with Git

**Why Version Control Matters:**

- Track changes over time
- Collaborate with team members
- Revert to previous versions
- Branch and merge features

**Git Workflow:**

1. `git init` - Initialize repository
2. `git add` - Stage changes
3. `git commit` - Save changes
4. `git push` - Upload to remote repository

---

## Package Management with npm

**What is npm?**

- Node Package Manager
- Manages dependencies for JavaScript projects
- Provides scripts for common tasks

**Key npm Commands:**

- `npm init` - Initialize project
- `npm install` - Install dependencies
- `npm run` - Execute scripts
- `npm update` - Update packages

**package.json** - Project configuration file

---

## Browser Developer Tools

**Chrome DevTools Features:**

**Elements Panel:**

- Inspect and modify HTML/CSS live
- Debug layout issues

**Console Panel:**

- View JavaScript errors and logs
- Test code interactively

**Sources Panel:**

- Set breakpoints and debug JavaScript
- Step through code execution

**Network Panel:**

- Monitor HTTP requests and responses

---

## Lab 02: Using Visual Studio Code Basics

**Learning Objectives:**

- Master VSCode features and extensions
- Learn Markdown for documentation
- Use Emmet for faster HTML writing
- Customize development environment

**Key VSCode Features:**

- Command Palette (Cmd/Ctrl + Shift + P)
- Multi-cursor editing
- Live Server extension
- Markdown preview

---

## Module 3: HTML Fundamentals

## HTML5 Semantic Elements

**Modern HTML5 provides meaningful structure:**

**Document Structure:**

- `<header>` - Page or section header
- `<nav>` - Navigation links
- `<main>` - Primary content
- `<footer>` - Page or section footer

**Content Organization:**

- `<article>` - Self-contained content
- `<section>` - Logical document divisions
- `<aside>` - Sidebar or tangential content
- `<figure>` & `<figcaption>` - Images with captions

**Benefits:** Better SEO, accessibility, and maintainability

---

## HTML Forms and User Input

**Essential Form Elements:**

**Input Types:**

- `<input type="text">` - Text fields
- `<input type="email">` - Email validation
- `<input type="password">` - Hidden input
- `<input type="number">` - Numeric input
- `<input type="date">` - Date picker

**Form Structure:**

```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />
  <button type="submit">Submit</button>
</form>
```

---

## Lab 03: Controlling Your Versions with Git

**Learning Objectives:**

- Initialize Git repositories
- Stage and commit changes
- Work with remote repositories
- Understand Git workflow and best practices

**Key Git Commands:**

- `git init` - Initialize repository
- `git add` - Stage changes
- `git commit` - Save changes with message
- `git push` - Upload to remote repository

---

## Lab 04: Initializing npm

**Learning Objectives:**

- Initialize npm package.json
- Understand package.json structure
- Configure project metadata
- Set up npm scripts

**Key Concepts:**

- `npm init` command
- Package.json configuration
- Project dependencies vs devDependencies
- npm script basics

---

## Module 4: CSS Fundamentals

## Modern CSS Layout

**CSS Grid - Two-Dimensional Layout:**

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
```

**Flexbox - One-Dimensional Layout:**

```css
.flex-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

**When to Use Each:**

- Grid: Complex layouts, two-dimensional control
- Flexbox: Component alignment, one-dimensional flow

---

## Responsive Design Principles

**Mobile-First Approach:**

```css
/* Base styles for mobile */
.container {
  width: 100%;
}

/* Tablet styles */
@media (min-width: 768px) {
  .container {
    width: 750px;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .container {
    width: 1200px;
  }
}
```

**Key Breakpoints:**

- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

---

## Lab 05: Using npm

**Learning Objectives:**

- Install and manage packages with npm
- Understand node_modules and package-lock.json
- Use npm scripts for automation
- Work with package versions

**Key npm Commands:**

- `npm install` - Install dependencies
- `npm install --save-dev` - Install dev dependencies
- `npm run` - Execute scripts
- `npm update` - Update packages

---

## Lab 06: Creating a New Project with Vite

**Learning Objectives:**

- Set up a new project using Vite
- Understand modern build tools
- Configure development environment
- Use hot module replacement (HMR)

**Vite Benefits:**

- Fast development server
- Instant hot module replacement
- Optimized production builds
- Modern JavaScript support

---

## Module 5: JavaScript Fundamentals

## Modern JavaScript (ES6+)

**Essential Modern Features:**

**Variable Declarations:**

```javascript
const name = 'John'; // Immutable
let age = 25; // Block-scoped
// Avoid var           // Function-scoped (legacy)
```

**Arrow Functions:**

```javascript
const add = (a, b) => a + b;
const greet = (name) => `Hello, ${name}!`;
```

**Template Literals:**

```javascript
const message = `Welcome, ${name}! You are ${age} years old.`;
```

---

## Destructuring and Spread Operator

**Array Destructuring:**

```javascript
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first = 1, second = 2, rest = [3, 4, 5]
```

**Object Destructuring:**

```javascript
const { name, age, city = 'Unknown' } = person;
```

**Spread Operator:**

```javascript
const newArray = [...oldArray, newItem];
const newObject = { ...oldObject, newProperty: value };
```

---

## Lab 07: Using Chrome Developer Tools – Elements Panel

**Learning Objectives:**

- Navigate the Elements panel in Chrome DevTools
- Inspect and modify HTML elements
- Edit CSS styles in real-time
- Debug layout and styling issues

**Elements Panel Features:**

- DOM tree inspection
- Style editing and computed styles
- Box model visualization
- Event listener debugging

---

## Lab 08: Using Chrome Developer Tools – Sources Panel (JavaScript Debugging)

**Learning Objectives:**

- Debug JavaScript using the Sources panel
- Set breakpoints and step through code
- Inspect variable values and call stack
- Use console for debugging

**Debugging Features:**

- Breakpoint management
- Step over, step into, step out
- Variable inspection and watches
- Call stack analysis

---

## Module 6: Advanced JavaScript

## Arrays and Objects

**Modern Array Methods:**

```javascript
const numbers = [1, 2, 3, 4, 5];

// Transformation
const doubled = numbers.map((n) => n * 2);

// Filtering
const evens = numbers.filter((n) => n % 2 === 0);

// Reduction
const sum = numbers.reduce((acc, n) => acc + n, 0);

// Finding
const found = numbers.find((n) => n > 3);
```

**Object Methods:**

```javascript
const keys = Object.keys(obj);
const values = Object.values(obj);
const entries = Object.entries(obj);
```

---

## DOM Manipulation

**Modern DOM API:**

```javascript
// Selection
const element = document.querySelector('.my-class');
const elements = document.querySelectorAll('.item');

// Modification
element.textContent = 'New text';
element.innerHTML = '<strong>Bold text</strong>';
element.classList.add('active');

// Creation
const newElement = document.createElement('div');
newElement.setAttribute('data-id', '123');
parent.appendChild(newElement);
```

---

## Event Handling

**Modern Event Handling:**

```javascript
// Event listeners
button.addEventListener('click', handleClick);

// Event object
function handleClick(event) {
  event.preventDefault();
  console.log(event.target);
}

// Event delegation
container.addEventListener('click', (event) => {
  if (event.target.matches('.button')) {
    // Handle button click
  }
});
```

---

## Lab 09: Creating an HTML Form

**Learning Objectives:**

- Create interactive forms with proper validation
- Use semantic form elements and attributes
- Implement accessibility best practices
- Handle form data with JavaScript

**Key Concepts:**

- Form validation attributes (`required`, `pattern`)
- Label-input relationships
- Form accessibility
- Modern input types

---

## Lab 10: Using CSS Selectors

**Learning Objectives:**

- Master different types of CSS selectors
- Understand selector specificity
- Apply styles effectively
- Practice advanced selector techniques

**Selector Types:**

- Element, class, and ID selectors
- Attribute selectors
- Pseudo-classes and pseudo-elements
- Combinator selectors

---

## Lab 11: Positioning with CSS (and Flexbox)

**Learning Objectives:**

- Master CSS positioning properties
- Use Flexbox for flexible layouts
- Create responsive design patterns
- Build common UI components

**Key Concepts:**

- Static, relative, absolute, fixed positioning
- Flexbox container and item properties
- Alignment and distribution
- Responsive layout techniques

---

## Module 7: APIs and Asynchronous JavaScript

## Working with APIs

**Fetch API for HTTP Requests:**

```javascript
// GET request
const response = await fetch('/api/users');
const users = await response.json();

// POST request
const response = await fetch('/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(userData),
});
```

**Error Handling:**

```javascript
try {
  const data = await fetchUserData();
  console.log(data);
} catch (error) {
  console.error('Failed to fetch data:', error);
}
```

---

## Asynchronous JavaScript

**Promises and Async/Await:**

```javascript
// Promise-based
function fetchData() {
  return fetch('/api/data')
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}

// Async/await
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

---

## Lab 12: Variables, Arrays, and Constants in JavaScript

**Learning Objectives:**

- Use modern variable declarations (`const`, `let`)
- Work with arrays and array methods
- Understand scope and hoisting
- Practice data manipulation techniques

**Key Concepts:**

- Variable declarations and scope
- Array creation and manipulation
- Const vs let vs var
- Modern JavaScript syntax

---

## Lab 13: Using Chrome DevTools – JavaScript Console

**Learning Objectives:**

- Master the JavaScript Console in Chrome DevTools
- Debug JavaScript code effectively
- Test JavaScript expressions interactively
- Analyze runtime errors and warnings

**Console Features:**

- Interactive JavaScript execution
- Error and warning messages
- Console logging methods
- Performance monitoring

---

## Module 8: Modern Frameworks and Deployment

## Introduction to Modern Frameworks

**Why Use Frameworks?**

- Component-based architecture
- State management
- Virtual DOM for performance
- Rich ecosystem and tooling

**Popular Options:**

- **React** - Component-based library
- **Vue** - Progressive framework
- **Angular** - Full-featured framework
- **Svelte** - Compile-time optimization

**Key Concepts:**

- Components and props
- State and lifecycle
- Event handling
- Routing and navigation

---

## Build Tools and Development Workflow

**Modern Build Pipeline:**

**Vite** - Next-generation build tool

- Lightning-fast development server
- Hot Module Replacement (HMR)
- Optimized production builds

**Package Management:**

- npm/yarn for dependency management
- package.json for project configuration
- Semantic versioning

**Code Quality:**

- ESLint for code linting
- Prettier for code formatting
- Git hooks for automated checks

---

## Lab 14: Using JavaScript Methods

**Learning Objectives:**

- Work with JavaScript functions and methods
- Understand method syntax and this binding
- Practice built-in methods for strings and arrays
- Create custom methods for objects

**Method Types:**

- String methods (slice, substring, indexOf)
- Array methods (push, pop, shift, unshift)
- Object methods and this context
- Function expressions and arrow functions

---

## Lab 15: Using JavaScript Objects

**Learning Objectives:**

- Create and manipulate JavaScript objects
- Understand object properties and methods
- Work with object constructors and prototypes
- Practice object-oriented programming concepts

**Object Concepts:**

- Object literal syntax
- Property access and modification
- Object methods and this binding
- Constructor functions and prototypes

---

## Testing and Debugging

**Testing Strategies:**

- Unit testing with Jest
- Component testing with React Testing Library
- End-to-end testing with Cypress
- Manual testing and debugging

**Debugging Tools:**

- Browser DevTools
- React Developer Tools
- VS Code debugging
- Console logging strategies

**Best Practices:**

- Test-driven development
- Continuous integration
- Code coverage metrics

---

## Lab 16: Performing DOM Manipulation

**Learning Objectives:**

- Select and modify DOM elements
- Create dynamic content with JavaScript
- Handle user interactions and events
- Build interactive web pages

**DOM Techniques:**

- Query selectors and element selection
- Content and attribute manipulation
- Dynamic element creation
- Event handling and delegation

---

## Deployment and Performance

**Deployment Options:**

- **Static Hosting:** Netlify, Vercel, GitHub Pages
- **Cloud Platforms:** AWS, Google Cloud, Azure
- **CDN Integration:** Fast global delivery

**Performance Optimization:**

- Code splitting and lazy loading
- Image optimization
- Caching strategies
- Bundle size optimization

**Monitoring:**

- Performance metrics
- Error tracking
- User analytics

---

## Lab 17: Building a Movie Review Webpage with jQuery

**Learning Objectives:**

- Introduction to jQuery library
- Build interactive web interfaces
- Practice DOM manipulation with jQuery
- Create a complete movie review application

**jQuery Features:**

- Simplified DOM selection and manipulation
- Event handling with jQuery
- AJAX requests for dynamic content
- Building interactive user interfaces

---

## Course Summary and Next Steps

**What You've Accomplished:**
✅ Modern HTML5 and semantic markup
✅ Advanced CSS with Grid and Flexbox
✅ JavaScript ES6+ and modern patterns
✅ DOM manipulation and event handling
✅ API integration and async programming
✅ React fundamentals and component architecture
✅ Testing, debugging, and deployment

**Next Steps:**

- Build personal projects
- Contribute to open source
- Explore advanced frameworks
- Learn backend development
- Stay updated with web standards

**Resources for Continued Learning:**

- MDN Web Docs, JavaScript.info
- React Documentation
- Frontend Masters, freeCodeCamp
- GitHub projects and communities

---

## Final Project Overview

**Capstone Project: Personal Portfolio Website**

**Requirements:**

- Responsive design with modern CSS
- Interactive features with JavaScript
- API integration for dynamic content
- React components for complex UI
- Professional deployment

**Features to Implement:**

- About section with personal information
- Portfolio showcase with project details
- Contact form with validation
- Blog or news section (API-driven)
- Dark/light theme toggle
- Mobile-responsive navigation

**Assessment Criteria:**

- Code quality and organization
- User experience and design
- Technical implementation
- Performance and accessibility
