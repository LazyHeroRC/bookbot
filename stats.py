def count_words(text):
    """Return the number of words in the given text."""
    # split on whitespace to get all words
    return len(text.split())

def count_characters(text):
    """Return a dict mapping each lowercase character to its frequency."""
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_char_counts(char_counts):
    """
    Turn a dict of {char: count} into a list of {"char": char, "num": count} dicts,
    sorted by count descending, and only for alphabetical characters.
    """
    # Build the list, filtering to alphabetic chars only
    items = [
        {"char": ch, "num": count}
        for ch, count in char_counts.items()
        if ch.isalpha()
    ]
    # Sort in place by the "num" key, descending
    items.sort(key=lambda d: d["num"], reverse=True)
    return items
