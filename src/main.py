from io_utils import read_preferences, write_matches, write_error
from matcher import gale_shapley
from verifier import check_validity, check_stability
import sys

def main():
    """
    Run all of out logic using this as the entry point.
    """
    if len(sys.argv) != 3:
        print("Usage: python src/main.py <input file path> <output file path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        n, hospital_prefs, student_prefs = read_preferences(input_path)
    except:
        write_error(output_path, "Invalid input.")
        return 1
    
    h_match = gale_shapley(n, hospital_prefs, student_prefs)
    write_matches(h_match, output_path)
    return 0

if __name__ == "__main__":
    main()