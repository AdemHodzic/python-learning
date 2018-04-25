#Importing json module for working with JSON and re module for working with regEx
import json
import re

#JSON file to be read and files for writing
file = open('quiz.json', 'r')
questions = open('quetions.txt', 'w')
answers = open('answers.txt', 'w')

#string read from quiz.json
json_str = file.read()

#string parsed in json
data = json.loads(json_str)

#some regex matches we need to change in our JSON strings
quatation = r'&quot;'
apostrophe = r'&#039;'
lower = r'&lt;'
greater = r'&gt;'

#iterating through JSON object and escaping quatations and apostrophes
for res in data['results']:
    #Getting questions and an swers from JSON
    question = res['question']
    corrrect_answer = res['correct_answer']
    wrong_answers = res['incorrect_answers']
    
    #Escaping quatations and apostrophe signs in our strings
    question = re.sub(apostrophe, '\'', question)
    question = re.sub(quatation, '\\"', question)
    
    corrrect_answer = re.sub(apostrophe, '\'', corrrect_answer)
    corrrect_answer = re.sub(quatation, '\\"', corrrect_answer)
    
    #Writing strings to apropriate files    
    questions.write(question)
    questions.write('\n')
    answers.write(corrrect_answer)
    answers.write('\n')
    
    #Since wrong_answers is list, we need to iterate over it and then write it to file
    for ans in wrong_answers:
        ans = re.sub(apostrophe, '\'', ans)
        ans = re.sub(quatation, '\\"', ans)
        answers.write(ans)
        answers.write('\n')

#Finally we are closing file streams we used
file.close()
questions.close()
answers.close()