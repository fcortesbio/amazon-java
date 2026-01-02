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

async def fetch_specialization_data():
    url = conf.url

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle")

        # Select the course cards

        ## 1. wait for a course-like element to exist

        try:
            await page.wait_for_selector('h3', timeout=10000)
        except:
            print("Timedout waiting for h3 elements")
        
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
                                "url": course_url
                            }
                    break
            
            if courses_data:
                break
        
        print(f"Extracted {len(courses_data)} courses")

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
