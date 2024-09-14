import os
import Utils

def add_score(difficulty):
    score = 0
    if (not os.path.exists(Utils.SCORES_FILE_NAME)):
        file = open(Utils.SCORES_FILE_NAME,'a')
        file.write(str((difficulty*3)+5))
        file.close()
    else:
        file = open(Utils.SCORES_FILE_NAME,'r')
        score = file.readline()
        score = int(score)
        file.close()
        score += (difficulty*3)+5
        file = open(Utils.SCORES_FILE_NAME, 'w')
        file.write(str(score))
        file.close()