sessions = [
    {"Videos", "Quiz", "Flashcards"},
    {"Videos", "Quiz"},
    {"Videos", "Notes"},
    {"Videos", "Quiz", "Notes"},
    {"Quiz", "Flashcards"},
    {"Notes", "Discussion"},
    {"Videos", "Discussion"},
    {"Quiz", "Notes"},
    {"Videos", "Quiz", "Flashcards"},
    {"Notes", "Discussion"},
    {"Videos", "Quiz"},
    {"Quiz", "Flashcards"},
]


def metrics(a, b):
    total = len(sessions)
    count_a = sum(a in s for s in sessions)
    count_b = sum(b in s for s in sessions)
    count_ab = sum(a in s and b in s for s in sessions)

    support = count_ab / total
    confidence = count_ab / count_a
    lift = confidence / (count_b / total)
    return support, confidence, lift


if __name__ == "__main__":
    s, c, l = metrics("Quiz", "Flashcards")
    print(f"Quiz -> Flashcards: support={s:.3f}, confidence={c:.2f}, lift={l:.2f}")