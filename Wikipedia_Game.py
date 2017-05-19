from Structures import *
import wikipedia


def safe_get(title):
    """Safely gets a Wikipedia article object for the inputted title. Some links within Wikipedia pages link to articles
    that have not been created yet. This is a method for ignoring those, as the wikipeida package throws an error for 
    these articles."""
    assert isinstance(title, str)
    try:
        return wikipedia.page(title)
    except:
        return

def is_valid_article(title):
    """Determines whether a given title links to a valid Wikipedia page. Similar reasonoing as in safe_get(), see
    previous docstring for more info."""
    assert isinstance(title, str)
    try:
        wikipedia.page(title)
        return True
    except:
        return False


def solve_wikipedia_game(article1, article2):
    """Wikipedia solver funtion. Uses breadth-first search on the links in an article."""
    assert isinstance(article1, str) and isinstance(article2, str)
    assert is_valid_article(article2)
    source = wikipedia.page(article1)  # errors if source article is invalid
    if article1 == article2:
        return [article1]
    fringe = Queue()
    tree = Tree(source)
    used = set()
    fringe.enqueue(tree)
    while not fringe.is_empty():
        current = fringe.dequeue()
        if current.visited:
            # This node has already been processed.
            continue
        current.visited = True
        for i in current.links():
            if i == article2:
                # skips out on much extra searching.
                return tree_path(current, article1)
            if i not in used:
                # The child is not in the queue.
                article = safe_get(i)
                if article:
                    # safe_get() returns None if the article is invalid; None is False in Python.
                    # This block continues tree construction.
                    used.add(i)
                    branch = Tree(article, current)
                    current.add_children(branch)
                    fringe.enqueue(branch)


def tree_path(node, article1):
    """Returns the trace from article1 to article2 (arguments to solve_wikipedia_game)."""
    assert isinstance(node, Tree)
    path = []
    while node.parent is not None:
        # node.parent is None iff Node is the root of the tree ie. article1
        path.append(node.title())
        node = node.parent
    path.append(article1)
    path.reverse()
    return path
