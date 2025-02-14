# def waterJugProblem(jug1Cap, jug2Cap, targetAmount):    
#     # Initialize the jugs and the possible actions    
#     j1 = 0    
#     j2 = 0    
#     actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), ("pour", 1, 2), ("pour", 2, 1)]       
#     # Create an empty set to store visited states    
#     visited = set()    
#     # Create a queue to store states to visit    
#     queue = [(j1, j2, [])]    
      
#     while queue:    
#         # Dequeue the front state from the queue    
#         j1, j2, seq = queue.pop(0)    
#         # If this state has not been visited before, mark it as visited    
#         if (j1, j2) not in visited:    
#             visited.add((j1, j2))    
#             # If this state matches the target amount, return the sequence of actions taken to get to this state    
#             if j1 == targetAmount or j2 == targetAmount:    
#                 return seq    
#                         # Generate all possible next states from this state    
#             for action in actions:    
#                 if action[0] == "fill":    
#                     if action[1] == 1:    
#                         next_state = (jug1Cap, j2)    
#                     else:    
#                         next_state = (j1, jug2Cap)    
#                 elif action[0] == "empty":    
#                     if action[1] == 1:    
#                         next_state = (0, j2)    
#                     else:    
#                         next_state = (j1, 0)    
#                 else:  # pour action    
#                     if action[1] == 1:    
#                         amount = min(j1, jug2Cap - j2)    
#                         next_state = (j1 - amount, j2 + amount)    
#                     else:    
#                         amount = min(j2, jug1Cap - j1)    
#                         next_state = (j1 + amount, j2 - amount)    
#                         # Add the next state to the queue if it has not been visited before    
#                 if next_state not in visited:    
#                     next_seq = seq + [action]    
#                     queue.append((next_state[0], next_state[1], next_seq))      
#     # If the queue becomes empty without finding a solution, return None    
#     return None    
# result = waterJugProblem(4, 3, 2)    
# print(result)

# #https://www.tpointtech.com/water-jug-problem-in-python


from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)  # Convert list to a set for O(1) lookups
    if endWord not in wordSet:
        return 0  # No transformation possible
    
    queue = deque([(beginWord, 1)])  # (word, steps)
    
    while queue:
        word, steps = queue.popleft()
        
        if word == endWord:
            return steps  # Found shortest path
        
        # Try changing each letter in the word
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    queue.append((newWord, steps + 1))
                    wordSet.remove(newWord)  # Avoid revisiting

    return 0  # No path found

# Example Usage
beginWord = "fool"
endWord = "sage"
wordList = ["fool", "pool", "poll", "pole", "pale", "sale", "sage"]

print(word_ladder(beginWord, endWord, wordList))  # Output: 5