# Amazon Junior Software Developer with GenAI
**Professional Certificate - Coursera**

> Documenting my journey through Amazon's 7-course software development program

## 📊 Progress Overview

**Overall**: Course 1 of 7 | ~14% Complete  
**Current**: Module 1.3 - Strings & Arrays  
**Start Date**: October 6, 2025  
**Target Completion**: February 2026

| # | Course | Duration | Status | Completion |
|---|--------|----------|--------|------------|
| 1 | [Introduction to Software Development](./01-intro-to-software-dev/) | 28 hrs | 🔄 In Progress | 30% |
| 2 | [Programming with Java](./02-programming-with-java/) | 26 hrs | ⬜ Not Started | 0% |
| 3 | [Data Structures & Algorithms](./03-data-structures-algorithms/) | 43 hrs | ⬜ Not Started | 0% |
| 4 | [Database Management (Java & SQL)](./04-database-java-sql/) | 30 hrs | ⬜ Not Started | 0% |
| 5 | [Full Stack Web Development](./05-full-stack-web-dev/) | 33 hrs | ⬜ Not Started | 0% |
| 6 | [Generative AI in Software Development](./06-genai-in-software-dev/) | 17 hrs | ⬜ Not Started | 0% |
| 7 | [Application Development (Capstone)](./07-application-development/) | 23 hrs | ⬜ Not Started | 0% |

**Total**: 200 hours

## 🎯 Key Skills & Technologies

- **Languages**: Java, SQL, JavaScript
- **Concepts**: OOP, Data Structures, Algorithms, Full-Stack Development
- **Tools**: Git, MySQL, GenAI tools
- **Frameworks**: (TBD as courses progress)

## 🏆 Completed Projects

- [ ] Virtual Zoo Application (Course 1)
- [ ] TBD (Course 7 - Capstone)

## 🛠️ Development Environment

- **Editor**: Zed Editor
- **Java Version**: OpenJDK 21
- **OS**: Arch Linux

---

What I currently use for development:

- **Editor**: Zed Editor
- **Build Tool**: javac 
- **Java Version**: OpenJDK 21
- **OS**: Arch Linux

I've also build a custom wrapper to compile and run Java programs and delete class files upon completion.

If you're using linux, you can add this function to your .bashrc or .zshrc file:

```bash
jrun() {
  if [ -z "$1" ]; then
    echo "Usage: jrun file.java [args...]"
    return 1
  fi
  
  local file="$1"
  shift 1

  if [[ ! -f "$file" ]]; then
    echo "Error: File '$file' not found"
    return 1
  fi

  local classname="${file%.java}"
  echo "Classname: $classname"

  # Compile
  if ! javac "$file"; then
    echo "Compilation failed"
    return 1
  fi

  # Run
  if ! java "$classname" "$@"; then
    echo "Execution failed"
    rm -f "${classname}.class"
    return 1
  fi

  # Cleanup
  rm -f "${classname}.class"
}
```

Usage: 

```bash
jrun file.java [args...] 
```

This will: 
- search for the file
- compile it using javac
- run it with the provided arguments
- delete the class file upon completion

This function helps maintain the directory clean by automatically deleting the generated class file after execution.

---

*Last updated: December 6, 2025*
