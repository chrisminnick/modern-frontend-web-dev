// DOM elements
const loadBtn = document.getElementById('load');
const output = document.getElementById('output');
const counter = document.getElementById('counter');
const multipleCheckbox = document.getElementById('multiple');
const nationalitySelect = document.getElementById('nationality');
const btnText = document.querySelector('.btn-text');
const loadingText = document.querySelector('.loading');

// State
let userCount = 0;

// Main function to load users
async function loadUsers() {
  try {
    // Disable button and show loading
    setLoadingState(true);

    // Determine how many users to fetch
    const isMultiple = multipleCheckbox.checked;
    const results = isMultiple ? 5 : 1;

    // Get nationality filter
    const nationality = nationalitySelect.value;

    // Build API URL
    let apiUrl = `https://randomuser.me/api/?results=${results}`;
    if (nationality) {
      apiUrl += `&nat=${nationality}`;
    }

    console.log('Fetching from:', apiUrl);

    // Fetch data from API
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Display users
    displayUsers(data.results);

    // Update counter
    userCount += data.results.length;
    counter.textContent = userCount;
  } catch (error) {
    console.error('Error fetching users:', error);
    showError(
      'Failed to load users. Please check your internet connection and try again.'
    );
  } finally {
    setLoadingState(false);
  }
}

// Function to display users
function displayUsers(users) {
  // Clear placeholder
  output.innerHTML = '';

  // Create container for users
  const userGrid = document.createElement('div');
  userGrid.className = 'user-grid';

  users.forEach((user) => {
    const userCard = createUserCard(user);
    userGrid.appendChild(userCard);
  });

  output.appendChild(userGrid);

  // Add fade-in animation
  userGrid.style.opacity = '0';
  userGrid.style.transform = 'translateY(20px)';

  // Trigger animation
  requestAnimationFrame(() => {
    userGrid.style.transition = 'all 0.5s ease';
    userGrid.style.opacity = '1';
    userGrid.style.transform = 'translateY(0)';
  });
}

// Function to create a user card
function createUserCard(user) {
  const card = document.createElement('div');
  card.className = 'user-card';

  // Format user data
  const fullName = `${user.name.first} ${user.name.last}`;
  const age = user.dob.age;
  const location = `${user.location.city}, ${user.location.country}`;
  const phone = user.phone;
  const registered = new Date(user.registered.date).toLocaleDateString();

  card.innerHTML = `
    <img src="${user.picture.large}" alt="${fullName}" class="user-avatar" />
    <div class="user-name">${fullName}</div>
    <div class="user-email">${user.email}</div>
    <div class="user-details">
      <div class="user-detail">
        <strong>Age:</strong> ${age}
      </div>
      <div class="user-detail">
        <strong>Gender:</strong> ${user.gender}
      </div>
      <div class="user-detail">
        <strong>Location:</strong> ${location}
      </div>
      <div class="user-detail">
        <strong>Phone:</strong> ${phone}
      </div>
      <div class="user-detail" style="grid-column: 1 / -1;">
        <strong>Member since:</strong> ${registered}
      </div>
    </div>
  `;

  return card;
}

// Function to show error message
function showError(message) {
  output.innerHTML = `
    <div class="error">
      <h3>⚠️ Error</h3>
      <p>${message}</p>
    </div>
  `;
}

// Function to set loading state
function setLoadingState(isLoading) {
  loadBtn.disabled = isLoading;

  if (isLoading) {
    btnText.style.display = 'none';
    loadingText.style.display = 'inline';
    loadingText.innerHTML = '<span class="loading-spinner"></span> Loading...';
  } else {
    btnText.style.display = 'inline';
    loadingText.style.display = 'none';
  }
}

// Event listeners
loadBtn.addEventListener('click', loadUsers);

// Keyboard support
document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !loadBtn.disabled) {
    loadUsers();
  }
});

// Add some example functionality for demonstration
console.log('=== Final Project: Random User Generator ===');
console.log('Features demonstrated:');
console.log('- Fetch API for HTTP requests');
console.log('- Async/await for handling promises');
console.log('- DOM manipulation and dynamic content creation');
console.log('- CSS Grid and Flexbox for responsive layout');
console.log('- Error handling for network requests');
console.log('- Loading states and user feedback');
console.log('- Event handling and keyboard support');
console.log('- Modern JavaScript (ES6+) features');

// Initialize
console.log('App initialized! Click "Load Random User" to begin.');
