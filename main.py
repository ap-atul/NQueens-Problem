from lib.solver import Solver

solver = Solver(n=10, verbose=False)
solver.runHillClimbing()

print(f"Steps climbed :: {solver.getStepsClimbed()}")
if solver.getHeuristics()[1] > 0.0:
    print("Stuck at Local Maximal State")
    print(f"Heuristics values :: {solver.getHeuristics()[0]} "
          f" {solver.getHeuristics()[1]}")
