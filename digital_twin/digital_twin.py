import re

class DigitalTwin:
    def __init__(self):
        self.name = 'Prateek Ghorawat, M.Eng'
        self.location = 'Munich, Germany (Open for Relocation)'
        self.languages = {'German': 'B1', 'English': 'C2'}
        self.email = 'prateek.ghorawat1999@gmail.com'
        self.phone = '+49 17677872804'
        self.linkedin = 'https://linkedin.com/in/prateek-ghorawat'
        self.experience = [
            {'company': 'Celonis', 'role': 'AI & Data Analyst', 'duration': 'Oct 2025 - Apr 2026', 'responsibilities': [
                'Developed AI-driven analytics solutions.',
                'Built data processing pipelines with Python and SQL.',
                'Created ML classification models.',
                'Automated workflows using LangChain.'
            ]},
            {'company': 'BMW AG', 'role': 'AI/ML Engineer & Data Analyst', 'duration': 'Apr 2024 - Oct 2025', 'responsibilities': [
                'Delivered AI and data analytics solutions.',
                'Built models achieving high forecasting accuracy.',
                'Developed dashboards in Power BI.'
            ]},
            {'company': 'Lacritz AI', 'role': 'Machine Learning Intern', 'duration': 'May 2023 - Jul 2023', 'responsibilities': [
                'Developed NLP pipelines and improved model performance.',
                'Worked with AWS services.'
            ]},
            {'company': 'Johnson Controls', 'role': 'Engineering & Automation Analyst', 'duration': 'Oct 2021 - Dec 2022', 'responsibilities': [
                'Delivered data-driven automation solutions.'
            ]}
        ]
        self.education = [
            {'institution': 'Hochschule Schmalkalden', 'degree': 'M.Eng in AI Product Development', 'duration': 'Oct 2022 - Dec 2025'},
            {'institution': 'Jain University', 'degree': 'B. Tech in Industrial Design', 'duration': 'Jun 2017 - Jul 2021'}
        ]
        self.skills = ['Python', 'SQL', 'TensorFlow', 'PyTorch', 'Power BI', 'AWS']

    def get_summary(self):
        return f'{self.name}, located in {self.location}. Skills: {', '.join(self.skills)}.'

    def display_experience(self):
        for job in self.experience:
            print(f"{job['role']} at {job['company']} ({job['duration']}):")
            for responsibility in job['responsibilities']:
                print(f"- {responsibility}")

    def answer_question(self, question):
        question = question.lower()
        if re.search(r'name|who you are', question):
            return f'I am {self.name}.'
        elif re.search(r'location|where you are', question):
            return f'I am located in {self.location}.'
        elif re.search(r'email|contact', question):
            return f'You can contact me at {self.email}.'
        elif re.search(r'phone|number', question):
            return f'My phone number is {self.phone}.'
        elif re.search(r'education|where did you study', question):
            return f'I studied at {self.education[0]["institution"]} for my M.Eng and at {self.education[1]["institution"]} for my B. Tech.'
        else:
            return "I'm sorry, I can't answer that question."  

# Interactive Session
if __name__ == '__main__':
    twin = DigitalTwin()
    print(twin.get_summary())
    while True:
        user_input = input('Ask about me: ')
        if user_input.lower() in ['exit', 'quit']:
            break
        response = twin.answer_question(user_input)
        print(response)