# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    s=Stack()
    global fnd
    fnd=False
    corr=list()
    current=problem.getStartState()
    def dfs(vertex):
        global fnd
        if problem.isGoalState(vertex):
            fnd=True
        else:
            if(vertex not in corr):
                corr.append(vertex)
            for v in problem.getSuccessors(vertex):
                if fnd == True:
                    break
                if(  v[0] not in corr):
                    s.push(v[1])
                    dfs(v[0])
                    if fnd == True:
                        break
                    else:
                        s.pop()
    dfs(current)
    path=[]
    while not s.isEmpty():
        path.insert(0,s.pop())
    
    return path

    "util.raiseNotDefined()"

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    fnd=False
    corr=list()
    vertex=problem.getStartState()
    q = util.Queue()
    l = util.Queue()
    q.push(vertex)
    if problem.isGoalState(vertex):
        fnd=True
    else:
        if(vertex not in corr):
            corr.append(vertex)
        while not q.isEmpty() and not fnd:
            j=q.pop()
            for v in problem.getSuccessors(j):
                if problem.isGoalState(v[0]):
                    fnd=True
                    l.push(v)
                    break
                else:
                    if v[0] not in corr:
                        corr.append(v[0])
                        q.push(v[0])
                        l.push(v)

    path=[]
    p=[]
    while not l.isEmpty():
        path.insert(0,l.pop())
    x=path[0]
    y=x[1]
    y3=x[0]
    p.insert(0,y)
    while True:
        zzz=0
        y=x[1]
        y2=x[0]
        if Directions.WEST ==y:
            y3=(y2[0]+1,y2[1])
        if Directions.EAST ==y:
            y3=(y2[0]-1,y2[1])
        if Directions.NORTH ==y:
            y3=(y2[0],y2[1]-1)
        if Directions.SOUTH ==y:
            y3=(y2[0],y2[1]+1)
        for v in path:
            if(v[0]==y3):
                p.insert(0,v[1])
                x=v
                zzz=1
        if zzz is not 1:
            break
        
    return p
    "util.raiseNotDefined()"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
