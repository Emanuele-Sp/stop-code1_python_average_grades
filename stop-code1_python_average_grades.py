# stop_&_code1/average_grade.py
list_of_grades = []
list_of_grades_with_subjects = []
positive_grades = []
negative_grades = []

subjects = ["italiano", "matematica", "storia", "geografia", "fisica", "Biiologia", "educazione fisica", "informatica", "chimica", "arte"]

def insert_grade(number_of_votes): # number_of_votes: list, subjects: list
    for i in range(number_of_votes):
        while True:
            grade = input(f"Inserisci un voto da 0 a 10 per {subjects[i]} ")
            try:
                grade = int(grade)
                if grade >= 1 and grade <= 10:
                    total_list = []
                    total_list.append(subjects[i])
                    total_list.append(grade)
                    list_of_grades_with_subjects.append(total_list)
                    list_of_grades.append(grade)
                    if grade >= 6:
                        list_positive = []
                        list_positive.append(subjects[i])
                        list_positive.append(grade)
                        positive_grades.append(list_positive)
                        break
                    else:
                        list_negative = []
                        list_negative.append(subjects[i])
                        list_negative.append(grade)
                        negative_grades.append(list_negative)
                        break
                else:
                    print("Valore non valido")
                
            except ValueError as veEx:
                print("Inserisci un valore valido")   
                
def media(list_of_grades):
    # media = 0
    # for m in list_of_grades:
        # media += m
    media = sum(list_of_grades)
    return  media/len(list_of_grades)
        
def print_result(med):
    if med >= 6:
        print("Congratulazioni sei stato PROMOSSO!")
    else:
        print("Mi dispiace sei stato BOCCIATO!")
        
def highest_grade():
    # grade = 0
    # for g in list_of_grades:
        # if g > grade:
            # grade = g
    grade = max(list_of_grades)
    return grade
    
def lower_grade():
    # grade = 10
    # for g in list_of_grades:
        # if g < grade:
            # grade = g
    grade = min(list_of_grades)
    return grade

def votes_above_average(med):
    count = 0
    for i in list_of_grades:
        if i > med:
            count += 1
    return count

def votes_below_average(med):
    count = 0
    for i in list_of_grades:
        if i < med:
            count += 1
    return count

def numbers_above_below(number: int, space: str):
    if number == 0:
         return f"Non ci sono valori {space} la media"
    elif number == 1:
        return f"C'è un valore {space} la media"
    else:
        return f"Ci sono {number} valori {space} la media"
        
def numbers_negative(number):
    if number == 0:
        return f"Non ci sono voti insufficienti"
    elif number == 1:
        return f"C'è un valore insufficiente"
    else:
        return f"Ci sono {number} valori insufficienti"
        
# FUNZIONE PRINCIPALE
while True:
    number_of_votes = input("Inserisci il numero di voti che vuoi aggiungere: ")
    try:
        number_of_votes = int(number_of_votes)
        if number_of_votes > 1 and number_of_votes < 10:
            insert_grade(number_of_votes)
            med = media(list_of_grades)
            print(list_of_grades)
            print(positive_grades)
            print(negative_grades)
            print(med)
            print_result(med)
            print(f"Il voto più alto è {highest_grade()}")
            print(f"Il voto più basso è {lower_grade()}")       
            print(numbers_above_below(votes_above_average(med), "sopra"))
            print(numbers_above_below(votes_below_average(med), "sotto"))
            print(numbers_negative(len(negative_grades)))
            break
        else:
            print("Inserisci un valore da 1 a 10: ")
    except ValueError as veEX:
        print("Inserisci un valore numerico: ")
