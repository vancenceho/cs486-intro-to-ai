"""Implementation of Problem 3, Assignment 1, CS486, Winter 2025.

Please replace 'pass  #(TODO) complete this function' with your own
implementation. Please do not change other parts of the code, including the
function signatures; however, feel free to add imports.
"""
import model
from queue import PriorityQueue
import math


def decode(model: model.LanguageModel, k: int = 2, n: int = 3) -> str:
    """Lowest-cost-first search with frontier size limit.

    Args:
        model: A language model.
        k: the frontier size limit. Default is 2.
        n: the length of the desired sentence. Default is 3.

    Returns:
        The decoded text, where words are separated by a single space.

    Hints:
        1. model.vocab() gives you the vocabulary.
        2. model.prob(w: str, c: List[str]) gives you the probability of word
           w given previous context c.
    """
    # TODO: complete this function
    vocab = model.vocab()
    frontier = PriorityQueue()
    frontier.put((0, []))

    while not frontier.empty():
        cost, sentence = frontier.get()

        if len(sentence) == n:
            return ' '.join(sentence)

        for word in vocab:
            new_sentence = sentence + [word]
            prob = model.prob(word, sentence)
            
            if prob > 0:
                new_cost = cost - math.log(prob)
                frontier.put((new_cost, new_sentence))

        new_frontier = PriorityQueue()
        for _ in range(min(k, frontier.qsize())):
            new_frontier.put(frontier.get())
        frontier = new_frontier

    return ''
    

if __name__ == '__main__':
    m = model.LanguageModel()
    if decode(m, 2, 3) == 'a dog barks' and decode(m, 1, 3) == 'a cat meows':
        print('success!')
    else:
        print('There might be something wrong with your implementation; please double check.')
