def positive_feedback(ratings):
    if not ratings:
        return 0
    positive = sum(1 for r in ratings if r >= 4)
    return (positive / len(ratings)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
percentage = positive_feedback(ratings)
print(f"Positive Feedback: {percentage:.1f}%")