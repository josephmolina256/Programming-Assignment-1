from typing import List

def read_preferences(path: str):
	"""
	Reads input file from path.
	Returns:
		n: int
		hospital_prefs: List[List[int]]
		student_prefs: List[List[int]]
	"""

	with open(path, "r") as f:
		lines = [line.strip() for line in f if line.strip()]
	
	if not lines:
		raise ValueError("Empty input file")

	n = int(lines[0])
	if len(lines) != 1 + 2 * n:
		raise ValueError("Malformed input. Wrong number of lines")

	hospital_preferences = []
	for i in range(1, n + 1):
		hospital_preferences.append([int(x) - 1 for x in lines[i].split()])

	student_preferences = []
	for i in range(n + 1, 2 * n + 1):
		student_preferences.append([int(x) - 1 for x in lines[i].split()])

	return n, hospital_preferences, student_preferences


def write_matches(h_match: List[List[int]], output_path: str = "data/example.out"):
	"""
	Writes matches to output file.
	"""
	n = len(h_match)
	with open(output_path, "w") as f:
		for h in range(n):
			s = h_match[h]
			# Convert to 1-based indexing
			f.write(f"{h + 1} {s + 1}\n")

def write_error(output_path: str, message: str):
	"""
	Writes an error to output file for malformed inputs.
	"""
	with open(output_path, "w") as f:
		f.write(message)