# N Queens Problem
Solved using Hill Climbing Heuristic Search technique. This searching is implemented
using simple HCS, so it may get stuck on Local Maxima.

Iterative HC will restart every time if the HC gets stuck, the default no of iterations
can be determined by the iterations parameter

## Algorithm

Simple Hill Climbing Search

```

heurisitc = h(currentState)
while True
    neighbours = currentState
    neighbour = min(h(nieghbours))
    newHeurisitc = h(neighbour)

    if newHeuristic >= heuristic
        exit

    currentState = neighbour

```

Iterative Hill Climbing Search

```

for 0 --> iterations
    heurisitc = h(currentState)
    while True
        neighbours = currentState
        neighbour = min(h(nieghbours))
        newHeurisitc = h(neighbour)
    
        if newHeuristic >= heuristic
            exit
    
        currentState = neighbour

    if stuck in local maxima
        restart --> new currentState

```

## Examples
n = 4
```
Starting Board :: 
Q  -  -  -  
-  Q  -  -  
-  -  -  Q  
-  Q  -  -  


Final Board :: 
-  -  Q  -  
Q  -  -  -  
-  -  -  Q  
-  Q  -  -  


Steps climbed :: 2
```

n = 5
```
Starting Board :: 
-  -  -  Q  -  
-  -  -  -  Q  
-  -  -  -  Q  
Q  -  -  -  -  
-  -  -  Q  -  

Final Board :: 
-  Q  -  -  -  
-  -  -  -  Q  
-  -  Q  -  -  
Q  -  -  -  -  
-  -  -  Q  -  

Steps climbed :: 2
```

Local Maxima Case
```
Starting Board :: 
Q  -  -  -  -  
Q  -  -  -  -  
-  -  -  Q  -  
-  -  -  Q  -  
Q  -  -  -  -  

Final Board :: 
-  -  Q  -  -  
Q  -  -  -  -  
-  -  -  Q  -  
-  -  -  Q  -  
Q  -  -  -  -  

Steps climbed :: 1
Stuck at Local Maxima State
```