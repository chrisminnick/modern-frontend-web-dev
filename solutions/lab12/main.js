// Declaring and initializing a variable
let userName = 'Alice';

// Declaring and initializing an array
let primeNumbers = [2, 3, 5, 7, 11, 13];

// Declaring and initializing a constant
const GRAVITY = 9.81;

// Using variables
console.log('The user name is:', userName);

// Accessing array elements
console.log('The first prime number is:', primeNumbers[0]);
console.log('The third prime number is:', primeNumbers[2]);

// Using a constant
console.log('The gravity constant is:', GRAVITY);

// Mutating vs reassigning
const pets = ['cat', 'dog'];
pets.push('parrot'); // OK (mutates array)
console.log(pets);
// pets = []                // NOT OK (reassigns the const)

// Modern JavaScript features
console.log('\n--- Modern JavaScript Features ---');

// Array destructuring
const [first, second, ...rest] = primeNumbers;
console.log('First prime:', first);
console.log('Second prime:', second);
console.log('Rest of primes:', rest);

// Object destructuring
const person = { name: 'Bob', age: 30, city: 'New York' };
const { name, age, city = 'Unknown' } = person;
console.log(`${name} is ${age} years old and lives in ${city}`);

// Spread operator with arrays
const morePrimes = [17, 19, 23];
const allPrimes = [...primeNumbers, ...morePrimes];
console.log('All primes:', allPrimes);

// Spread operator with objects
const extendedPerson = { ...person, occupation: 'Developer', age: 31 };
console.log('Extended person:', extendedPerson);
