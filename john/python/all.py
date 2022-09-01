print("all projects")
print("============")

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age


def chapter_57():
    print("in chapter 57")

    print("")
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")
    print("")


    pid4343 = Patient("Taleb", "Sue", 61)
    pid4344 = Patient("Anand", "Punya", 29)
    pid4345 = Patient("Lin", "Lilly", 48)
    pid1298 = Patient("Nilsson", "Rhonda", 33)

    print(f"first patient {pid4343.first_name} {pid4343.last_name} aged {pid4343.age}")







def chapter_58():
    print("in chapter 58")





user_input = ""
while user_input != "q":
  user_input = input("Enter a number, or q to quit:")
  print("chapter {user_input}:")

  if user_input != "q":
    if user_input == "57":
        chapter_57()

    if user_input == "58":
        chapter_58()
