from Question import *

question_prompts = [
    '(1) What is the radius of Earth?(m/s) \n (a) 6000 \n (b) 4000 \n (c) 6500',

    '(2) What is the haviest Object in Universe? \n (a) Wood \n (b) Sun \n (c) Black Hole',

    '(3) What is the rarest material in Earth? \n (a)Gold \n (b) Earth\n (c) Diamond',

    '(4) What is the name of Human? \n',

    '(5) What color is sky? \n (a) Blue \n (b) Clear \n (c) Black',

    '(6) What is the Einstines Formula? \n (a) E+Mc \n (b) e=mc^2 \n (c) e=mx',

    '(7) What is not an error? \n (a) a = n \n (b) printf(a) \n (c) print(a)',

    '(8) What is the radius of Jupiter? \n (a) 16000 \n (b) 40000 \n (c) 16500',

    '(9) What is the radius of Jupiter? \n (a) 16000 \n (b) 40000 \n (c) 16500',

    '(10) What is the radius of Jupiter? \n (a) 16000 \n (b) 40000 \n (c) 16500',

]

questions = [
    Question(question_prompts[0], 'c'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'c'),
    Question(question_prompts[3], 'homo sapiens'),
    Question(question_prompts[4], 'b'),
    Question(question_prompts[5], 'b'),
    Question(question_prompts[6], 'a c'),
    Question(question_prompts[7], 'a'),
    Question(question_prompts[8], 'a'),
    Question(question_prompts[9], 'a'),
]

def run_test(questions):
    score = 0
    for question in questions:
        print(question.ques)
        answer = input("Enter a answer: ")
        if answer == question.answer:
            score += 1

    print(f'Your test score is {score} out of  {len(questions)}')

run_test(questions)