#실습1
#1,2
scores = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
#3
scores["David"] = 80
#4
scores["Alice"] = 88
#5
scores.pop("Bob")
#6
for i in scores:
    print(i, ':', scores[i])
    #'Alice: 88'
    #'Charlie: 95'
    #'David: 80' 출력