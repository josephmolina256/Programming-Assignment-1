from typing import List

def gale_shapley(
        n: int, 
        hospital_preferences: List[List[int]], 
        student_preferences: List[List[int]]
    ) -> List[int]:
    """
    Hospital-offerer style Gale-Shapley algorithm.

    Args:
        n (int): number of students/hospitals
        hospital_preferences (List[List[int]]): 0-based indexes. Index i in the outer list corresponds to hospital i + 1. The jth item in the inner list corresponds to the j+1-th preferred student.
        student_preferences (List[List[int]]): 0-based indexes. Index i in the outer list corresponds to student i + 1. Index jth item in the inner list corresponds to the j+1-th preferred hospital.

    Returns:
        List[int]: 0-based indexes. List of integers representing the student matched to each hospital. Index i corresponds to hospital i + 1.
    """

    free_hospitals = list(range(n))
    h_match = [None]*n
    s_match = [None]*n
    next_i = [0]*n

    while free_hospitals:
        h = free_hospitals.pop(0)
        if next_i[h] >= n:
            continue
        s = hospital_preferences[h][next_i[h]]
        next_i[h] += 1

        # if the student is unmatched it will (perhaps, temporarily) accept
        if s_match[s] is None:
            s_match[s]=h
            h_match[h]=s

        # otherwise we'll compare the current hospital to the one already assigned
        else:
            flag = False
            assigned_h = s_match[s]
            for hosp in student_preferences[s]:
                # student_preferences are 0-based hospital indices
                if hosp == h:
                    flag = True  # student prefers current hospital h over assigned_h
                    break
                if hosp == assigned_h:  # student prefers assigned_h over current
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