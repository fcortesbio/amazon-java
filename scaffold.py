import json
import re
from pathlib import Path

def create_scaffold(json_path): 
	with open(json_path, 'r') as f:
		data = json.load(f)

	base_dir = Path(__file__).parent
	base_dir.mkdir(exist_ok=True)

	# Sort Courses by order to ensure directory naming stays consistent
	sorted_courses = sorted(data['courses'].values(), key = lambda x: x['order'])
	print(sorted_courses)

	for course in sorted_courses:
		# Create course directory. e.g., 01-programming-with-java
		course_slug = slugify(course['name'])
		course_dirname = f"{course['order']:02d}-{course_slug}"
		course_path = base_dir / course_dirname
		course_path.mkdir(exist_ok=True)

		# Create Course README
		readme_content = course_readme_template.format(
			name = course['name'],
			url = course['url'],
			description = course.get('description', 'N/A'),
			progress_list = "\n".join([f"- [ ] {m}" for m in course['modules']])
			)

		(course_path / "README.md").write_text(readme_content)

		# Create module subdirectories
		for i, module_name in enumerate(course['modules'], 1):
			module_slug = slugify(module_name)
			module_dirname = f"m{i:02d}-{module_slug}"
			module_path = course_path / module_dirname
			module_path.mkdir(exist_ok=True)

			# Create module-level notes file
			notes_content = module_notes_template.format(
				index = i, 
				module_name = module_name
				)
			(module_path / "notes.md").write_text(notes_content)
		print(f"Scaffolding complete. Root: {base_dir.absolute()}")

def slugify(text: str)-> str: 
	"""Helper to standarize slug generator for directory nanmes"""
	text = text.lower()
	text = re.sub(r'[^a-z0-9]+','-', text)
	return text.strip('-')

def padint(number: int)-> str:
	""""helper"""
	return f"{number:02d}"


course_readme_template: str = """
# **{name}**
**Link:**[{url}]({url})

## Description
{description}

## Progress Tracker
{progress_list}

---
*Generated with Scaffold.py*
"""	

module_notes_template: str = """
# **Module {index}: {module_name}**

## Objectives
- [] Complete video lectures
- [] Finish labs/quizzes

## Notes
> Start taking notes for {module_name} here...

---
[Back to Parent Course](../README.md)
"""

if __name__ == "__main__":
	# testString: str = "this should be a slug"
	# slugInt: int = padint(1)
	# print("slugint: ", slugInt)
	# testResult: str = slugify(testString)
	# print(slugInt+'-'+testResult)

	create_scaffold("certificate_structure.json")

