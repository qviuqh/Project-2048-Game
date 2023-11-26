# Create new score
new_score = 0

# Read file and collect the best score
with open("user/high_score.txt",'r') as file:
    high_score = int(file.read())
    file.close()

# Update the best score
def update_high_score(new_value):
    with open("user/high_score.txt",'w+') as file:
        file.write(str(new_value))
        file.close()