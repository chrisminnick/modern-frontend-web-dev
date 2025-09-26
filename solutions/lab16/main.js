// Modern DOM selection methods (preferred over getElementById)
const title = document.querySelector('#title');
const btn = document.querySelector('#btn');
const msg = document.querySelector('#message');

// Basic DOM manipulation
btn.addEventListener('click', () => {
  title.textContent = 'You clicked the button!';
  msg.textContent = 'DOM updated successfully 🎉';
});

// Advanced DOM manipulation examples
console.log('--- Advanced DOM Examples ---');

// Create new elements dynamically
function addNewSection() {
  const newSection = document.createElement('section');
  newSection.innerHTML = `
    <h2>Dynamically Created Section</h2>
    <p>This section was created with JavaScript!</p>
    <button class="remove-btn">Remove This Section</button>
  `;

  // Add some styling
  newSection.style.cssText = `
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    color: white;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
  `;

  document.body.appendChild(newSection);

  // Add event listener to the remove button
  const removeBtn = newSection.querySelector('.remove-btn');
  removeBtn.addEventListener('click', () => {
    newSection.remove(); // Modern way to remove elements
  });
}

// Add button to create new sections
const createBtn = document.createElement('button');
createBtn.textContent = 'Create New Section';
createBtn.style.cssText = `
  background: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin: 1rem 0;
`;
createBtn.addEventListener('click', addNewSection);
document.body.appendChild(createBtn);

// querySelector vs querySelectorAll examples
const allButtons = document.querySelectorAll('button');
console.log('Number of buttons:', allButtons.length);

// Event delegation example
document.body.addEventListener('click', (event) => {
  if (event.target.matches('.remove-btn')) {
    console.log('Remove button clicked via delegation!');
  }
});
