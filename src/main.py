from io_utils import read_preferences, write_matches
from matcher import gale_shapley
from verifier import check_validity, check_stability

def main():
    """
    Run all of out logic using this as the entry point.
    """
    input_path = "data/example.in"
    n, hospital_prefs, student_prefs = read_preferences(input_path)
    h_match = gale_shapley(n, hospital_prefs, student_prefs)
    write_matches(h_match, "data/example.out")
    return 0

if __name__ == "__main__":
    main()