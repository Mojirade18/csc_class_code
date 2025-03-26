def job_classifier(job_interest):
    job_dict = {
        "technology": ["Software Developer", "Cybersecurity Analyst", "Data Scientist", "AI Engineer"],
        "healthcare": ["Doctor", "Nurse", "Medical Researcher", "Pharmacist"],
        "engineering": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Aerospace Engineer"],
        "education": ["Teacher", "Professor", "Educational Consultant", "Curriculum Developer"],
        "business": ["Marketing Manager", "Financial Analyst", "Entrepreneur", "HR Manager"],
        "arts": ["Graphic Designer", "Musician", "Actor", "Writer"]
    }
    
    job_interest = job_interest.lower()
    
    for field, careers in job_dict.items():
        if field in job_interest:
            return f"You might enjoy a career as a {careers[0]} or {careers[1]}!"
    
    return "Sorry, I couldn't classify your interest. Try a different keyword!"

# Example Usage
if __name__ == "__main__":
    user_input = input("What job field are you interested in? ")
    print(job_classifier(user_input))
