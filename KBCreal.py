print("Welcome to KBC! Lets start the game")

questions = [[
    "In what language is the phrase ‘Hakuna Matata’?", "1. Dutch",
    "2. Swahili", "3. Yoruba", "4. Nigerian", 2
],
             [
                 "What is the capital city of France?", "1. Paris",
                 "2. New Castle", "3. Cannes", "4. Marselleis", 1
             ],
             [
                 "In what language is the phrase ‘Hakuna Matata’?", "1. Dutch",
                 "2. Swahili", "3. Yoruba", "4. Nigerian", 2
             ],
             [
                 "In what language is the phrase ‘Hakuna Matata’?", "1. Dutch",
                 "2. Swahili", "3. Yoruba", "4. Nigerian", 2
             ],
             [
                 "In what language is the phrase ‘Hakuna Matata’?", "1. Dutch",
                 "2. Swahili", "3. Yoruba", "4. Nigerian", 2
             ],
             [
                 "In what language is the phrase ‘Hakuna Matata’?", "1. Dutch",
                 "2. Swahili", "3. Yoruba", "4. Nigerian", 2
             ]]
levels = [5000, 10000, 40000, 80000, 160000, 320000]
money = 0
i = 0
for i in range(0, len(questions)):
  print(f"Question for Rs.{levels[i]}")
  print(f"{questions[i][0]}")
  print(f"{questions[i][1]}     {questions[i][2]}")
  print(f"{questions[i][3]}     {questions[i][4]}")
  rep = int(input("enter an answer 1-4"))
  if rep == questions[i][5]:
    print(f"Correct answer!!! you have won Rs. {levels[i]}")
    money = money + levels[i]
  else:
    print("Incorrect answer!")
    break

print(f"you have wonn Rs.{money}")