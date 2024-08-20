# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:14:56 2024

@author: Zach
"""

def work_environment():
    environment = {
        'city': {
            'name': 'Techville',
            'location': 'Northern California',
            'weather': 'mild with occasional rain in spring',
            'safety': 'high',
        },
        'office': {
            'attributes': {
                'layout': 'open space with designated quiet areas for focused work',
                'kitchen': 85,  # Rating out of 100 based on amenities and comfort
                'sub_location': (0, 1),  # Imaginary grid position within a tech park
                'technology': 100,  # State-of-the-art technology for development and collaboration
                'monthly_spend_on_amenities': '5000',  # Expenditure in USD for office amenities
                'decor': 'modern with inspirational tech quotes on walls',
                'recreational_areas': {
                    'indoor': 'table tennis and video game lounge',
                    'outdoor': 'rooftop garden and seating area'
                },
                'meeting_rooms': {
                    'number': 5,
                    'tech_equipped': True,
                    'booking_system': 'digital and user-friendly'
                },
                'security': {
                    'building_access': 'keycard and biometric',
                    'IT_security_measures': 'top-notch cybersecurity protocols'
                }
            }
        }
    }
    return environment
