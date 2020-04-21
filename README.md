    STORY
Briefly, Florentine families were families back in the 15th centrury that were acting competitively with each other.
Florence families were trying to become dominant in their network and so there was a network game. 
It's something like "game of thrones", or to be clear, like many of the games in the past that dominion houses played.
You want to be in the center of the social graph and maintain valuable contacts.
Every family is a node in the graph of the social network. 
          
    THINKING
To become dominant in a social network you have to be popular in it.
There are a lot of ways to become popular or to maintain your popularity in a social network.
One of them is to increase or maintain your betweenness centrality of your node.
Betweenness centrality of a node simply is: the "number" of the shortest paths that are crossing this node.
Here, every family wanted to reach every other family without crossing many nodes.
Also the same family would like to be easily reached from other families. 

    THE GAME
We insert two nodes(two families) in the graph and they start to compete each other.
They start with zero connections. And they both do one move at a time. Add or remove any edge in the graph.
Every family wants to be dominant based on different centralities. In this algorithm betweenness centrality is taken into the consideration.

    TACTIC
It's easy for a family to think that "moving using a greedy algorith will be the most efficient" but that's not true.
Using a greedy algorithm in the problem means that you will try all the possible moves(add's-remove's) in the graph an see the result.
Whichever move gives you big possitive difference, that is what you choose to play.
That's not smart enough since the enemy family is making moves at the same time your family does. That means that the graph is changing dynamically while you make a move. The graph you are playing to is not known
So it's mandatory to think what's the possible enemy's move, before you make your move. There is no other way but to think that the enemy is moving orthologically.
Inserting in the equation the probable move of the enemy gives a first advantage to the game.

    FIRST MOVE
The first move is critical. It can so the tactic here is:
Greedy implementation for the enemy node ----> most possible orthological moves for them
Greedy implementation for our node in graphs with the most possible orthological moves of the enemy ----> most possible starting moves that will be efficient

    ACKNOWLEDGEMENT
Won't work if the enemy is thinking exactly like us. The winner here will be the one that has the most nested loops and calculating the most probable moves of the enemy before implementing their algorithm.
So whoever looks more forward has bigger chances of winning. Estimating further the moves of the enemy can be valuable.
Doing so you will have to deal with many data that are difficult to handle.

    VALUABLE ANNOTATION
Finding out that the enemy is using greedy algorithm means that you are one step ahead. You know their next move, so you implement greedy algorithm on the new graph that includes their greedy act. No way to lose here, because a greedy implementation in a knowned graph is the perfect option.
