tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

def school_student():
    i = 0
    j = 0
    while i < max(len(tutors), len(klasses)):
        if i >= len(tutors):
            yield (None, klasses[i])
        elif j>= len(klasses):
            yield (tutors[j], None)
        else:
            yield (tutors[j], klasses[i])
        i += 1
        j += 1


for gen in school_student():
    print(gen)