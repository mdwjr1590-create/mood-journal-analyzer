"""
test_journal_analyzer.py

This file outlines how the Mood Journal Analyzer project will be tested.
Some of these may later become full unit tests.
"""

import os
import tempfile
import unittest

from journal_analyzer import MoodJournalAnalyzer


class TestMoodJournalAnalyzer(unittest.TestCase):
    """
    Unit tests for the MoodJournalAnalyzer class.
    """

    def setUp(self):
        """
        Create a MoodJournalAnalyzer object before each test.
        Add a few sample entries for testing.
        """
        self.analyzer = MoodJournalAnalyzer()
        self.analyzer.add_entry("2026-04-01", "I felt happy and calm today.")
        self.analyzer.add_entry(
            "2026-04-02", "Today was stressful and frustrating."
        )
        self.analyzer.add_entry(
            "2026-04-03", "I felt hopeful after finishing my work."
        )

    def test_add_entry(self):
        """
        Test whether a new entry is successfully added to the list.
        """
        analyzer = MoodJournalAnalyzer()
        analyzer.add_entry("2026-04-10", "I felt excited about my project.")

        self.assertEqual(len(analyzer.entries), 1)
        self.assertEqual(analyzer.entries[0].date, "2026-04-10")
        self.assertEqual(analyzer.entries[0].text, "I felt excited about my project.")

    def test_save_and_load_entries(self):
        """
        Test whether entries can be saved to a CSV file
        and later loaded back correctly.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_name = temp_file.name

        try:
            self.analyzer.save_entries(temp_name)

            new_analyzer = MoodJournalAnalyzer()
            new_analyzer.load_entries(temp_name)

            self.assertEqual(len(new_analyzer.entries), 3)
            self.assertEqual(new_analyzer.entries[0].date, "2026-04-01")
            self.assertIn("happy", new_analyzer.entries[0].text.lower())
        finally:
            if os.path.exists(temp_name):
                os.remove(temp_name)

    def test_analyze_mood(self):
        """
        Test whether mood-related words are counted correctly.
        """
        results = self.analyzer.analyze_mood()

        self.assertEqual(results["positive_count"], 3)
        self.assertEqual(results["negative_count"], 2)
        self.assertEqual(results["overall_mood"], "mostly positive")

    def test_word_frequency_report(self):
        """
        Test whether the most common words are reported correctly.
        """
        report = self.analyzer.word_frequency_report(top_n=5)
        report_dict = dict(report)

        self.assertEqual(report_dict["felt"], 2)
        self.assertEqual(report_dict["today"], 2)
        self.assertIn("happy", report_dict)


if __name__ == "__main__":
    unittest.main()
