# Repository Navigation Guide

A quick reference for navigating and maintaining this learning repository.

---

## 📂 Directory Structure

```
amazon-java/
├── 01-intro-to-software-dev/     # Course 1 (28 hrs)
├── 02-programming-with-java/     # Course 2 (26 hrs)
├── 03-data-structures-algorithms/# Course 3 (43 hrs)
├── 04-database-java-sql/         # Course 4 (30 hrs)
├── 05-full-stack-web-dev/        # Course 5 (33 hrs)
├── 06-genai-in-software-dev/     # Course 6 (17 hrs)
├── 07-application-development/   # Course 7 (23 hrs) - Capstone
├── resources/                    # Shared resources across courses
├── portfolio/                    # Showcase of completed projects
├── LEARNING_LOG.md              # Daily/weekly reflections
└── README.md                    # Main overview & progress tracker
```

---

## 🎯 Typical Workflow

### Starting a New Module

1. Navigate to the appropriate course directory:
   ```bash
   cd 01-intro-to-software-dev/
   ```

2. Create or update notes file in `notes/`:
   ```bash
   nvim notes/module-02-control-flow.md
   ```

3. Work on exercises in `exercises/`:
   ```bash
   nvim exercises/loops/ForLoopPractice.java
   ```

4. Update course README to track progress:
   ```bash
   nvim README.md
   # Mark module as complete ✅
   # Update completion percentage
   # Add key takeaways
   ```

### Daily Learning Routine

1. **Update LEARNING_LOG.md** with today's entry:
   ```bash
   nvim LEARNING_LOG.md
   ```

2. **Take notes** as you learn:
   ```bash
   nvim 01-intro-to-software-dev/notes/module-XX.md
   ```

3. **Complete exercises** and save in appropriate directories

4. **Commit progress** (small, logical commits):
   ```bash
   git add -p
   git commit -m "feat: complete string manipulation exercises"
   ```

### Completing a Course

1. Update main README.md:
   - Change course status to "✅ Completed"
   - Update completion percentage
   - Update overall progress

2. Update course README with final takeaways

3. If applicable, move completed project to portfolio:
   ```bash
   ln -s ../01-intro-to-software-dev/projects/virtual-zoo portfolio/virtual-zoo
   ```

4. Commit the completion milestone:
   ```bash
   git commit -m "feat: complete Course 1 - Introduction to Software Development"
   ```

---

## 📝 File Naming Conventions

### Notes
- Use kebab-case: `module-01-getting-started.md`
- Include module number for easy sorting
- Keep descriptive but concise

### Exercises
- Use PascalCase for Java files: `StringManipulation.java`
- Group related exercises in subdirectories
- Include a README.md for complex exercise sets

### Projects
- Use kebab-case for directories: `virtual-zoo/`
- Follow standard project structure (src/, tests/, etc.)
- Always include a README.md

---

## 🔍 Finding Information

### By Course
Navigate directly to course folder: `01-intro-to-software-dev/`

### By Topic
Check `resources/cheatsheets/` for quick references

### By Date
Search `LEARNING_LOG.md` for specific learning sessions

### Code Examples
- Check course `exercises/` directories
- Review `resources/cheatsheets/java-syntax.md`

---

## 📊 Tracking Progress

### Update Main README
When you make progress, update `/README.md`:
- Course completion percentages
- Overall progress percentage
- Current focus
- Last updated date

### Update Course README
In each course's `README.md`:
- Check off completed modules
- Add key takeaways
- Update project status
- Document challenges and solutions

### Update Learning Log
Add entries to `LEARNING_LOG.md`:
- Today's focus
- Key insights
- Challenges faced
- Next steps

---

## 🛠️ Useful Commands

### View Repository Structure
```bash
tree -L 2 -I '.git'
```

### Find All Java Files
```bash
find . -name "*.java" -type f
```

### Search Notes for Topic
```bash
grep -r "inheritance" */notes/
```

### Count Completed Exercises
```bash
find . -name "*.java" -type f | wc -l
```

### View Git History
```bash
git log --oneline --graph
```

---

## 🎨 Customization Tips

### Add New Resource Type
```bash
mkdir resources/videos
echo "# Video Resources" > resources/videos/README.md
```

### Create Course Template
```bash
cp 02-programming-with-java/README.md new-course/README.md
# Edit and customize
```

### Add Custom Scripts
```bash
mkdir scripts/
# Add helpful automation scripts
```

---

## 📌 Best Practices

1. **Commit Often**: Small, logical commits are better than large ones
2. **Document as You Go**: Don't wait until later to take notes
3. **Review Regularly**: Revisit previous modules to reinforce learning
4. **Update Progress**: Keep READMEs current for motivation
5. **Backup**: Push to GitHub regularly
6. **Reflect**: Use LEARNING_LOG.md to track insights and growth

---

## 🆘 Troubleshooting

### Lost a File?
```bash
git log --all --full-history -- "path/to/file"
```

### Need to Reorganize?
1. Create new structure
2. Move files with `git mv` to preserve history
3. Update all READMEs with new paths
4. Commit with clear message

### Forgot Where Something Is?
```bash
find . -name "*keyword*"
grep -r "search term" .
```

---

*Keep this guide handy as you navigate through your learning journey!*
