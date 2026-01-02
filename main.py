import json
import asyncio
from playwright.async_api import async_playwright

especialization_url="https://www.coursera.org/professional-certificates/amazon-junior-software-developer"

async def fetch_specialization_data():
    url = especialization_url

    async with async_playwright() as p:
        


def main():
    print("Hello from amazon-java!")


if __name__ == "__main__":
    main()
