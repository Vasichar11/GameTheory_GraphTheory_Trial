import networkx as nx
import matplotlib.pyplot as plt
import operator
import random

#--------------GAME ON------------------#
G = nx.florentine_families_graph()
TEAMS=[]                     #Teams that will challenge themselves
TEAMS.append("Spaghetti")    #FRIENDLY TEAM-->Spaghetti
G.add_node(TEAMS[-1])
G.add_edge("Spaghetti","Medici")          #Let's say friendly team has these two edges at start.
G.add_edge("Spaghetti","Peruzzi")

TEAMS.append("Tortellini")   #ENEMY TEAM-->Tortellini
G.add_node(TEAMS[-1])
G.add_edge("Tortellini","Albizzi")        #And enemy team has these two.
G.add_edge("Tortellini","Peruzzi")

nx.draw_kamada_kawai(G, with_labels=True)
plt.show()

# Next, both of the teams are eligible to do concurrently one move. Who will make the best move regarding betweenness centrality? (The same algorithm can be used for other types of centralities if little changes are made)

#-------GREEDY STRATEGY-----# (We try all the possible moves at the exact moment, sounds the best option but that's not the case)
b = nx.betweenness_centrality(G)
sorted_b = sorted(b.items(), key=operator.itemgetter(1), reverse=True)  # Sorted families regarding betweenness centrality high-low.
families = []                                   # Some mandatory initializations.
add_o = {}
remove_o = {}
for i in range(17):                             # Assign family names from sorted.b.
 families.append(sorted_b[i][0])

for fam1 in families:
 for fam2 in families:
   t = (fam1, fam2)                              # The edge that I will try to add OR cut.
   if G.has_edge(fam1,fam2):                     # If there is an edge between these families try to cut it and see what happens.
       G.remove_edge(fam1,fam2)
       new = nx.betweenness_centrality(G)
       remove_o[t] = new["Tortellini"] -new["Spaghetti"]   # Betweenness.centrality difference if I remove an edge. I want the maximimum of this!
       G.add_edge(fam1,fam2)                               # Add the removed edge back to the graph, to continue the search.
   else:
    G.add_edge(fam1,fam2)
    new = nx.betweenness_centrality(G)
    add_o[t] =new["Tortellini"]- new["Spaghetti"]          # Betweenness.centrality difference if I add an edge. I want the maximimum of this!
    G.remove_edge(fam1,fam2)                               # Remove the edge that I've just added, to continue the search.
print("")
print("<<-----GAME ON----->>")
print("")
sorted_add_o = sorted(add_o.items(), key=operator.itemgetter(1), reverse=True)      # Sort the things out.
sorted_remove_o = sorted(remove_o.items(), key=operator.itemgetter(1), reverse=True)
print("Best addition/removal for the enemy team(key-->added edge, value-->enemy's new betweenness centrality after this move):")
print("ADD the edge: ",sorted_add_o[0])        # And here we have the best addition for the enemy team. We are going to use that for our advantage
print("or")                                    # We can check here if enemy is using greedy algorithm. If the enemy's moves are always based on our greedy algorithm results, we can bet that they will keep moving "greedy". Now we are one step ahead!
print("REMOVE the edge: ",sorted_remove_o[0])  # Here we have the best removal for the enemy team. We also can use that.
print("\n")
c1=0                                                     # Probability thinking
c2=0                                                     # The possibility to gain dominance is high if we can guess enemy's moves.
flag=0                                                   # Let's find the 5 best options of the enemy, for the exact phase.
bestmoves=[]                                             # Assuming enemy's moves are rational, he have to choose one of these.
print("5 Best additions/removals for the enemy team(edge,'profit',action):")  # Kind of stochastic but this is the character of the problem. First you guess how the enemy is moving and then you move. Otherwise you are in the same page with the enemy, while you want to be one step ahead.

for i in range(5):
    if (sorted_add_o[c1][1]>=sorted_remove_o[c2][1]):
        G.add_edge(sorted_add_o[c1][0][0],sorted_add_o[c1][0][1])
        print(sorted_add_o[c1],"add")
        flag = 0
    else:
        G.remove_edge(sorted_remove_o[c2][0][0],sorted_remove_o[c2][0][1])
        print(sorted_remove_o[c2],"remove")
        flag=1

    add = {}
    remove = {}
    for fam1 in families:
        for fam2 in families:
            t = (fam1, fam2)            # The edge that i will add or remove
            if G.has_edge(fam1, fam2):  # If there is an edge like that, let's try to remove it.
                G.remove_edge(fam1, fam2)
                new = nx.betweenness_centrality(G)
                remove[t] = new["Spaghetti"] - new["Tortellini"]  # key-->(fam1,fam2) with value new["Spaghetti"] - new["Tortellini"] which is the b.centrality difference
                G.add_edge(fam1, fam2)                            # Add the edge again to keep the graph 'untouched'.
                continue
            else:
                G.add_edge(fam1, fam2)
                new = nx.betweenness_centrality(G)
                add[t] = new["Spaghetti"] - new["Tortellini"]
                G.remove_edge(fam1, fam2)                         # Again don't forget to return the graph to original form.
    sorted_add = sorted(add.items(), key=operator.itemgetter(1), reverse=True)

    sorted_remove = sorted(remove.items(), key=operator.itemgetter(1), reverse=True)
    if sorted_add[0][1]>=sorted_remove[0][1]:
        sorted_add[0]= sorted_add[0],"add"
        bestmoves.append(sorted_add[0])
    else:
        sorted_remove[0] = sorted_remove[0],"remove"
        bestmoves.append(sorted_remove[0])
    if flag==1:
        G.add_edge(sorted_remove_o[c2][0][0], sorted_remove_o[c2][0][1])
        c2=c2+2
    else:

        if  (sorted_add_o[c1][0][1],sorted_add_o[c1][0][0]) in G:
            G.remove_edge(sorted_add_o[c1][0][1],sorted_add_o[c1][0][0])
        else:
            G.remove_edge(sorted_add_o[c1][0][0],sorted_add_o[c1][0][1])
        c1=c1+2

print("")
print("Now that we took into consideration how the enemy may move we can proceed to our choice")
print("Finally the best moves for our family sorted by 'betweenness profit'")
print(bestmoves)
print("")
print("<<-----MAKE YOUR CHOICE----->>")