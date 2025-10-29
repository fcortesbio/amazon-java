# Java Syntax Quick Reference

A quick reference guide for Java syntax and common patterns learned throughout the certificate program.

---

## Variables & Data Types

### Primitive Types

```java path=null start=null
// Integer types
byte age = 127;              // 8-bit: -128 to 127
short year = 2025;           // 16-bit: -32,768 to 32,767
int count = 100000;          // 32-bit: ~-2.1B to 2.1B
long bigNum = 9223372036854775807L;  // 64-bit

// Floating-point types
float price = 19.99f;        // 32-bit decimal
double precise = 3.14159265; // 64-bit decimal (default)

// Other primitives
boolean isActive = true;     // true or false
char initial = 'A';          // Single character (16-bit Unicode)
```

### Reference Types

```java path=null start=null
String name = "Java Developer";  // Immutable text sequence
String[] names = {"Alice", "Bob"};  // Array of strings
```

---

## Operators

### Arithmetic

```java path=null start=null
int sum = 5 + 3;        // Addition: 8
int diff = 5 - 3;       // Subtraction: 2
int product = 5 * 3;    // Multiplication: 15
int quotient = 5 / 3;   // Division: 1 (integer division)
int remainder = 5 % 3;  // Modulus: 2
```

### Assignment

```java path=null start=null
int x = 10;
x += 5;  // x = x + 5;  (15)
x -= 3;  // x = x - 3;  (12)
x *= 2;  // x = x * 2;  (24)
x /= 4;  // x = x / 4;  (6)
x %= 5;  // x = x % 5;  (1)
```

### Relational (Comparison)

```java path=null start=null
5 == 5   // Equal to: true
5 != 3   // Not equal to: true
5 > 3    // Greater than: true
5 < 3    // Less than: false
5 >= 5   // Greater than or equal: true
5 <= 3   // Less than or equal: false
```

### Logical

```java path=null start=null
true && false   // AND: false (both must be true)
true || false   // OR: true (at least one must be true)
!true           // NOT: false (inverts the value)
```

### Unary

```java path=null start=null
int count = 5;
count++;  // Post-increment: count = 6
count--;  // Post-decrement: count = 5
++count;  // Pre-increment: count = 6
--count;  // Pre-decrement: count = 5
```

---

## String Methods

```java path=null start=null
String text = "Hello, World!";

// Common methods
text.length()              // 13
text.charAt(0)             // 'H'
text.substring(0, 5)       // "Hello"
text.toLowerCase()         // "hello, world!"
text.toUpperCase()         // "HELLO, WORLD!"
text.trim()                // Removes leading/trailing whitespace
text.replace("World", "Java")  // "Hello, Java!"
text.contains("World")     // true
text.startsWith("Hello")   // true
text.endsWith("!")         // true
text.split(",")            // ["Hello", " World!"]
```

---

## Control Flow

### If-Else Statements

```java path=null start=null
if (condition) {
    // executes if condition is true
} else if (anotherCondition) {
    // executes if anotherCondition is true
} else {
    // executes if all conditions are false
}
```

### Switch Statements

```java path=null start=null
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code if no cases match
}
```

### Loops

```java path=null start=null
// For loop
for (int i = 0; i < 10; i++) {
    // repeats 10 times
}

// While loop
while (condition) {
    // repeats while condition is true
}

// Do-While loop
do {
    // executes at least once
} while (condition);

// Enhanced for loop (for arrays/collections)
for (String item : array) {
    // iterates through each element
}
```

---

## Methods

```java path=null start=null
// Method declaration
public static returnType methodName(parameters) {
    // method body
    return value;  // if returnType is not void
}

// Example
public static int add(int a, int b) {
    return a + b;
}
```

---

## Classes and Objects (OOP Basics)

```java path=null start=null
// Class definition
public class Person {
    // Fields (attributes)
    private String name;
    private int age;
    
    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Methods
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}

// Creating objects
Person person = new Person("Alice", 30);
person.getName();  // "Alice"
```

---

## Arrays

```java path=null start=null
// Declaration and initialization
int[] numbers = {1, 2, 3, 4, 5};
String[] names = new String[10];  // Creates array of size 10

// Accessing elements
int first = numbers[0];  // 1
numbers[2] = 10;         // Changes third element to 10

// Array length
int size = numbers.length;  // 5

// Iterating through arrays
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

// Enhanced for loop
for (int num : numbers) {
    System.out.println(num);
}
```

---

## Input/Output

```java path=null start=null
// Output
System.out.println("Hello");  // Prints with newline
System.out.print("Hello");    // Prints without newline

// String concatenation in output
System.out.println("Value: " + variable);

// Input (requires import java.util.Scanner)
Scanner scanner = new Scanner(System.in);
String input = scanner.nextLine();     // Read line
int number = scanner.nextInt();        // Read integer
double decimal = scanner.nextDouble(); // Read double
```

---

## Comments

```java path=null start=null
// Single-line comment

/*
 * Multi-line comment
 * Used for longer explanations
 */

/**
 * Javadoc comment
 * Used for documentation
 * @param parameter description
 * @return return value description
 */
```

---

*This cheatsheet will be updated as new concepts are learned throughout the certificate program.*
