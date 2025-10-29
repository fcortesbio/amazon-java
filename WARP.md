# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a learning repository documenting progress through Amazon's Junior Software Developer with GenAI Professional Certificate (7-course program on Coursera). The repository contains course notes, exercises, and projects organized by course number.

**Current Status**: Course 1 (Introduction to Software Development) - Module 1.3  
**Progress**: ~14% complete overall, 30% through Course 1

## Repository Structure

The repository follows a course-based structure with standardized organization:

```
amazon-java/
├── 0X-course-name/          # Each course has its own directory
│   ├── notes/               # Markdown notes organized by module
│   ├── exercises/           # Practice code organized by topic
│   ├── projects/            # Course-specific projects
│   └── README.md            # Course progress and objectives
├── resources/               # Shared learning resources
│   ├── cheatsheets/
│   ├── references/
│   └── tools/
├── portfolio/               # Portfolio-worthy projects
├── LEARNING_LOG.md          # Daily learning journal
└── README.md                # Overall program progress
```

**Key directories:**
- `01-intro-to-software-dev/` - Currently active; contains Java basics exercises
- `07-application-development/` - Future capstone project location
- `resources/` - Cross-course reference materials

## Build & Run Commands

This repository contains standalone Java files that are compiled and run individually. There is **no centralized build system** (no Gradle/Maven setup at repository root).

### Compiling Java Files

Individual exercise files are compiled directly with `javac`:

```bash
# Compile a single file
javac path/to/File.java

# Run the compiled class
java -cp path/to File
```

**Example workflow:**
```bash
cd 01-intro-to-software-dev/exercises/basics
javac CurrencyConversion.java
java CurrencyConversion
```

### Testing

Currently no automated testing framework is configured. The user prefers Python for testing according to project rules, but no test suite exists yet for this repository.

## Development Environment

**Editor**: Neovim with nvim-jdtls plugin  
**Java Version**: OpenJDK 21  
**OS**: Arch Linux

The nvim-jdtls plugin provides:
- Smart code completions
- Diagnostics and error checking
- Hover documentation
- Document symbols
- Syntax highlighting
- Auto-imports

## Code Organization

### Exercise Files
Exercise files are **standalone Java classes** with `public static void main()` methods. They do not use packages and are not part of a larger application structure.

**Typical structure:**
```java
public class ExerciseName {
    public static void main(String[] args) {
        // Exercise implementation
    }
}
```

### Projects
Future projects (like the Virtual Zoo) may use Gradle with the standard structure documented in course notes:
- Root directory with `settings.gradle.kts` and `gradlew`
- `app/` module containing source code
- Package declarations matching directory structure (`package org.example;`)

When a project uses Gradle:
```bash
# From project root (where gradlew exists)
./gradlew run        # Build and run
./gradlew build      # Build only
./gradlew test       # Run tests
```

## Learning Workflow

This repository tracks a structured learning journey. When working here:

1. **Check progress**: Review `README.md` and `LEARNING_LOG.md` for current position
2. **Find context**: Course READMEs contain module objectives and key takeaways
3. **Exercises are educational**: Code may be intentionally simple or demonstrate specific concepts
4. **Notes are primary**: The `notes/` directories contain detailed learning material

## Important Files

- `LEARNING_LOG.md` - Daily learning entries with insights and challenges
- `README.md` - High-level progress tracker and course overview
- `01-intro-to-software-dev/README.md` - Current course status and structure
- `01-intro-to-software-dev/notes/module-01-getting-started.md` - Detailed course content

## Git Workflow

Per user rules, adhere to these practices:
- Never commit directly to main (except documentation fixes)
- Check active branch with `git status` before starting work
- Create descriptive feature branches (e.g., `feature/virtual-zoo`, `fix/exercise-typo`)
- Use concise, imperative commit messages (e.g., "fix: correct variable type in CurrencyConversion")
- Run `git pull --rebase` before pushing when collaborating
