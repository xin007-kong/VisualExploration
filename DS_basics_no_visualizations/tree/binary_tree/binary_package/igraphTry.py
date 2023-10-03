import matplotlib.pyplot as plt
import igraph as ig

g = ig.Graph.Tree(n=7, children=2)
plt.figure()
ig.plot(g, target=plt.gca())
plt.show()
