from pypdf import PdfReader

reader = PdfReader(r"C:\Users\anike\Downloads\Aniket_Resume.pdf")
page = reader.pages[0]

text = page.extract_text()

import re

def extract_email(text):
    match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\b\d{10}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b', text)
    return match.group(0) if match else None

def extract_name(text):
    lines = text.split('\n')
    return lines[0].strip() if lines else None

def extract_skills(text):
    skills_list = ["Python", "Data Analysis", "Machine Learning", "SQL", "Java"]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills

def parse_resume(text):
    resume_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        # Add similar functions for experience, education, etc.
    }
    return resume_data

parsed_data = parse_resume(text)
print(parsed_data)
