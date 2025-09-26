// Fix the error first, then explore console methods:
const somethingiswrong = 'Actually, everything is fine!';
console.log(somethingiswrong);

// Some data to explore:
const people = [
  { name: 'Ada', role: 'Engineer' },
  { name: 'Grace', role: 'Scientist' },
  { name: 'Linus', role: 'Hacker' },
];

// Advanced console methods
console.log('--- Basic Console Methods ---');
console.log('Hello from console.log');
console.error('This is an error message');
console.warn('This is a warning');
console.info('This is an info message');

console.log('\n--- Data Display Methods ---');
console.table(people);
console.dir(people); // shows object structure

console.log('\n--- Grouping Methods ---');
console.group('User Information');
console.log('Name: Alice');
console.log('Age: 25');
console.log('Role: Developer');
console.groupEnd();

console.log('\n--- Timing Methods ---');
console.time('Performance Test');
// Simulate some work
for (let i = 0; i < 100000; i++) {
  Math.random();
}
console.timeEnd('Performance Test');

console.log('\n--- Trace Method ---');
function functionA() {
  functionB();
}
function functionB() {
  console.trace('Call stack trace:');
}
functionA();
