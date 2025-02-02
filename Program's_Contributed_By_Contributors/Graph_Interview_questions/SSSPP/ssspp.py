class Graph:

    def __init__(self, gdict) -> None:
        if gdict is None:
            gdict = dict()
        self.gdict = gdict

    def bfs(self, start, end):

        queue = []

        queue.append([start])

        while queue:

            path = queue.pop(0)

            node = path[-1]

            if node == end:
                return path

            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)

                queue.append(new_path)


cust_dict = {"a": ["b", "c"], "b": ["d", "g"], "c": [
    "d", "e"], "d": ["f"], "e": ["f"], "g": ["f"]}


g = Graph(cust_dict)

print(g.bfs("a", "f"))
