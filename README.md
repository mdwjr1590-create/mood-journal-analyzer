# Mood Journal Analyzer

## Introduction
Mood Journal Analyzer is a Python program that allows users to save short daily journal entries and analyze patterns in their writing over time. The program is designed to help users reflect on emotional trends by identifying positive, negative, and neutral mood-related words in their entries.

This project combines file handling, functions, classes, and simple data analysis. It is useful for users who want to keep a daily journal while also getting a basic summary of the emotional tone of their reflections.

## Why someone would use this program
A user might use this program to:
- keep track of journal entries over time
- notice whether their writing is becoming more positive or negative
- identify repeated themes or words in their reflections
- organize entries by date for easier review

## Main Features
- add a journal entry with a date
- save entries to a CSV file
- load entries from a CSV file
- analyze mood-related words in entries
- generate a word frequency report
- display all saved entries in a readable format

## Files in the Project
- `main.py`  
  Runs the program and handles user interaction.

- `journal_analyzer.py`  
  Contains the main classes and functions for storing journal entries and analyzing them.

- `test_journal_analyzer.py`  
  Contains unit tests for the core methods in the project.

- `sample_entries.csv`  
  Example input file that shows the required data format.

- `project_report_outline.md`  
  Outline for the final report.

## Data Format
The program reads and writes CSV files with the following columns:

`date,entry`

### Field descriptions
- `date`: must be written in `YYYY-MM-DD` format
- `entry`: a journal reflection written as a string

### Example
```csv
date,entry
2026-04-01,I felt happy and relaxed after finishing my homework.
2026-04-02,Today was stressful and frustrating but I got through it.
2026-04-03,I felt calm and hopeful about the week ahead.
