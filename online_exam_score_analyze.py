scores=[89,98,84,75,92,78]
total_score=sum(scores)
print("Total score is:",total_score)
avg=total_score/len(scores)
print("Average score is:",avg)
count=0
for i in range(len(scores)):
    if scores[i]>avg:
        count+=1
print("Count of scores above average are:",count)
