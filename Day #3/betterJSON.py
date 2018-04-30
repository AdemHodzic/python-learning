import json
import re

#Files needed
write_questions = open('questions.txt', 'w')
write_answers = open('answers.txt', 'w')
json_file = open('quiz.json', 'r')

#json string
json_string = json_file.read()

#we've taken oru json string and turned it in dictionary
data = json.loads(json_string)

#string we need to escape when working with special characters
quatation = r'&quot;'
apostrophe = r'&#039;'
lower = r'&lt;'
greater = r'&gt;'

for res in data['results']:
    #Getting questions and an swers from JSON
    question = res['question']
    corrrect_answer = res['correct_answer']
    wrong_answers = res['incorrect_answers']

    #Escaping quatations and apostrophe signs in our strings
    question = re.sub(apostrophe, '\'', question)
    question = re.sub(quatation, '\"', question)
    question = re.sub(lower, '<', question)
    question = re.sub(greater, '>', question)
    
    corrrect_answer = re.sub(apostrophe, '\'', corrrect_answer)
    corrrect_answer = re.sub(quatation, '\"', corrrect_answer)
    corrrect_answer = re.sub(lower, '<', corrrect_answer)
    corrrect_answer = re.sub(greater, '>', corrrect_answer)
    
    #Writing strings to apropriate files    
    write_questions.write(question)
    write_questions.write('\n')
    
    #Addin answers to list that we will use later
    answer_list = [corrrect_answer]
    #Initializing final answer
    final_answer = ''
    
    for ans in wrong_answers:
        ans = re.sub(apostrophe, '\'', ans)
        ans = re.sub(quatation, '\"', ans)
        ans = re.sub(lower, '<', ans)
        ans = re.sub(greater, '>', ans)
        answer_list.append(ans)
    
    final_answer = '(sep)'.join(answer_list)
    write_answers.write(final_answer)
    write_answers.write('\n')

write_questions.close()
write_answers.close()
json_file.close()



