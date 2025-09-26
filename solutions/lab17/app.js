// Enhanced jQuery version with delete functionality
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

console.log('--- Vanilla JS Comparison ---');
console.log('jQuery version above uses:');
console.log('- $ for selection');
console.log('- .val() for getting/setting values');
console.log('- .append() for adding HTML');
console.log('- .on() for event delegation');
console.log('- .fadeOut() for animations');

// Vanilla JS equivalent (modern version)
/*
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
    li.dataset.id = reviewCounter;
    li.style.cssText = 'margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 4px;';
    li.innerHTML = `
      <strong>${movie}:</strong> ${review}
      <button class="delete-btn" style="float: right; background: #dc3545; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">
        Delete
      </button>
    `;
    
    reviewsList.appendChild(li);
    movieInput.value = '';
    reviewInput.value = '';
    movieInput.focus();
  } else {
    alert('Please enter both movie name and review!');
  }
});

// Event delegation for delete buttons
reviewsList.addEventListener('click', (e) => {
  if (e.target.classList.contains('delete-btn')) {
    if (confirm('Are you sure you want to delete this review?')) {
      e.target.parentElement.remove();
    }
  }
});
*/
