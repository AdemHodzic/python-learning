from contextManager import Manager

#Short script for inputing data from fiel to database

config = {'host': '127.0.0.1',
          'user': 'root',
          'password': 'password',
          'database': 'Quiz', }


questions = list()
answers = list()

with open('answers.txt') as file:
    for line in file:
        listAnswers = line.split('(sep)')
        answers.append(listAnswers)

with open('questions.txt') as file:
    for line in file:
        questions.append(line)

number = len(questions)
q_index = 0

with Manager(config) as cursor:
    _SQL = "INSERT INTO questions(text,correct,wrong1,wrong2,wrong3) VALUES(%s, %s, %s, %s, %s)"
    for i in range(0,number):
        text = questions[i]
        correct = answers[i][0]
        q_index+=1
        wrong1 = answers[i][1]
        q_index+=1
        wrong2 = answers[i][2]
        q_index+=1
        wrong3 = answers[i][3]
        q_index+=1
        cursor.execute(_SQL,(text,correct,wrong1,wrong2,wrong3))
        print("Question succefully added")