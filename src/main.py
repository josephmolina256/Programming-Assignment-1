from io_utils import read_preferences, write_matches, write_error
from matcher import gale_shapley
from verifier import check_validity, check_stability
import sys

def main():
    """
    Run all of out logic using this as the entry point.
    """
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("""Usages:
        For matching:
            python src/main.py <input file path> <output file path>
        For matching and verification:
            python src/main.py <input file path> <output file path> --verify""")
        return 1


    input_path = sys.argv[1]
    output_path = sys.argv[2]
    is_verify = True if len(sys.argv) == 4 and sys.argv[3] == "--verify" else False
    
    try:
        n, hospital_prefs, student_prefs = read_preferences(input_path)
    except:
        write_error(output_path, "Invalid input.")
        return 1
    
    h_match = gale_shapley(n, hospital_prefs, student_prefs)

    if is_verify:
        is_valid = check_validity(matching=h_match, n=n)
        is_stable = check_stability(h_match, hospital_prefs, student_prefs)
        if not is_valid:
            write_error(output_path, "Invalid matching.")
            return 1
        if not is_stable:
            write_error(output_path, "Matching is not stable.")
            return 1

    write_matches(h_match, output_path)
    return 0

if __name__ == "__main__":
    main()