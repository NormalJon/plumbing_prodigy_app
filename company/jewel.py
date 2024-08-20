# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:34:07 2024

@author: Zach
"""

def jewel(): 
    Background = 'Jewel is a mid-level developer with a knack for front-end design and a hobbyist interest in UI/UX design. 
    tenure = 'They have been with the company for three years.'
    personality_traits = 'Creative, outgoing, detail-oriented, and always up for a challenge.'
    interests = "graphic design, gaming, and volunteering at local coding bootcamps."
    skills = "Proficient in React, CSS animations, and has a good eye for design."
    quirks = "Known for their lively stand-up updates and wearing graphic tees related to coding jokes."

def jewel_profile():
    data = {
        "family": {
            "father": {
                "job": "engineer",
                "status": "alive",
                "hobbies": "hiking",
                "relationship_with_Jewel": "close, inspired Jewel's interest in tech"
            },
            "mother": {
                "job": "architect",
                "status": "alive",
                "hobbies": "painting, gardening",
                "relationship_with_Jewel": "supportive, encouraged Jewel's creative side"
            },
            "siblings": {
                "number": 1,
                "sister": {
                    "age": 22,
                    "interests": "environmental science, activism",
                    "relationship_with_Jewel": "strong, often collaborate on tech-for-good projects"
                }
            }
        },
        "education": {
            "bachelors_degree": {
                "field": "Computer Science",
                "university": "University of Technology",
                "extra_curriculars": ["design club president", "volunteer tutor for programming"],
                "achievements": ["graduated summa cum laude", "best capstone project in UI/UX"]
            }
        },
        "career_path": {
            "first_job": {
                "role": "Junior Front-end Developer",
                "company": "Start-up Tech Innovations",
                "key_learnings": "Gained proficiency in React, developed a passion for user-centric design"
            },
            "current_role": {
                "role": "Mid-Level Front-end Developer",
                "company": "Our Company",
                "responsibilities": ["Lead the redesign of the customer analytics dashboard", "Mentor junior developers"],
                "aspirations": "Become a lead designer and developer for user experience projects"
            }
        },
        "personal_growth": {
            "hobbies": ["digital painting", "attending tech meetups"],
            "recent_interests": ["augmented reality for enhancing user interfaces", "sustainability in tech"],
            "life_goals": ["contribute to an open-source project that makes a significant impact", "design an app that aids in environmental conservation"]
        },
        "personality_traits": {
            "strengths": ["creative problem solving", "attention to detail", "effective communicator"],
            "areas_for_growth": ["patience with complex backend issues", "delegation"]
        }
    }
    return data

             
             
          
        
        
        
        }
    
def jewel_values():
    values = {
        'creativity': 86,
        'empathy': 75,
        'intelligence': 60,
        'vocabulary': 90,
        'analytical skill': 85,
        'teamwork': 80,
        'problem-solving': 88,
        'adaptability': 82,
        'leadership': 70,
        'attention to detail': 92
    }
    return values

    
            
            }
    
def jewel_environment():
    """Defines the environment the character is in, rated from a score of 0-100. Ratings indicate how comfortable a 
    character feels in regard to a specific environmental factor. Scores are generated based on past background."""
    
    environment = {
        'financial': 80,  # Jewel has a stable job and manages her finances well.
        'living_space': 90,  # She lives in a comfortable apartment that reflects her personal style.
        'city': {
            'location': 'Techville, Northern California',  # A vibrant tech hub.
            'weather': 75,  # Jewel enjoys mild weather but is not a fan of the occasional rain.
            'access_to_hobbies': 95,  # The city offers ample opportunities for her interests in design and tech meetups.
        },
        'friendships': 85,  # Jewel has a strong network of friends both within and outside of work.
        'work_commute': 70,  # The commute is manageable but can be tiring during peak traffic.
        'workplace_comfort': 88,  # The office is modern and well-equipped, fostering a creative and productive environment.
        'access_to_nature': 80,  # She appreciates the city's parks and outdoor spaces, though she wishes for more.
        'cultural_fit': 92,  # Jewel feels aligned with the city's innovative and forward-thinking culture.
        'community_involvement': 75,  # She participates in local events and workshops, though her busy schedule can limit involvement.
    }
    
    return environment

    
def calculate_environment_score(ideal, actual, weight):
    """Calculates the adjusted score based on the ideal vs. actual environment."""
    score = max(0, ideal - (ideal - actual) * weight)
    return score

def jewel_environment_hoboville_adjusted():
    jewel_ideal = {
        'financial': 80,
        'living_space': 90,
        'access_to_hobbies': 95,
        'friendships': 85,
        'work_commute': 70,
        'workplace_comfort': 88,
        'access_to_nature': 80,
        'cultural_fit': 92,
        'community_involvement': 75,
    }

    hoboville_traits = {
        'financial_stability': 60,
        'living_space_quality': 50,
        'hobbies_access': 40,
        'social_opportunities': 50,
        'commute_safety': 40,
        'work_environment': 60,
        'nature_access': 30,
        'cultural_alignment': 40,
        'community_engagement': 30,
    }

    # Weightings based on Jewel's priorities (1 = high importance, 0.5 = medium, 0.25 = low)
    weightings = {
        'financial': 1,
        'living_space': 1,
        'access_to_hobbies': 0.75,
        'friendships': 0.75,
        'work_commute': 1,
        'workplace_comfort': 0.75,
        'access_to_nature': 0.5,
        'cultural_fit': 0.75,
        'community_involvement': 0.5,
    }

    adjusted_environment = {}
    for key, value in jewel_ideal.items():
        adjusted_score = calculate_environment_score(value, hoboville_traits[key + '_quality' if key == 'living_space' else key], weightings[key])
        adjusted_environment[key] = adjusted_score

    return adjusted_environment

       value_priorities = {
           'Jewel': {
               'recognition': 7,
               'compensation': 8,
               'comfort': 6,
               'opportunity': 9,
               'justice': 5,
               'fairness': 8  
    

print(group_dynamics(jewel,sammy)):  

def group_dynamics():
    
    
def interaction_outcome():  
    for outcome in interaction:
        if ((character_1[communication] + character_2[communication])//2) >= 50:
            return good_result 
        else: 
            return dissagreement 
    
    
    
    
    
    
    
    