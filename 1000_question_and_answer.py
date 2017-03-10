# -*- coding: UTF-8 –*-
questions = {}
answers = {}

level_name = {}

with open('1000_answers_raw.txt','rb') as fd:
    current_sec = 'test'
    current_answer = ''
    ans_tmp = {}
    for item in fd:
        line = item.decode('utf8').strip()
        #print line[:11]
        if line[:7] == 'section' and line[:11] != current_sec:
            answers[current_sec] = ans_tmp
            ans_tmp = {}
            current_sec = line[:11].strip()
            continue
        if line[:3].strip() in ['01.', '02.', '03.', '04.', '05.', '06.', '07.', '08.', '09.', '10.']:
            current_answer = line[:3].strip()
            ans_tmp[current_answer] = []
            lines = line.split('$$$$$$')
            ans_tmp[current_answer] = lines
    answers[current_sec] = ans_tmp
    #with open('wocao.txt', 'wb')as kk:
        #pprint.pprint(answers, stream=kk)





with open('1000_questions_raw.txt','rb') as fd:
    current_sec = 'test'
    current_question = ''
    ques_tmp = {}
    for item in fd:
        line = item.strip()
        if line[:7] == 'section' and line[:11] != current_sec:
            questions[current_sec] = ques_tmp
            ques_tmp = {}
            level = line.split()[2]
            current_sec = line[:11].strip()
            level_name[current_sec] = level
            continue
        if line[:3].strip() in ['01.','02.','03.','04.','05.','06.','07.','08.','09.','10.']:
            current_question = line[:3].strip()
            ques_tmp[current_question] = []
            ques_tmp[current_question].append(line)
        else:
            ques_tmp[current_question].append(line)
        #questions[current].append(line)
    questions[current_sec] = ques_tmp
    #with open('wocao1.txt', 'wb')as kk:
        #pprint.pprint(questions,stream=kk)

def read_from_answer(sec,question,answers):
    my_answer = answers[sec][question]
    explan = my_answer[0]
    translate = my_answer[1]
    return explan,translate


def write_q_and_a():
    kk = ['01.','02.','03.','04.','05.','06.','07.','08.','09.','10.']
    i = 1
    with open('final.txt', 'wb') as fd:
        while i <= 100:
            current_sec = 'section ' + str(i).rjust(2,'0')
            level = level_name[current_sec].rjust(5,' ')
            current_sec0 = '********************************************'
            current_sec1 = '*                                     ' + current_sec + '                                     *'
            current_sec2 = '*                                         ' + level + '                                          *'
            current_sec3 = '********************************************'
            fd.write(current_sec0)
            fd.write('\n')
            fd.write(current_sec1)
            fd.write('\n')
            fd.write(current_sec2)
            fd.write('\n')
            fd.write(current_sec3)
            fd.write('\n')

            for current_num in kk:
                q_lsit = questions[current_sec][current_num]
                for ll in q_lsit:
                    fd.write(ll)
                    fd.write('\n')
                a_explan,a_translate = read_from_answer(current_sec,current_num,answers)
                a_explan = '###'+a_explan[4:]
                a_translate = '***翻译：'.decode('utf8') + a_translate
                fd.write('\n')
                fd.write(a_explan.encode('utf8'))
                fd.write('\n')
                fd.write(a_translate.encode('utf8'))
                fd.write('\n')
                fd.write('\n')
            i += 1

write_q_and_a()

'''
with open('1000_answers_raw.txt','rb') as fd:
    current = ''
    answers = {}
    for item in fd:
        line = item.decode('utf8').strip()
        if line[:7] == 'Section' and line != current:
            current = line
            answers[line] = []
            continue
        if line:
            answers[current].append(line)
    with open('wocao.txt','wb')as kk:
        for sec in answers:
            jj = answers[sec]
            for line in jj:
                kk.write(line.encode('utf8'))
                kk.write('\n')
'''
