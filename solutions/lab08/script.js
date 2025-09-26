const launchBtn = document.getElementById('launch');
const timerEl = document.getElementById('timer');

function startTimer(start = 10) {
  let timer = start;
  const id = setInterval(() => {
    // BUG: we decrement before checking, which skips 0 properly
    timer--; // <-- suspect line
    timerEl.textContent = timer; // shows updated time
    if (timer === 0) {
      // may never hit as expected
      clearInterval(id);
      console.log('🚀 Lift off!');
    }
  }, 1000);
}

function init() {
  launchBtn.addEventListener('click', startTimer);
}

init();
