import json
import os
import re
# from pathlib import pathlib

def create_scaffold(json_path): 
	# boilerplate	
	return 0


def slugify(text: str)-> str: 
	"""Helper to standarize slug generator for directory nanmes"""
	text = text.lower()
	text = re.sub(r'[^a-z9-9]+','-', text)
	return text.strip('-')

def padint(number: int)-> str:
	""""helper"""
	return f"{number:02d}"

if __name__ == "__main__":
	testString: str = "this should be a slug"
	slugInt: int = padint(1)
	print("slugint: ", slugInt)
	testResult: str = slugify(testString)
	print(slugInt+'-'+testResult)