print('Hello, welcome to Computer Science trivia!')

ans = input('Are you ready to play? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. Who is the father of Computer Science? ')
    if ans.lower() == 'alan turing' or ans.lower() == 'turing':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('2. What were the first computers programmed using? ')
    if ans.lower() == 'machine language' or ans.lower() == 'machine code' or ans.lower() == 'machine':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('3. What does CPU stand for? ')
    if ans.lower() == 'central processing unit':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('4. What does RAM stand for? ')
    if ans.lower() == 'random access memory':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    print('Thank you for playing, you got', score, " questions correct.")
    mark = (score/total_q) * 100

    print("Score:", str(mark) + '%')

print('Goodbye!')
        
