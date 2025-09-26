# Lab 15: Using JavaScript Objects

## Objectives

- Learn how to create and use JavaScript objects.
- Understand key–value pairs and property access.
- Add methods to objects and use `this`.

## Duration

30–40 minutes

## Materials Needed

- VSCode
- Node.js or browser console

## Instructions

1. Create a file `objects.js`.
2. Define and log an object:

   ```javascript
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
   ```

3. Add a new property:
   ```javascript
   person.job = 'Web Developer';
   console.log(person);
   ```
4. Loop through object properties:

   ```javascript
   for (let key in person) {
     console.log(key, person[key]);
   }
   ```

5. **Modern Object Features** (explore these additional features):

   Object destructuring:

   ```javascript
   const { name, age } = person;
   console.log(`Destructured: ${name} is ${age} years old`);
   ```

   Shorthand property syntax:

   ```javascript
   const city = 'New York';
   const country = 'USA';
   const location = { city, country }; // same as { city: city, country: country }
   ```

   Computed property names:

   ```javascript
   const propName = 'dynamicProperty';
   const dynamicObj = {
     [propName]: 'This property name was computed!',
   };
   ```

   Compare arrow functions vs regular functions as methods:

   ```javascript
   const modernPerson = {
     name: 'Bob',
     greet: function () {
       console.log(`Hello, I'm ${this.name}`); // 'this' works
     },
     arrowGreet: () => {
       console.log(`Arrow: ${this?.name || 'undefined'}`); // 'this' is different!
     },
   };
   ```

6. **ES6 Classes** (modern alternative to object literals):

   ```javascript
   class Person {
     constructor(name, age) {
       this.name = name;
       this.age = age;
     }

     greet() {
       console.log(`Hi from class! I'm ${this.name}`);
     }

     static species() {
       return 'Homo sapiens';
     }
   }

   const classPerson = new Person('Charlie', 35);
   classPerson.greet();
   ```

## Discussion and Sharing

- What's the difference between dot and bracket notation?
- Why is `this` useful inside methods?
- How do objects help organize data?
- **Enhanced Questions:**
  - How does object destructuring make code more readable?
  - When would you use computed property names?
  - What's the difference between arrow functions and regular functions as object methods?
  - How do ES6 classes compare to object literals for creating multiple similar objects?
