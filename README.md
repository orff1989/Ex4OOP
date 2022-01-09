![image](https://user-images.githubusercontent.com/93159965/147562147-754a2b7c-d5d0-44c8-b6d9-a37ce5fc1b44.png)

# Assignment 4

> Made by Or Finberg
>
> GitHub page:  
> [https://github.com/orff1989](https://github.com/orff1989)


# The Pokemon game - python
In this project, we build a graph with Pokemons and the agents need to catch as many Pokemons as possible.



# Analysis of the performance of the algorithms:

![Screenshot 2021-12-27 232312](https://user-images.githubusercontent.com/43110158/147508128-080c7d0a-e1d4-40e3-af4f-0393b710bbd4.png)

PC specifications: CPU: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz 2.30 GHz, Ram:16GB, Operating System: Windows 11 64bit.

# UML Diagram

This is a uml of the project:

![Class Diagram](ClassesDiagram.png)



### How To Run
clone this project by: git clone https://github.com/orff1989/Ex4OOP.git
run the server, Ex4_Server_v0.0.jar, with the command: java -jar Ex4_Server_v0.0.jar 0.
run the python file, student_code, and then the gui will show up.


## DiGraph class - implements GraphInterface

This class implement GraphInterface abstract class that represents an interface of a graph.

Each DiGraph contain dictionary of his nodes, and each node contain his edges.\
In addition each DiGraph holds the number of edges in the graph and a mode counter (mc)\
that represent the number of changes (add node, add edge, remove node or remove edge) in the graph.


| **Main methods**      |    **Details**        |
|-----------------|-----------------------|
| `v_size()` | Returns the number of vertices in this graph |
| `e_size()` | Returns the number of edges in this graph |
| `get_mc()` | Returns the current version of this graph |
| `add_edge()` | Adds an edge to the graph |
| `add_node()` | Adds a node to the graph |
| `remove_node()` | Removes a node from the graph |
| `remove_edge()` | Removes an edge from the graph |



## GraphAlgo class - implenents GraphAlgoInterface
This class implement GraphAlgoInterface abstract class that represents an interface of a graph.\
Each GraphAlgo contain a DiGraph on which the algorithm works on.


| **Main methods**      |    **Details**        |
|-----------------|-----------------------|
| `get_graph()` | Rutern the directed graph on which the algorithm works on |
| `load_from_json()` | Loads a graph from a json file |
| `save_to_json()` | Saves the graph in JSON format to a file |
| `shortest_path()` | Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm |
| `TSP()` | Finds the shortest path that visits all the nodes in the list |
| `centerPoint()` |   Finds the node that has the shortest distance to it's farthest node |
| `dijkDist()` |  returns all the shortest path from the given source and its distance. Link to Dijkstra's algorithm- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm |
| `theLightNextNodeNotVisited()` | returns the closest and lightest node from a given node |
| ` theLightNextNode()` | returns lightest node from a given node |
| `sumOfW()` | returns the weight of the givien list |
| `eccentricity()` |  returns list of the largest pathh |
| `plot_graph()` | Plots the graph |

## External info:
- More about graph : https://en.wikipedia.org/wiki/Directed_graph


