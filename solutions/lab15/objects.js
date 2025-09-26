const person = {
  name: 'Alice',
  age: 25,
  greet: function () {
    console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
  },
};

console.log(person.name);
console.log(person['age']);
person.greet();

// Add a new property
person.job = 'Web Developer';
console.log(person);

// Loop through object properties
for (let key in person) {
  console.log(key, person[key]);
}

console.log('\n--- Modern Object Features ---');

// Object destructuring
const { name, age } = person;
console.log(`Destructured: ${name} is ${age} years old`);

// Shorthand property syntax
const city = 'New York';
const country = 'USA';
const location = { city, country }; // same as { city: city, country: country }
console.log('Location object:', location);

// Computed property names
const propName = 'dynamicProperty';
const dynamicObj = {
  [propName]: 'This property name was computed!',
  [`${propName}2`]: 'Another dynamic property',
};
console.log('Dynamic object:', dynamicObj);

// Arrow functions as methods (be careful with 'this')
const modernPerson = {
  name: 'Bob',
  age: 30,
  // Regular function - 'this' refers to the object
  greet: function () {
    console.log(`Hello, I'm ${this.name}`);
  },
  // Arrow function - 'this' is lexically bound (different behavior!)
  arrowGreet: () => {
    console.log(`Arrow function: this.name is ${this?.name || 'undefined'}`);
  },
};

modernPerson.greet();
modernPerson.arrowGreet();

// ES6 Classes as modern alternative to object literals
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(
      `Hi from class! I'm ${this.name} and I'm ${this.age} years old.`
    );
  }

  static species() {
    return 'Homo sapiens';
  }
}

const classPerson = new Person('Charlie', 35);
classPerson.greet();
console.log('Species:', Person.species());
