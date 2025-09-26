// String methods
const title = 'modern front-end web development';
const proper = title
  .split(' ')
  .map((w) => w[0].toUpperCase() + w.slice(1))
  .join(' ');
console.log(proper); // "Modern Front-End Web Development"

// Array methods
const nums = [5, 12, 8, 130, 44];
const doubled = nums.map((n) => n * 2);
const large = nums.filter((n) => n > 10);
const sum = nums.reduce((acc, n) => acc + n, 0);

console.log({ doubled, large, sum });

// Object methods
const person = { name: 'Chris', role: 'Instructor', active: true };
console.log(Object.keys(person)); // ['name','role','active']
console.log(Object.values(person)); // ['Chris','Instructor',true]

// Small exercise: filter numbers > 10
function filterGreaterThanTen(arr) {
  return arr.filter((n) => n > 10);
}
console.log(filterGreaterThanTen(nums)); // [12,130,44]

// Additional useful array methods
console.log('\n--- More Array Methods ---');

// find() - returns first matching element
const firstLarge = nums.find((n) => n > 10);
console.log('First number > 10:', firstLarge); // 12

// some() - tests if any element passes the test
const hasLargeNumbers = nums.some((n) => n > 100);
console.log('Has numbers > 100:', hasLargeNumbers); // true

// every() - tests if all elements pass the test
const allPositive = nums.every((n) => n > 0);
console.log('All numbers positive:', allPositive); // true

// includes() - checks if array contains a value
const hasEight = nums.includes(8);
console.log('Contains 8:', hasEight); // true

// Method chaining example
const processedNums = nums
  .filter((n) => n > 10) // [12, 130, 44]
  .map((n) => n * 2) // [24, 260, 88]
  .sort((a, b) => a - b); // [24, 88, 260]
console.log('Processed numbers:', processedNums);

// Advanced string methods
console.log('\n--- Advanced String Methods ---');
const sentence = 'The quick brown fox jumps over the lazy dog';
console.log('Original:', sentence);
console.log('Starts with "The":', sentence.startsWith('The'));
console.log('Ends with "dog":', sentence.endsWith('dog'));
console.log('Includes "fox":', sentence.includes('fox'));
console.log('Padded:', sentence.padStart(50, '-'));
console.log('Repeated:', '🚀'.repeat(5));
