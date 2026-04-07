"""
test_journal_analyzer.py

This file outlines how the Mood Journal Analyzer project will be tested.
Some of these may later become full unit tests.
"""

import unittest
from journal_analyzer import MoodJournalAnalyzer


class TestMoodJournalAnalyzer(unittest.TestCase):

    def setUp(self):
        """
        Create a MoodJournalAnalyzer object before each test.
        Add a few sample entries for testing.
        """
        self.analyzer = MoodJournalAnalyzer()

        # planned sample entries
        # self.analyzer.add_entry("2026-04-01", "I felt happy today.")
        # self.analyzer.add_entry("2026-04-02", "I was stressed about school.")

    def test_add_entry(self):
        """
        Test whether a new entry is successfully added to the list.
        """
        pass

    def test_save_and_load_entries(self):
        """
        Test whether entries can be saved to a CSV file
        and later loaded back correctly.
        """
        pass

    def test_analyze_mood(self):
        """
        Test whether mood-related words are counted correctly.
        """
        pass

    def test_word_frequency_report(self):
        """
        Test whether the most common words are reported correctly.
        """
        pass


if __name__ == "__main__":
    unittest.main()
