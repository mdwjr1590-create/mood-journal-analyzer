"""
journal_analyzer.py

This file will contain the main logic for the Mood Journal Analyzer project.
It will store journal entries, save/load files, and analyze mood patterns.
"""

import csv
import re
from collections import Counter
from datetime import datetime


class JournalEntry:
    """
    Represents one journal entry.

    Attributes:
        date (str): The date of the entry in YYYY-MM-DD format.
        text (str): The journal text for that date.
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
        Create an empty list to store journal entries.
        """
        self.entries = []

        # These word lists can be expanded later.
        self.positive_words = [
            "happy", "calm", "hopeful", "good", "excited",
            "great", "relaxed", "grateful", "joyful", "productive"
        ]
        self.negative_words = [
            "sad", "stressed", "stressful", "angry", "frustrated", "frustrating",
            "worried", "upset", "anxious", "tired", "overwhelmed"
        ]

    def _validate_date(self, date):
        """
        Check that a date is in YYYY-MM-DD format.

        Parameters:
            date (str): The date to validate.

        Raises:
            ValueError: If the date is not in the correct format.
        """
        datetime.strptime(date, "%Y-%m-%d")

    def _tokenize(self, text):
        """
        Convert text into a list of lowercase words.

        Parameters:
            text (str): Input text.

        Returns:
            list[str]: Cleaned words from the text.
        """
        return re.findall(r"[a-zA-Z']+", text.lower())

    def add_entry(self, date, text):
        """
        Add a new journal entry to the program.

        Parameters:
            date (str): Date in YYYY-MM-DD format.
            text (str): User's journal entry.
        """
        self._validate_date(date)

        cleaned_text = text.strip()
        if not cleaned_text:
            raise ValueError("Journal entry text cannot be empty.")

        entry = JournalEntry(date, cleaned_text)
        self.entries.append(entry)

    def save_entries(self, filename):
        """
        Save all journal entries to a CSV file.

        Parameters:
            filename (str): Name of file to save.
        """
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "entry"])
            for entry in self.entries:
                writer.writerow([entry.date, entry.text])

    def load_entries(self, filename):
        """
        Load journal entries from a CSV file.

        Parameters:
            filename (str): Name of file to read.

        Notes:
            Existing entries are cleared before loading the file so that
            repeated loads do not create duplicates.
        """
        loaded_entries = []

        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                raise ValueError("CSV file must include a header row.")

            required_columns = {"date", "entry"}
            if not required_columns.issubset(set(reader.fieldnames)):
                raise ValueError("CSV file must contain 'date' and 'entry' columns.")

            for row in reader:
                date = row["date"].strip()
                text = row["entry"].strip()
                self._validate_date(date)
                if text:
                    loaded_entries.append(JournalEntry(date, text))

        self.entries = loaded_entries

    def analyze_mood(self):
        """
        Analyze entries for mood-related words.

        Returns:
            dict: Summary information about positive and negative mood words.
        """
        positive_count = 0
        negative_count = 0

        for entry in self.entries:
            words = self._tokenize(entry.text)
            positive_count += sum(word in self.positive_words for word in words)
            negative_count += sum(word in self.negative_words for word in words)

        if positive_count > negative_count:
            summary = "mostly positive"
        elif negative_count > positive_count:
            summary = "mostly negative"
        else:
            summary = "neutral"

        return {
            "entry_count": len(self.entries),
            "positive_count": positive_count,
            "negative_count": negative_count,
            "overall_mood": summary,
        }

    def word_frequency_report(self, top_n=10):
        """
        Count the most common words across all entries.

        Parameters:
            top_n (int): Number of top words to return.

        Returns:
            list[tuple[str, int]]: Most common words and their counts.
        """
        if top_n <= 0:
            raise ValueError("top_n must be greater than 0.")

        all_words = []
        for entry in self.entries:
            all_words.extend(self._tokenize(entry.text))

        counts = Counter(all_words)
        return counts.most_common(top_n)

    def display_entries(self):
        """
        Display all journal entries in a readable format.
        """
        if not self.entries:
            print("No journal entries saved.")
            return

        print("\nSaved Journal Entries")
        print("-" * 22)
        for entry in self.entries:
            print(f"Date: {entry.date}")
            print(f"Entry: {entry.text}\n")
