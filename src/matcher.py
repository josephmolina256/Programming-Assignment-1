def parse_input(path):
    with open(path, "r") as f:
        n = int(f.readline())

        hospital_preferences = []
        for i in range(n):
            hospital_preferences.append([int(x) for x in f.readline().split()])

        student_preferences = []
        for i in range(n):
            student_preferences.append([int(x) for x in f.readline().split()])

    return n, hospital_preferences, student_preferences

def gale_shapley(n, hospital_preferences, student_preferences):

    free_hospitals = list(range(n))
    h_match = [None]*n
    s_match = [None]*n
    next_i = [0]*n

    while free_hospitals:
        h = free_hospitals.pop(0)
        s = hospital_preferences[h][next_i[h]]
        next_i[h] += 1

        # if the student is unmatcged it will (perhaps, temporarily) accept
        if s_match[s] is None:
            s_match[s]=h
            h_match[h]=s

        # otherwise we'll compare the current hospital to the one already assigned
        else:
            flag = False
            assigned_h = s_match[s]
            for hosp in student_preferences[s]:
                if hosp == h: 
                    flag = True #student preferes current to assigned
                    break
                if hosp == assigned_h: #student preferes assigned to current
                    break

            # reassign hospital if necessary, turn old hospital free
            if flag:
                s_match[s]=h
                h_match[h]=s
                h_match[assigned_h]=None
                free_hospitals.append(assigned_h)      
            else:
                free_hospitals.append(h) 

    return h_match