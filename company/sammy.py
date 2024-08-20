# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:51:16 2024

@author: Zach
"""

def sammy_profile():
    data = {
        "family": {
            "mother": {
                "job": "school teacher",
                "status": "alive",
                "hobbies": ["reading", "gardening"]
            },
            "sibling": {
                "relation": "sister",
                "job": "graphic designer",
                "status": "alive",
                "hobbies": ["photography", "traveling"]
            }
        },
        "education": {
            "bachelors_degree": {
                "field": "Computer Science",
                "university": "State University",
                "year": 2015
            },
            "additional_training": {
                "course": "Full Stack Web Development",
                "institution": "Online Bootcamp",
                "year": 2017
            }
        },
        "interests": ["drones", "woodworking", "exploring new APIs"],
        "previous_industry_experience": {
            "industry": "Hospitality",
            "role": "Operations Manager",
            "years": 5
        },
        "transition_to_tech": {
            "reason": "Passion for technology and problem-solving",
            "year": 2017
        }
    }
    return data
