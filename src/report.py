from matcher import MatchResult

def print_report(result: MatchResult):
    """
    Prints a clean, readable summary of the resume-job match.
    """

    print("\n" + "=" * 50)
    print(f"Match Score: {result.score:.1f}%")
    print("=" * 50)

    print("\nMatched Skills:")
    if result.matched:
        print(", ".join(sorted(result.matched)))
    else:
        print("None")

    print("\nMissing Skills:")
    if result.missing:
        print(", ".join(sorted(result.missing)))
    else:
        print("None")

    print("=" * 50 + "\n")
