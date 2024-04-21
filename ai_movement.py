from random import randint

def ai_move(ai_list, p_list):
    temp = set(ai_list + p_list)
    temp = list({1,2,3,4,5,6,7,8,9} - temp)
    return temp[randint(0, len(temp)-1)]