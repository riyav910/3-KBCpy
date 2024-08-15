class Question():

  def __init__(self, question, correct_answer_option, o1, o2, o3, o4):
    self.name = question
    self.o1 = o1
    self.o2 = o2
    self.o3 = o3
    self.o4 = o4
    self.answer = correct_answer_option


amount_group = [
    '10000', '20000', '40000', '80000', '160000', '320000', '640000',
    '1250000', '2500000', '5000000', '10000000', '70000000'
]
amount_stage = [
    "0", '80000', '320000', '1250000', '5000000', '10000000', '70000000'
]
question1 = Question("What is the capital of France?", "4", "London", "Berlin",
                     "Moscow", "Paris")
question2 = Question("What is the capital of Germany?", "3", "Paris", "London",
                     "Berlin", "Moscow")
question3 = Question("What is the capital of Italy?", "1", "Rome", "London",
                     "Berlin", "Moscow")
question4 = Question("What is the capital of Spain?", "4", "Rome", "Paris",
                     "London", "Madrid")
question5 = Question("What is the capital of Ukraine?", "2", "Rome", "Kiev",
                     "Paris", "Minsk")
question6 = Question("What is the capital of Greece?", "3", "Rome", "Anthens",
                     "Kiev", "Paris")
question7 = Question("What is the capital of Norway?", "1", "Olso", "Rome",
                     "Riga", "Kiev")
question8 = Question("What is the capital of Fianland?", "4", "Rome", "Kiev",
                     "Dublin", "Helsinki")
question9 = Question("What is the capital of Latvia?", "2", "Rome", "Riga",
                     "Kiev", "Libson")
question10 = Question("What is the capital of Switzerland?", "1", "Bern",
                      "Rome", "Pristina", "Minsk")
question11 = Question("What is the capital of Cuba?", "3", "Havana", "Ottawa",
                      "Kiev", "San Jose")
question12 = Question("What is the capital of Greenland?", "4", "Stanley",
                      "Kiev", "Road Town", "Nuuk")
question13 = Question("What is the capital of Bermuda?", "2", "Jakarta",
                      "Hamilton", "Marigot", "Brades")
questionlist = [
    question1, question2, question3, question4, question5, question6,
    question7, question8, question9, question10, question11, question12,
    question13
]
life = True
# amount_won = 0
if life == True:
  for i in range(13):
    print(questionlist[i].name)
    print("1: " + questionlist[i].o1)
    print("2: " + questionlist[i].o2)
    print("3: " + questionlist[i].o3)
    print("4: " + questionlist[i].o4)
    # lst=['1','2','3','4']
    answer = input("Your Answer Option : ")
    if answer == questionlist[i].answer:
      print("Correct answer!")
      amount_won = int(amount_group[i])
      print("You have won Rs." + str(amount_won) + '.00\n')
    else:
      print("Incorrect answer!")
      life = False
      break

for j in range(len(amount_stage)):
  # for j in amount_stage:
  if amount_won < int(amount_stage[j]):
    net_amount = amount_stage[int(j) - 1]
    print("You won Rs." + str(net_amount) + '.00\n')
    break
  # else:
  # print("Sorry! Your winnig price is Rs.0.00")
  # break
