# Write a program to implement A* algorithm.


from simpleai.search import SearchProblem, astar


GOAL = "HELLO WORLD"


class hello_problem(search_problem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # How far are we from the goal?

        wrong = sum([1 if state[i] != GOAL[i] else 0 for i in range(len(state))])

        missing = len(GOAL) - len(state)
        return wrong + missing


problem = hello_problem(initial_state="")
result = astar(problem)
print(result.state)
print(result.path())
