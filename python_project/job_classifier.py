from difflib import get_close_matches

def job_classifier():
    job_dict = {
        "technology": ["Software Developer", "Cybersecurity Analyst", "Data Scientist", "AI Engineer"],
        "healthcare": ["Doctor", "Nurse", "Medical Researcher", "Pharmacist"],
        "engineering": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Aerospace Engineer"],
        "education": ["Teacher", "Professor", "Educational Consultant", "Curriculum Developer"],
        "business": ["Marketing Manager", "Financial Analyst", "Entrepreneur", "HR Manager"],
        "arts": ["Graphic Designer", "Musician", "Actor", "Writer"],
        "science": ["Physicist", "Chemist", "Biologist", "Astronomer"],
        "law": ["Lawyer", "Paralegal", "Judge", "Legal Consultant"],
        "sports": ["Athlete", "Coach", "Sports Analyst", "Referee"]
    }
    
    work_styles = {
        "creative": ["Graphic Designer", "Musician", "Writer", "Actor"],
        "analytical": ["Software Developer", "Data Scientist", "Physicist", "Financial Analyst"],
        "hands-on": ["Engineer", "Doctor", "Athlete", "Chef"]
    }
    
    user_interest = input("What job field are you interested in? ").strip().lower()
    user_work_style = input("Do you prefer a creative, analytical, or hands-on job? ").strip().lower()
    
    closest_match = get_close_matches(user_interest, job_dict.keys(), n=1)
    if closest_match:
        field = closest_match[0]
        careers = job_dict[field]
        
        if user_work_style in work_styles:
            filtered_careers = [job for job in careers if job in work_styles[user_work_style]]
            if filtered_careers:
                return f"Based on your interest in {field} and your preference for {user_work_style} work, you might enjoy: {', '.join(filtered_careers)}."
        
        return f"You might enjoy a career in {field}: {', '.join(careers)}."
    
    return "Sorry, I couldn't classify your interest. Try using broader job categories!"

# Run the classifier
if __name__ == "__main__":
    print(job_classifier())
