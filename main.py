from lib.Graph import Graph


list_routes = input("Input the routes.(Example: 'AB5, BC4, CD8'):")
#list_routes = "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

graph_routesAC = Graph()
graph_routesAC.build_graph(list_routes)
graph_routesAC.path_list = graph_routesAC.build_path_list('A', 'C')

graph_routesAD = Graph()
graph_routesAD.build_graph(list_routes)
graph_routesAD.path_list = graph_routesAC.build_path_list('A', 'D')

##############################################################################################################

size = graph_routesAC.find_path_size(["A", "B", "C"])
print('Output #1:', size)

##############################################################################################################

size = graph_routesAD.find_path_size(["A", "D"])
print('Output #2:', size)

##############################################################################################################

size = graph_routesAC.find_path_size(["A", "D", "C"])
print('Output #3:', size)

##############################################################################################################

size = graph_routesAD.find_path_size(["A", "E", "B", "C", "D"])
print('Output #4:', size)

##############################################################################################################

size = graph_routesAD.find_path_size(["A", "E", "D"])
print('Output #5:', size)

##############################################################################################################

graph_routesCC3 = Graph()
graph_routesCC3.build_graph(list_routes)
graph_routesCC3.path_list = graph_routesAC.build_path_list('C', 'C', max_path_stop=3)

print('Output #6:', len(graph_routesCC3.path_list))

##############################################################################################################

graph_routesAC4 = Graph()
graph_routesAC4.build_graph(list_routes)
graph_routesAC4.path_list = graph_routesAC4.build_path_list('A', 'C', path_stop=4)

print('Output #7:', len(graph_routesAC4.path_list))

##############################################################################################################

size = graph_routesAC.shortest_path()
print('Output #8:', size)

##############################################################################################################

graph_routesBB = Graph()
graph_routesBB.build_graph(list_routes)
graph_routesBB.path_list = graph_routesBB.build_path_list('B', 'B')

size = graph_routesBB.shortest_path()
print('Output #9:', size)

##############################################################################################################

graph_routesCC = Graph()
graph_routesCC.build_graph(list_routes)
graph_routesCC.path_list = graph_routesCC.build_path_list('C', 'C', max_distance=30)

size = graph_routesCC.number_routes()

print('Output #10:', size)