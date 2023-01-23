score_dict = {'calculus': 60}
input_subject = 'python'
input_score = 50

def add_score(subject_score,subject,score):
    this_dict = subject_score
    this_dict.update({subject : score})

add_score(score_dict,input_subject,input_score)
def calc_average_score(para_dict):
    count = 0
    for i in para_dict:
        count += 1
    total = sum(para_dict.values())
    mean = total/count

    return "{:.2f}".format(mean)
    
print(calc_average_score(score_dict))