from Queue import *
import wikipedia

def solve_wikipedia_game(article1, article2):
    fringe = Queue()
    tree = Tree(article1)
    used = set()
    fringe.enqueue(article1)
