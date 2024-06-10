#მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
#დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
#რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

mom_age = int(input("tell us your mom's age:   "))
dad_age = int(input("tell us your dad's age:   "))

if mom_age < dad_age:
    print("mom is younger than dad")

if mom_age > dad_age:
    print("mom is older than dad")