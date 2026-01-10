feedback={"Positive": 45, "Neutral": 18, "Negative": 7}
total_feedback=sum(feedback.values())
print(total_feedback)
#type_feedback=max(feedback.values())
#print(type_feedback)
highest_feedback = max(feedback, key=feedback.get)
print(highest_feedback)
