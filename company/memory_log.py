# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:57:49 2024

@author: Zach
"""

class MemoryLog:
    def __init__(self):
        self.logs = []

    def add_entry(self, date, event_type, details, participants, emotions=None):
        self.logs.append({
            'date': date,
            'event_type': event_type,
            'details': details,
            'participants': participants,
            'emotions': emotions if emotions else {}
        })

    def get_recent_entries(self, participant=None, event_type=None, limit=5):
        filtered_logs = [log for log in self.logs if (participant is None or participant in log['participants']) and (event_type is None or event_type == log['event_type'])]
        return filtered_logs[-limit:]

    def get_most_recent_interaction(self, participants):
        # Filter logs for entries including all specified participants
        interaction_logs = [log for log in self.logs if all(participant in log['participants'] for participant in participants)]
        # Sort by date in descending order to get the most recent first
        interaction_logs.sort(key=lambda x: x['date'], reverse=True)
        # Return the most recent interaction, if any
        return interaction_logs[0] if interaction_logs else None

# Example instantiation and usage
memory_log = MemoryLog()

# Adding example entries
memory_log.add_entry('2024-03-10', 'Stand-up Meeting', 'Team discussed current project statuses.', ['Jewel', 'Sammy', 'Alex'], {'Jewel': 'curious', 'Sammy': 'motivated'})
memory_log.add_entry('2024-03-11', 'Conversation', 'Jewel and Sammy discussed UI design trends.', ['Jewel', 'Sammy'], {'Jewel': 'inspired', 'Sammy': 'interested'})
memory_log.add_entry('2024-03-12', 'Conversation', 'Jewel and Sammy followed up on the UI discussion.', ['Jewel', 'Sammy'], {'Jewel': 'satisfied', 'Sammy': 'confident'})

# Retrieving the most recent interaction between Jewel and Sammy
most_recent_interaction = memory_log.get_most_recent_interaction(['Jewel', 'Sammy'])
print(most_recent_interaction)
