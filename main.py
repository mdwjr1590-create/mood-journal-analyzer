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
    """
    analyzer = MoodJournalAnalyzer()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                date = input("Enter the date (YYYY-MM-DD): ").strip()
                text = input("Enter your journal entry: ").strip()
                analyzer.add_entry(date, text)
                print("Entry added successfully.")

            elif choice == "2":
                filename = input("Enter the filename to load: ").strip()
                analyzer.load_entries(filename)
                print("Entries loaded successfully.")

            elif choice == "3":
                filename = input("Enter the filename to save to: ").strip()
                analyzer.save_entries(filename)
                print("Entries saved successfully.")

            elif choice == "4":
                analyzer.display_entries()

            elif choice == "5":
                results = analyzer.analyze_mood()
                print("\nMood Analysis Report")
                print("-" * 20)
                print(f"Number of entries: {results['entry_count']}")
                print(f"Positive words: {results['positive_count']}")
                print(f"Negative words: {results['negative_count']}")
                print(f"Overall mood: {results['overall_mood']}")

            elif choice == "6":
                report = analyzer.word_frequency_report()
                print("\nMost Common Words")
                print("-" * 18)
                for word, count in report:
                    print(f"{word}: {count}")

            elif choice == "7":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except FileNotFoundError:
            print("That file could not be found.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
