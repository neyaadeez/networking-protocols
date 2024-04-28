from collections import defaultdict

class OSPF:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_link(self, source, destination, cost):
        self.graph[source][destination] = cost
        self.graph[destination][source] = cost

    def shortest_path_tree(self, source):
        visited = set()
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        shortest_paths = {}

        while len(visited) < len(self.graph):
            current_node = min((node for node in self.graph if node not in visited), key=lambda x: distances[x])
            visited.add(current_node)

            for neighbor, cost in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + cost
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        shortest_paths[neighbor] = current_node

        return shortest_paths

# Example usage
ospf = OSPF()
ospf.add_link('A', 'B', 1)
ospf.add_link('A', 'C', 2)
ospf.add_link('B', 'C', 1)
ospf.add_link('B', 'D', 3)
ospf.add_link('C', 'D', 1)

shortest_paths = ospf.shortest_path_tree('A')
print("Shortest path tree from node A:")
print(shortest_paths)
