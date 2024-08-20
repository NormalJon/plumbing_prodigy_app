# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:12:22 2024

@author: Zach
"""

def group_dynamics(person_a, person_b):
    # Example traits for simplicity
    # Traits: Creativity, Pragmatism, Outgoingness, Focus
    personalities = {
        'Jewel': {'Creativity': 8, 'Pragmatism': 5, 'Outgoingness': 7, 'Focus': 6},
        'Sammy': {'Creativity': 4, 'Pragmatism': 8, 'Outgoingness': 3, 'Focus': 7}
    }
    
    # Determine the interaction style based on traits
    interaction_style = ""
    
    if personalities[person_a]['Outgoingness'] - personalities[person_b]['Outgoingness'] > 2:
        interaction_style += f"{person_a} moderates their outgoingness around {person_b}. "
    elif personalities[person_b]['Outgoingness'] - personalities[person_a]['Outgoingness'] > 2:
        interaction_style += f"{person_a} feels more encouraged to be outgoing around {person_b}. "
    
    if abs(personalities[person_a]['Creativity'] - personalities[person_b]['Pragmatism']) > 3:
        interaction_style += f"{person_a} brings more creative ideas, while {person_b} focuses on practical implications. "
    elif abs(personalities[person_b]['Creativity'] - personalities[person_a]['Pragmatism']) > 3:
        interaction_style += f"{person_b} brings more creative ideas, while {person_a} focuses on practical implications. "
    
    if interaction_style == "":
        interaction_style = f"{person_a} and {person_b} have a balanced working relationship, with no significant adjustments in their personalities."
    
    return interaction_style

# Example usage
print(group_dynamics('Jewel', 'Sammy'))
