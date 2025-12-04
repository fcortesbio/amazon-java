# Module 01 - Getting Started

## 1.1. Software Development Landscape

**Key Concepts**

- Software Development is the process of creating software.
- Software is a set of instructions that tell a computer what to do.
- Software Development is a creative process.

* **SDLC** (Software Development Life Cycle)

  - Planning
  - Analysis
  - Design
  - Implementation
  - Testing
  - Deployment
  - Maintenance

* **Roles**:

  - Frontend: Visuals/UI (HTML, CSS, JS)
  - Backend: Logic, Database, APIs, Security (Java, Python, Node.js)
  - DevOps: Infrastructure, CI/CD, Monitoring

* Compiled vs. Interpreted Languages: Java is a "write once, run anywhere" language (uses JVM).

Course Project: Virtual Zoo

- **Goal**: Build a menu-driven zoo app.
- **Core concepts Applied**: Inheritance (Animal -> Tiger), Interfaces (Swimming), Polymorphism.

## 1.2. Variables & Data Types

**Key Terms**

- **Variable**: A named storage location. Requires a **data type** (what kind of data) and an **Identifier** (name).

- **Declaration**: The process of creating a variable.

```java
int score;
```

- **Initialization**: The process of assigning a value to a variable.

```java
int score = 10;
```

**Primitive Data Types**

| Type    | Size   | Stores           | Example                |
| ------- | ------ | ---------------- | ---------------------- |
| int     | 32-bit | Whole numbers    | int year = 2025;       |
| double  | 64-bit | Decimals         | double price = 19.99;  |
| boolean | 1-bit  | True/False       | boolean isOpen = true; |
| char    | 16-bit | Single character | char grade = 'A';      |

**Note**: `String` is **not** a primitive data type; it is an Object (Reference Type).

**Syntax: Declaration & Initialization**

```java
// Best Practice: Combine declaration & initialization
dataType variableName = value;

int totalScore = 100;
String userName = "DevOne"; // Double Quotes for String
boolean isActive = true; // No Quotes for boolean
char initial = 'D'; // Single Quote for char
```

**Operators**

- **Arithmetic**: +, -, \*, /, %
- **Assignment**: =
- **Comparison**: ==, !=, >, <, >=, <=
- **Logical**: &&, ||, !

## 1.3. Strings (Text Handling)

**Key concepts**

- **Methods**: Functions that operate on objects of certain types (e.g., String).
- **Immutable**: Once created, cannot be changed. Methods like `toUpperCase()` return a new string; they do not modify the original string.
- **Zero-indexing**: First character is at index 0.

**Core String Methods Cheat Sheet**

```java

String text = "Java";

// 1. Length
int len = text.length(); // Returns 4

// 2. Character at specific index
char letter = text.charAt(0); // Returns 'J'
// ERROR: text.charAt(4) -> StringIndexOutOfBoundsException

// 3. Substring (Slicing)
// substring(start, end) -> End index is EXCLUSIVE
String part = text.substring(0, 2); // Returns "Ja" (Indices 0 and 1)
String endPart = text.substring(2); // Returns "va" (Index 2 to end)

// 4. Comparison (CRITICAL)
// DO NOT use '==' for Strings. Use .equals()
boolean match = text.equals("Java"); // true

// 5. Case manipulation
String big = text.toUpperCase(); // "JAVA"
String small = text.toLowerCase(); // "java"

```

**Java vs. Python "String-Manipulation Gotchas"**

Unlike python, Java data accessing is strict and requires bounds checking.

- No negative indexing: `text.charAt(-1)` -> StringIndexOutOfBoundsException
- No out-of-bounds indexing: `text.charAt(5)` -> StringIndexOutOfBoundsException

Accessing an index that doesn't exists crashes the program unless the exception is handled.
