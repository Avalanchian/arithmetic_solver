class Problem:
    def solve(self):
        if self.op == '+':
            return self.num1 + self.num2
        else:
            return self.num1 - self.num2

    def get_lines(self):
        """Prepare the string for each line in the output."""
        lines = [""] * 4
        lines[0] = "  {: >{pad}d}".format(self.num1, pad=self.num1_pad)
        lines[1] = "{:s} {: >{pad}d}".format(self.op, self.num2, pad=self.num2_pad)
        lines[2] = "--" + "-" * max(self.num1_len, self.num2_len)
        lines[3] = "{: >{p}d}".format(self.solution, p=len(lines[2]))
        return lines

    def error_check(self):
        if self.op not in ['+', '-']:
            return (True, "Error: Operator must be '+' or '-'.")
        elif self.num1 >= 10_000 or self.num2 >= 10_000:
            return (True, 'Error: Numbers cannot be more than four digits.')
        else:
            return (False, None)

    def __init__(self, problem):
        parts = problem.split()
        self.num1 = int(parts[0])
        self.num1_len = len(parts[0])
        self.num2 = int(parts[2])
        self.num2_len = len(parts[2])
        self.op = parts[1]
        self.solution = self.solve()

        if self.num1_len < self.num2_len:
            self.num1_pad = self.num2_len
        else:
            self.num1_pad = 0

        if self.num2_len < self.num1_len:
            self.num2_pad = self.num1_len
        else:
            self.num2_pad = 0
        
        self.lines = self.get_lines()


def arithmetic_arranger(request, give_solution=False):
    # Perform error checking and initialise problem objects.
    if len(request) > 5:
        return ('Error: Too many problems.')
    try:
        problems = [Problem(problem) for problem in request]
    except ValueError:
        return ('Error: Numbers must only contain digits.')
    for p in problems:
        if p.error_check()[0]:
            return (p.error_check()[1])

    # Join the parts of each line together.
    arranged_problems = [""] * 4
    arranged_problems[0] += "    ".join([p.lines[0] for p in problems])
    arranged_problems[1] += "    ".join([p.lines[1] for p in problems])
    arranged_problems[2] += "    ".join([p.lines[2] for p in problems])
    arranged_problems[3] += "    ".join([p.lines[3] for p in problems])
    
    if give_solution:
        return "\n".join(arranged_problems)
    else:
        return "\n".join(arranged_problems[:3])