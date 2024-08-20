# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:45:09 2024

@author: Zach
"""

def value_priority(character):
    """
    Assigns priority scores to values for a character, which can be used to
    understand how characteristics are amplified or suppressed based on these values.

    Parameters:
    - character: A string representing the name of the character.

    Returns:
    A dictionary with values as keys and priority scores as values.
    """

    # Example character value priorities
    value_priorities = {
        'Jewel': {
            'recognition': 7,
            'compensation': 8,
            'comfort': 6,
            'opportunity': 9,
            'justice': 5,
            'fairness': 8
        },
        'Sammy': {
            'recognition': 5,
            'compensation': 7,
            'comfort': 4,
            'opportunity': 8,
            'justice': 9,
            'fairness': 9
        }
    }

    # Default value priorities if character is not found
    default_values = {
        'recognition': 5,
        'compensation': 5,
        'comfort': 5,
        'opportunity': 5,
        'justice': 5,
        'fairness': 5
    }

    return value_priorities.get(character, default_values)
