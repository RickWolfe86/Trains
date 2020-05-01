import collections


class Graph:
    def __init__(self):
        self.graph = []
        self.path_list = []
        # creating named tuple for the node,edge and distance for better code visualization
        self.node_edge = collections.namedtuple("node_edge", ["start", "end", "distance"], rename=False)

    def build_graph(self, node_edges_distance_inputs):
        """
        Builds a graph from nodes and edges and distances inputs

        Args:
            node_edges_distance_inputs (string): the nodes, edges, distance separated by ", "(Example: 'AB5, BC4, CD8')
        Returns:
            bool: True if successful, False otherwise.
        """
        # building graph into a list of named tuple
        try:
            self.graph = [self.node_edge(start=x[0], end=x[1], distance=(int(x[2:]))) for x in
                          node_edges_distance_inputs.split(", ")]
        except:
            return False
        return True

    def get_all_sub_path_distances(path):
        """
        Return a list of all sub-paths distance from a path

        Args:
            path (list): list of named tuple node_edge
        Returns:
            list: a list of sub-paths distances
        """
        try:
            return [sub_path.distance for sub_path in path]
        except:
            return []

    def get_total_path_distance(path):
        """
        Return the total distance of a path

        Args:
            path (list): list of named tuple node_edge
        Returns:
            int: a sum of all distances of the path
        """
        return sum(Graph.get_all_sub_path_distances(path))

    def build_path_list(self, start_node, end_node, path_stop=0, max_path_stop=100, max_distance=0, sub_path=[]):
        """
        Build a list of path given start and end node

        Args:
            start_node (string): the start node of the path
            end_node (string): the end node of the path
            path_stop (int, optional): exact stops will the path have
            max_path_stop (int, optional): maximum stops of the path
            max_distance (int, optional): maximum distance of the path
            sub_path(list): internal don't use
        Returns:
            list: a list of all path who was found given start and end node
        """
        all_path_list = []
        path_array = []
        for g in self.graph:
            path_aux = sub_path.copy()

            if start_node == g.start:
                path_aux.append(self.node_edge(start=g.start, end=g.end, distance=g.distance))
                # if its not the end and max path size not reached them try to reach end node using actual end node
                # as start
                if (end_node != g.end and len(path_aux) < max_path_stop) or len(path_aux) < path_stop:
                    path_array += self.build_path_list(g.end, end_node, path_stop, max_path_stop, max_distance,
                                                       path_aux)
                else:
                    path_array = [path_aux]
                # if the max distance is different from 0 and the total distance of the path didint meet them try to
                # get news path
                if 0 < max_distance >= Graph.get_total_path_distance(path_aux):
                    path_array += self.build_path_list(g.end, end_node, path_stop, max_path_stop, max_distance,
                                                       path_aux)

                # if path_aux has at least one path and the last position is the end node, them we have a full path
                # and only appends if its a new path
                for p in path_array:
                    if len(p) > 0 and p[-1].end == end_node and p not in all_path_list \
                            and (max_distance == 0 or (0 < max_distance > Graph.get_total_path_distance(p))) \
                            and (path_stop == 0 or (0 < path_stop == len(p))):
                        all_path_list.append(p)

        return all_path_list

    def find_path_size(self, list_of_nodes):
        """
        Return the path size from self.path_list given list of nodes

        Args:
            list_of_nodes (list):
        Returns:
            int or string: if successful the minimum distance path else the string 'NO SUCH ROUTE'
        """
        size = 0
        # reducing path list for better perfomance
        reduced_path_list = [x for x in self.path_list if len(x) + 1 == len(list_of_nodes)]
        for paths in reduced_path_list:
            for x in range(len(list_of_nodes) - 1):
                if [paths[x].start, paths[x].end] == [list_of_nodes[x], list_of_nodes[x + 1]]:
                    size += paths[x].distance
                else:
                    size = 0
                    break
            # if size > 0 means that never entered in else statement so it has the full path and there is no
            # need to continue the loop
            if size > 0:
                break
        if size == 0:
            return 'NO SUCH ROUTE'
        return size

    def shortest_path(self):
        """
        Return the shortest path of self.path_list

        Args:
            no args
        Returns:
            int: the minimum length distances on the path
        """
        return min([Graph.get_total_path_distance(path) for path in self.path_list])

    def number_routes(self):
        """
        Return the number of routes on the self.path_list

        Args:
            no args
        Returns:
            int: the sum of all length distances on the path
        """
        return len([Graph.get_total_path_distance(path) for path in self.path_list])
