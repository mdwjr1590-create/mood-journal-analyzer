"""
main.py

This file will run the Mood Journal Analyzer program.
It will display a menu and let the user choose what action to take.
"""

from journal_analyzer import MoodJournalAnalyzer


def show_menu():
    """
    Display the main menu options to the user.
    """
    print("\nMood Journal Analyzer")
    print("1. Add entry")
    print("2. Load entries from file")
    print("3. Save entries to file")
    print("4. Display entries")
    print("5. Analyze mood")
    print("6. Show word frequency report")
    print("7. Exit")


def main():
    """
    Main function for running the program.

    Planned flow:
        1. Create MoodJournalAnalyzer object
        2. Show menu
        3. Ask user for a choice
        4. Call the matching method
        5. Repeat until user exits
    """
    analyzer = MoodJournalAnalyzer()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # ask for date and entry text
            # call analyzer.add_entry()
            pass

        elif choice == "2":
            # ask for filename
            # call analyzer.load_entries()
            pass

        elif choice == "3":
            # ask for filename
            # call analyzer.save_entries()
            pass

        elif choice == "4":
            # call analyzer.display_entries()
            pass

        elif choice == "5":
            # call analyzer.analyze_mood()
            # print results
            pass

        elif choice == "6":
            # call analyzer.word_frequency_report()
            # print most common words
            pass

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
