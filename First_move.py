import networkx as nx
import matplotlib.pyplot as plt
import operator
import random


G = nx.florentine_families_graph()

#--------------Variables-----------
TEAM = "Spaghetti" #<---------Write your team name here
TEAM_NUM = 2  #<---------Write the number of participants
TEAMS =[]
history = []
#--------------End of variables-----------

G = nx.florentine_families_graph()

TEAMS.append(TEAM)
G.add_node(TEAMS[-1])

TEAMS.append("Tortellini")
G.add_node(TEAMS[-1])

nx.draw_kamada_kawai(G, with_labels=True)
plt.show()

##Strategy of first move that will help the most in the future

b = nx.betweenness_centrality(G)
sorted_b = sorted(b.items(), key=operator.itemgetter(1), reverse=True)
families = []
add = {}
remove = {}
for i in range(16):
 families.append(sorted_b[i][0])
first = []


def greedy(x):
 G.add_edge("Spaghetti",x)
 for fam1 in families:
    for fam2 in families:
        if fam1!=fam2:
            t = (fam1, fam2)  # The edge that is added
            if G.has_edge(fam1, fam2):
                continue
            else:
                G.add_edge(fam1, fam2)
                new = nx.betweenness_centrality(G)
                add[t] = new["Spaghetti"]  # add KEY(fam1,fam2) with value new["Spaghetti"] - new["Tortellini"] which is the difference of b.centrality
                G.remove_edge(fam1, fam2)
 sorted_add = sorted(add.items(), key=operator.itemgetter(1), reverse=True)
 return sorted_add[1]


list=[]
#rand_fam = random.choice(families)
#G.add_edge("Tortellini",rand_fam)
#print("Tortellinis με",rand_fam)
for fam0 in families:
 print("Ii first with",fam0)
 print("Afterwards the best move and the profit is",greedy(fam0))
 s = greedy(fam0)
 list.append((fam0,s[0][1],s[1]))
 G.remove_edge("Spaghetti",fam0)

print("\n")
print("The best first moves, and the sorted profit of them:")
sorted_list= sorted(list, key=lambda item: item[2], reverse=True)
print(sorted_list)