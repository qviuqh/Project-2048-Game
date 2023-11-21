new_score = 0

with open("user/high_score.txt",'r') as file:
    high_score = int(file.read())
    file.close()

def update_high_score(new_value):
    with open("user/high_score.txt",'w+') as file:
        file.write(str(new_value))
        file.close()