import json
import asyncio
from playwright.async_api import async_playwright
from dataclasses import dataclass

@dataclass(frozen=True)
class CertificateConfig:
    name: str
    url: str
    output: str

conf = CertificateConfig(
    name = "Amazon Junior Software Developer Professional Certificate",
    url = "https://www.coursera.org/professional-certificates/amazon-junior-software-developer",
    output = "certificate_structure.json"

)

async def extract_course_modules(page, course_url, debug=False):
    """Extract module names from a course page."""
    try:
        print("  Visiting course page...")
        await page.goto(course_url, wait_until="domcontentloaded", timeout=30000)
        
        # Wait for content to load
        try:
            await page.wait_for_selector('h2, h3', timeout=5000)
        except:
            print("  Warning: Timeout waiting for content")
        
        # Try to extract from JSON-LD first
        json_ld_data = await page.evaluate('''
            () => {
                const scripts = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
                return scripts.map(s => {
                    try {
                        return JSON.parse(s.textContent);
                    } catch (e) {
                        return null;
                    }
                }).filter(d => d !== null);
            }
        ''')
        
        modules = []
        
        # Look for syllabus/hasPart structure in JSON-LD
        for data in json_ld_data:
            items = []
            if isinstance(data, dict):
                if '@graph' in data:
                    items = data['@graph']
                else:
                    items = [data]
            
            for item in items:
                if isinstance(item, dict) and item.get('@type') == 'Course' and 'hasPart' in item:
                    parts = item.get('hasPart', [])
                    for part in parts:
                        if isinstance(part, dict):
                            module_name = part.get('name', '')
                            if module_name:
                                modules.append(module_name)
                    break
            
            if modules:
                break
        
        # Fallback: scrape from DOM if JSON-LD didn't work
        if not modules:
            print("  JSON-LD failed, trying DOM scraping...")
            
            # Look for accordion items which contain module information
            accordion_items = await page.query_selector_all('[data-testid="accordion-item"]')
            
            if accordion_items:
                for item in accordion_items:
                    # Find h3 and check if it's followed by "Module X" text
                    h3 = await item.query_selector('h3')
                    if h3:
                        module_title = await h3.inner_text()
                        module_title = module_title.strip()
                        
                        # Verify it's a real module by checking for "Module X" nearby
                        parent = await h3.evaluate_handle('el => el.closest("div")')
                        parent_elem = parent.as_element()
                        if parent_elem:
                            parent_text = await parent_elem.inner_text()
                            # Check if this section mentions "Module" followed by a number
                            if 'Module' in parent_text and any(char.isdigit() for char in parent_text):
                                modules.append(module_title)
            
            # If accordion approach didn't work, try alternative
            if not modules:
                print("  Accordion extraction failed, trying alternative...")
                # Look for h3 elements near "Module N" text
                module_headers = await page.query_selector_all('h3')
                for h3 in module_headers:
                    # Get parent context
                    parent_handle = await h3.evaluate_handle('el => el.parentElement')
                    parent = parent_handle.as_element()
                    if parent:
                        parent_text = await parent.inner_text()
                        h3_text = await h3.inner_text()
                        
                        # Check if Module N appears near this h3
                        if 'Module' in parent_text and h3_text and len(h3_text) < 100:
                            if h3_text not in modules:
                                modules.append(h3_text)
                                if len(modules) >= 10:  # Safety limit
                                    break
        
        print(f"  Found {len(modules)} modules")
        return modules
    
    except Exception as e:
        print(f"  Error extracting modules: {e}")
        return []


async def fetch_specialization_data():
    url = conf.url

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = await context.new_page()
        
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"Error loading main page: {e}")
            await browser.close()
            return

        # Wait for content
        try:
            await page.wait_for_selector('h3', timeout=10000)
        except:
            print("Warning: Timeout waiting for h3 elements")
        
        # Extract JSON-LD structured data which contains course information
        json_ld_data = await page.evaluate('''
            () => {
                const scripts = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
                return scripts.map(s => {
                    try {
                        return JSON.parse(s.textContent);
                    } catch (e) {
                        return null;
                    }
                }).filter(d => d !== null);
            }
        ''')
        
        if not json_ld_data:
            print("Error: No JSON-LD data found on the page")
            await browser.close()
            return
        
        courses_data = {}
        
        # Find the Course schema with hasPart (may be nested under @graph)
        for data in json_ld_data:
            items_to_check = []
            
            if isinstance(data, dict):
                # Check if data has @graph (nested structure)
                if '@graph' in data:
                    items_to_check = data['@graph']
                else:
                    items_to_check = [data]
            
            for item in items_to_check:
                if isinstance(item, dict) and item.get('@type') == 'Course' and 'hasPart' in item:
                    courses = item.get('hasPart', [])
                    print(f"Found {len(courses)} courses in JSON-LD data")
                    
                    for i, course in enumerate(courses):
                        course_name = course.get('name', '')
                        course_desc = course.get('description', 'No description available')
                        course_url = course.get('url', '') or course.get('@id', '')
                        
                        if course_name:
                            slug = course_name.lower().replace(" ", "-").replace(":", "").replace(",", "")
                            courses_data[slug] = {
                                "name": course_name,
                                "description": course_desc,
                                "order": i + 1,
                                "url": course_url,
                                "modules": []
                            }
                    break
            
            if courses_data:
                break
        
        if not courses_data:
            print("Error: No courses found in JSON-LD data")
            await browser.close()
            return
        
        print(f"Extracted {len(courses_data)} courses")
        
        # Now visit each course page to extract modules
        print("\nExtracting modules from each course...")
        for i, (slug, course) in enumerate(courses_data.items(), 1):
            print(f"\n[{i}/{len(courses_data)}] {course['name']}")
            
            # Convert @id URL to actual course URL
            course_url = course['url']
            if '#mooc' in course_url:
                course_url = course_url.replace('#mooc', '')
            
            # Debug only first course
            modules = await extract_course_modules(page, course_url, debug=(i == 1))
            course['modules'] = modules

        specialization = {
            "name": conf.name,
            "link": conf.url, 
            "courses": courses_data
        }

        with open(conf.output, "w") as f:
            json.dump(specialization, f, indent=2)


        print(f"Structure saved to {conf.output}")
        await browser.close()




def main():
    asyncio.run(fetch_specialization_data())

if __name__ == "__main__":
    main()
