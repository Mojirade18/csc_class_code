# I want to make a job classifier where students get to say a skill they have then the code gives a list of what career has such skills.
def greeting(name):
    print(f"Hello {name}, welcome to job classifier")
    
def instructions():
    global instruction
    intruction = """The first thing you are expected to do is:
1. Put in your name
2. Type in the skills yo have
3. Click enter an await the result"""
    print(intruction)

List_of_jobs = {
    "Software Developer": [
        "Programming (Python, Java, C++)",
        "Problem Solving",
        "Data Structures & Algorithms",
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


skills = input("What type of skills do you have? ")
if skills.isalpha:
    pass
else:
    print("Only alphabets are allowed!")
    