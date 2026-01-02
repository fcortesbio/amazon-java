# Learning notes on: [Amazon Junior Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/amazon-junior-software-developer)

These are my notes and documentation while completing the Java Specialization in coursera. I'll try to document as best as possible my workflow, personalized tools and concepts learned, as well as the progress.

---

## Getting Started. 

**Environment**: 
OS: [Arch Linux](https://archlinux.org/) (6.18.2-arch2-1)
Shell: [Bash](https://www.gnu.org/software/bash/) 5.3.9
[OpenJDK Runtime Environment](https://openjdk.org/) (build 25.0.1)
Code Editor: The course outline recommends [IntelliJ IDEA](https://www.jetbrains.com/idea/download/?section=linux). I aim for a minimal setup, with only basic completions and no IA features to enhance learning, so I opted to use [Sublime Text](https://www.sublimetext.com/)

**Project structure**


I use a playwrite scrapper to automate the course structure set up. 

To start, you may want to clone the repo: 

```bash
git clone https://github.com/fcortesbio/amazon-java
cd amazon-java 
```

Make uv is in your machine

Install playwright and install a browser. 

Execute and check certificate data:

```
uv --version
uv run playwright install chromium
uv run main.py && bat certificate_structure.json
```


