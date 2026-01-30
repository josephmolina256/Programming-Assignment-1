from typing import List


def check_validity(
        matching: List[int],
        n: int
    ) -> bool:
    """
    Checks if all students and hospitals have been matched.
    """
    print("length of matching:", len(matching))
    if len(matching) != n:
        print("Length mismatch")
        return False
    if set(matching) != set(range(n)):
        return False
    
    return True

def check_stability(
        matching: List[int],
        hospital_prefs: List[List[int]],
        student_prefs: List[List[int]]
    ) -> bool:
    """
    Checks to see if all matches are stable!
    """

    """
    Example:
    hospital_prefs = [[0, 1, 2],  
                      [1, 2, 0],  
                      [1, 0, 3]]
    student_prefs =  [[1, 0, 3],  
                      [0, 1, 2],
                      [0, 1, 2]]
    matching = [0, 1, 2] 
    """

    n = len(matching)
    for h in range(n):
        s_current = matching[h] # Student currently matched to hospital h
        s_rankings = hospital_prefs[h] # Get hospital h's rankings of students

        for s in s_rankings:
            if s == s_current:
                break
            h_current = matching.index(s)  # Current hospital matched to student s
            h_rankings_s = student_prefs[s]  # Get student s's rankings of hospitals
            for h_pref in h_rankings_s:
                if h_pref == h_current:  # Student prefers current hospital over hospital h
                    break
                if h_pref == h:  # Student prefers hospital h over current
                    return False  # Found instability
    return True