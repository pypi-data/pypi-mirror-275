# PyResumeParser

PyResumeParser is a Python package designed to parse resume PDF files and extract key entities such as names, emails, phone numbers, education details, skills, and more. It utilizes `spaCy` and `pdfminer.six` for natural language processing and PDF text extraction.

## Installation

You can install PyResumeParser using pip:

```bash
pip install pyresumeparser
Usage
As a Python Module
To use PyResumeParser in your Python code, you can import the package and call the parse_resume function:

python
Copy code
import pyresumeparser

pdf_file = "resume.pdf"
parsed_resume = pyresumeparser.parse_resume(pdf_file)
print(parsed_resume)
From the Terminal
You can also use PyResumeParser directly from the terminal:

bash
Copy code
pyresumeparser resume.pdf
This command will parse the specified PDF file and print the extracted entities in JSON format.

Example Output
Here is an example of the JSON output you might get from parsing a resume:

json
Copy code
{
    "first_name": ["John"],
    "last_name": ["Doe"],
    "email": ["johndoe@example.com"],
    "phone": ["+1 234 567 890"],
    "country": ["USA"],
    "state": ["California"],
    "city": ["San Francisco"],
    "pincode": ["94107"],
    "college_name": ["University of Example"],
    "education": ["BSc Computer Science"],
    "designation": ["Software Engineer"],
    "position_held": ["Lead Developer"],
    "companies_worked": ["Tech Company Inc."],
    "projects_worked": ["Project A", "Project B"],
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "total_experience": ["5 years"],
    "language": ["English"],
    "linkedin": ["https://linkedin.com/in/johndoe"],
    "github": ["https://github.com/johndoe"]
}
Requirements
The following packages are required to use PyResumeParser:

spacy==3.7.4
pdfminer.six==20231228
spacy-transformers==1.3.5
tqdm==4.66.4
You can install these packages using pip:

bash
Copy code
pip install -r requirements.txt
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue on GitHub.

License
This project is licensed under the MIT License.

Author
Developed by Palash Khan.

Feel free to reach out with any questions or feedback. Happy parsing!

