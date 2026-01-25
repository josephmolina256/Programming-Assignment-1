def read_preferences(path):
	"""
	Reads input file from path.
	Returns:
		n: int
		hospital_prefs: list[list[int]]
		student_prefs: list[list[int]]
	"""

	with open(path, "r") as f:
		lines = [line.strip() for line in f if line.strip()]
	
	if not lines:
		raise ValueError("Empty input file")

	n = int(lines[0])
	if len(lines) != 1 + 2 * n:
		raise ValueError("Malformed input. Wrong number of lines")

	...


def write_matches():
	...

