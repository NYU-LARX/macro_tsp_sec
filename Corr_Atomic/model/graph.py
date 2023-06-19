

class Graph():
    def __init__(self, graph_dict= None) -> None:
          
        """ 
        Transportation network: no self-loop
        inputs:
            graph_dictionary, if none, then initialize with empty graph
        """
        from collections import OrderedDict
        if graph_dict == None:
            graph_dict = OrderedDict()
        self.__graph_dict = OrderedDict(graph_dict)
        if self.__is_with_loop():
            raise ValueError("The graph are supposed to be without self-loop please recheck the input data!")
    
    def __is_with_loop(self) -> bool:
        
        return false
        