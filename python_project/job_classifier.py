def greeting(name):
    print(f"Hello {name}, welcome to the Job Classifier!")
    
def instructions():
    instruction = """The first thing you are expected to do is:
1. Put in your name which you would have definitely done before now.
2. Type in the skills you have (separated by commas)
3. Press enter and await the result
4. If you want to exit the program type in exit in the skills requested"""
    print(instruction)

List_of_jobs = {
    "Software Developer": [
        "Programming (Python, Java, C++)",
        "Problem Solving",
        "Data Structures and Algorithms",
        "Version Control (Git)",
        "Database Management",
        "Software Testing",
        "Object-Oriented Programming (OOP)",
        "Agile Methodology"
    ],
    "Data Scientist": [
        "Data Analysis",
        "Machine Learning",
        "Statistical Modeling",
        "Python, R",
        "Data Visualization (Matplotlib, Seaborn)",
        "Big Data Technologies (Hadoop, Spark)",
        "SQL, NoSQL",
        "Data Preprocessing"
    ],
    "Web Developer": [
        "HTML, CSS, JavaScript",
        "Frontend Frameworks (React, Angular, Vue)",
        "Backend Development (Node.js, Django, Flask)",
        "Responsive Design",
        "Version Control (Git)",
        "Database Management (MySQL, MongoDB)",
        "REST APIs",
        "Cross-Browser Compatibility"
    ],
    "Graphic Designer": [
        "Adobe Photoshop",
        "Adobe Illustrator",
        "UI/UX Design",
        "Typography",
        "Logo Design",
        "Wireframing & Prototyping",
        "Creative Thinking",
        "Branding & Identity"
    ],
    "Project Manager": [
        "Project Management",
        "Agile & Scrum Methodology",
        "Time Management",
        "Budgeting & Cost Management",
        "Risk Management",
        "Team Leadership",
        "Stakeholder Management",
        "Communication Skills"
    ],
    "Digital Marketing Specialist": [
        "SEO (Search Engine Optimization)",
        "Content Marketing",
        "PPC (Pay-Per-Click)",
        "Social Media Marketing",
        "Email Marketing",
        "Google Analytics",
        "Marketing Automation",
        "Conversion Rate Optimization"
    ],
    "Civil Engineer": [
        "Construction Management",
        "Structural Analysis",
        "CAD Software (AutoCAD, Revit)",
        "Project Management",
        "Geotechnical Engineering",
        "Material Science",
        "Surveying",
        "Building Codes and Standards"
    ],
    "Nurse": [
        "Patient Care",
        "Medical Terminology",
        "Clinical Skills",
        "Pharmacology",
        "Healthcare Documentation",
        "First Aid & CPR",
        "Medical Equipment Handling",
        "Communication with Patients and Families"
    ],
    "Sales Manager": [
        "Sales Strategy",
        "Lead Generation",
        "Customer Relationship Management (CRM)",
        "Negotiation Skills",
        "Team Leadership",
        "Market Research",
        "Sales Forecasting",
        "Product Knowledge"
    ],
    "Teacher": [
        "Lesson Planning",
        "Classroom Management",
        "Subject Expertise",
        "Communication Skills",
        "Technology Integration",
        "Assessment and Evaluation",
        "Adaptability",
        "Patience & Empathy"
    ]
}

# Get user input
names = input("What is your name? ")
greeting(names)
instructions()
while True:
    skills = input("What type of skills do you have? ").strip().lower().split(",")
# Clean up skills (remove extra spaces)
    skills = [skill.strip() for skill in skills]

    found_jobs = []

# Check if any skill matches a job
    for job, job_skills in List_of_jobs.items():
        for skill in skills:
            if any(skill.lower() in js.lower() for js in job_skills):  # Case-insensitive match
                found_jobs.append(job)
                break  # Avoid duplicate job listings

# Remove duplicates
    found_jobs = list(set(found_jobs))

# Print results
    if found_jobs:
        print(f"Based on your skills, you might be interested in: {', '.join(found_jobs)}")
        quest = str(input("Do you want to try it again? (y/n)"))
        if quest == "y" or quest == "Y":
            continue
        else:
            break
    else:
        print("No matching job found. Try another skill.")

