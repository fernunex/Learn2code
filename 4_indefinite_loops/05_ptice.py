# Problem name: COCI '08 Contest 1 #2 Ptice
# Code: coci08c1p2
# Link: https://dmoj.ca/problem/coci08c1p2

n_questions = int(input())
answers = input()
i = 0

adrian_correct = 0 #  A , B , C , A , B , C , A , B , C , A , B , C , ...
bruno_correct = 0 #  B , A , B , C , B , A , B , C , B , A , B , C , … 
gora_correct = 0 #  C , C , A , A , B , B , C , C , A , A , B , B , … 

adrian_secuence = 'ABC'
bruno_sequence = 'BABC'
gora_sequence = 'CCAABB'

while i < n_questions:
    correct_answer = answers[i]

    if correct_answer == adrian_secuence[i % 3]:
        adrian_correct += 1
    
    if correct_answer == bruno_sequence[i % 4]:
        bruno_correct += 1
    
    if correct_answer == gora_sequence[i % 6]:
        gora_correct += 1

    i += 1

if adrian_correct == bruno_correct and bruno_correct == gora_correct: # All wins
    print(adrian_correct)
    print('Adrian')
    print('Bruno')
    print('Goran')
elif adrian_correct == bruno_correct: 
    
    if adrian_correct > gora_correct: # Adrian and Bruno wins
        print(adrian_correct)
        print('Adrian')
        print('Bruno')
    
    else: # Gora wins
        print(gora_correct)
        print('Goran')


elif adrian_correct == gora_correct:
    if adrian_correct > bruno_correct: # Adrian and Gora wins
        print(adrian_correct)
        print('Adrian')
        print('Goran')
    
    else: # Bruno wins
        print(bruno_correct)
        print('Bruno')

elif gora_correct == bruno_correct:
    if gora_correct > adrian_correct: # Gora and Bruno wins
        print(gora_correct)
        print('Bruno')
        print('Goran')
    else: # Adrian Wins
        print(adrian_correct)
        print('Adrian')
elif adrian_correct > bruno_correct and adrian_correct > gora_correct: # Adrian wins
    print(adrian_correct)
    print('Adrian')
elif bruno_correct > adrian_correct and bruno_correct > gora_correct: # Bruno wins
    print(bruno_correct)
    print('Bruno')
else: # Goran wins
    print(gora_correct)
    print('Goran')


