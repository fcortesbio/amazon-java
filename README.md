# Amazon Junior Software Developer: 90-Day Apprenticeship


This repository documents my 90-day learning path into systematic Java engineering. 

The main learning resource: [Amazon Junior Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/amazon-junior-software-developer)

Rather than simply following the outline, I am treating this specialization as a "Software Apprenticeship"—focusing on system architecture, manual syntax mastery (no AI assistance), and automated workflow tooling.

These are my notes and documentation while completing the Java Specialization in Coursera. I'll try to document as best as possible my workflow, personalized tools and concepts and lessons learned, as well as the progress.

---

## High-Density Environment

- **OS**: [Arch Linux](https://archlinux.org/)(Kernel 6.12+)

- **Runtime**: [OpenJDK 25](https://openjdk.org/) (Experimental/Latest)

- **Editor**: [Sublime Text](https://www.sublimetext.com/) + Vintage Mode (No AI completion to force internalizing Java syntax).

- Shell: [Bash](https://www.gnu.org/software/bash/) 5.3.9

- **CLI Stack**: [uv](https://docs.astral.sh/uv/) (Python scripts management), [bat](https://github.com/sharkdp/bat) (syntax-highlit cat), [httpie](https://github.com/httpie/cli) (API testing).

## Custom Java CLI Tools
To maintain a fast feedback loop without an IDE, I use a set of [custom bash](https://github.com/fcortesbio/bash-custom/blob/main/java-tools.sh) utilities:

- `jnew <ClassName>`: Scaffolds a new Java file with standard boilerplate and opens it in Sublime Text.
- `jrun <File.java>`: A wrapper that handles `javac` compilation, execution, and automatic `.class` cleanup in one step.

## Git Workflow Utility

To minimize friction between coding and documentation, I use a custom [git-tools](https://github.com/fcortesbio/bash-custom/blob/main/git-tools.sh2) wrapper:

- gacp "<message>": A streamlined command that stages all changes, creates a commit, and pushes to the current branch in a single atomic operation. This ensures my progress logs and code snippets are backed up instantly as I complete course milestones.


# Project Architecture & Automation

To avoid manual folder creation, I use a custom Playwright-based crawler and Scaffold engine to synchronize the local filesystem with the Coursera curriculum. 

1. The Scraper [(`scraper.py`)](./scrapper.py)

Uses Playwright to extract application/ld+json (Linked Data) from Coursera. The script outputs a JSON file with structured data for courses and modules of the Specialization. Configuration is currently hardcoded in the python script, so if working on a different Specialization you may want to manually add the Coursera Specialization link and name. 

2. The Scaffolder [(scaffold.py)](./scaffold.py)

Consumes the generated JSON to build a lexicographically sorted directory tree (01-name, 02-name) with pre-populated Markdown templates for notes and task tracking.

## Quick Start

**Setup Environment**

Make sure uv is installed, then initialize the environment:

```bash
# Clone the repository
git clone https://github.com/fcortesbio/amazon-java && cd amazon-java

# Install Playwright binaries via uv
uv run playwright install chromium
```

**Scraping a Different Specialization**

If you wish to use these tools for a different Coursera specialization, you can jump back to the core tooling state before the Amazon-specific folders were committed:

```bash
# Reset to the tooling-only state
git checkout dd391af

# Edit scraper.py with your target URL and specialization name, then:
uv run scraper.py

# Confirm the contents of your json file before running the scaffold

bat certificate_structure.json

uv run scaffold.py
```

## Roadmap (90 Days)

- [ ] Phase 1 (Days 1-30): Java Fundamentals & OOP (Courses 1-3)

- [ ] Phase 2 (Days 31-60): SQL & Persistence (Course 4 & 7)

- [ ] Phase 3 (Days 61-90): Spring Boot & Portfolio Projects (Course 5-6)

## Progress, Logs and Comments

Current module: [1.1 - Getting Started with Java](/01-introduction-to-software-development/m01-getting-started-with-java/notes.md) 

## Future enhancements

- Moving forward, I plan to turn the scaffold/scrapper logic into a potential CLI tool. 
- Externalize configuration to an environment file instead of hardcoded
