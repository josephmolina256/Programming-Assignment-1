from src.io_utils import read_preferences
from src.matcher import gale_shapley
from src.verifier import check_validity, check_stability
import sys

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'data/taskC/n512.in'
    n_read, hospital_prefs, student_prefs = read_preferences(input_file)
    h_match = gale_shapley(n_read, hospital_prefs, student_prefs)
    print('input:', input_file)
    print('valid:', check_validity(h_match, n_read))
    print('stable:', check_stability(h_match, hospital_prefs, student_prefs))
    print('len matching:', len(h_match))

if __name__ == '__main__':
    main()
