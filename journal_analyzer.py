"""
journal_analyzer.py

This file will contain the main logic for the Mood Journal Analyzer project.
It will store journal entries, save/load files, and analyze mood patterns.
"""

import csv
from collections import Counter


class JournalEntry:
    """
    Represents one journal entry.

    Attributes:
        date (str): The date of the entry in YYYY-MM-DD format
        text (str): The journal text for that date
    """

    def __init__(self, date, text):
        self.date = date
        self.text = text


class MoodJournalAnalyzer:
    """
    Main class for managing and analyzing journal entries.
    """

    def __init__(self):
        """
        Will create an empty list to store journal entries.

        Planned attributes:
            self.entries
            self.positive_words
            self.negative_words
        """
        self.entries = []

        # These word lists may be expanded later
        self.positive_words = ["happy", "calm", "hopeful", "good", "excited"]
        self.negative_words = ["sad", "stressed", "angry", "frustrated", "worried"]

    def add_entry(self, date, text):
        """
        Add a new journal entry to the program.

        Parameters:
            date (str): date in YYYY-MM-DD format
            text (str): user's journal entry

        Steps:
            1. Create a JournalEntry object
            2. Add it to self.entries
        """
        pass

    def save_entries(self, filename):
        """
        Save all journal entries to a CSV file.

        Parameters:
            filename (str): name of file to save

        Planned behavior:
            - open file in write mode
            - write header row
            - write each entry's date and text
        """
        pass

    def load_entries(self, filename):
        """
        Load journal entries from a CSV file.

        Parameters:
            filename (str): name of file to read

        Planned behavior:
            - open file in read mode
            - read each row
            - create JournalEntry objects
            - add them to self.entries
        """
        pass

    def analyze_mood(self):
        """
        Analyze entries for mood-related words.

        Planned behavior:
            - look through all saved entries
            - count positive words
            - count negative words
            - decide whether the overall mood is mostly positive,
              mostly negative, or neutral

        Planned return:
            a dictionary with counts and summary
        """
        pass

    def word_frequency_report(self, top_n=10):
        """
        Count the most common words across all entries.

        Parameters:
            top_n (int): number of top words to return

        Planned behavior:
            - split entry text into words
            - count repeated words
            - return most common words

        Planned return:
            list of tuples like [('happy', 3), ('school', 2)]
        """
        pass

    def display_entries(self):
        """
        Display all journal entries in a readable format.

        Planned behavior:
            - loop through self.entries
            - print date and entry text
        """
        pass
