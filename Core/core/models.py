from django.db import models
from datetime import datetime


class Node:
    def __init__(self, identifier, edges, data={}):
        self.id = identifier
        self.edges = edges
        self.data = data


    def __str__(self):
        ret = ""
        for key in self.data:
            ret += str(key) + ": " + str(self.data[key]) + "\n"
        return ret


class Edge:
    def __init__(self, first_node, second_node, data=None):
        self.first_node = first_node
        self.second_node = second_node
        self.data = data


    def __str__(self) -> str:
        return str(self.first_node) + " - " + str(self.second_node)


class Graph:
    def __init__(self, data={}):
        self.data = data
        self.counter = 0


    def add_node(self, node):
        self.data[node.id] = node
        self.counter += 1


    def __str__(self):
        ret = ""
        for node_id in self.data:
            for edge in self.data[node_id].edges:
                ret += str(edge) + "\n"
            ret += "----------------------------------\n"
        return ret


    def search(self, term):
        g = Graph()

        for node_id in self.data:
            node = self.data[node_id]
            if self.search_check(term, node):
                g.data[node_id] = node

        for node_id in g.data:
            node = g.data[node_id]
            node.edges = list(
                filter(lambda x: x.second_node in g.data, node.edges)) # filtering edges that are not in a filtered subset of our graph

        return g


    def search_check(self, term, node):
        for key in node.data:
            if term in str(node.data[key]):
                return True
        return False


    def filter(self, query):
        tokens = query.strip().split(" ")

        if len(tokens) < 3 or len(tokens) > 4:
            raise ValueError("Query ima los broj delova!")

        attr = tokens[0]
        operator = tokens[1]
        value = tokens[2]

        if self.data == {}:
            return Graph()

        first_node = None
        for key in self.data:
            first_node = self.data[key]
            break

        print(attr, first_node.data)
        if attr not in first_node.data:
            raise ValueError("Nema tog atributa.")

        type_of_attr = type(first_node.data[attr])
        print(type_of_attr)

        value = self.filter_check_value_type(type_of_attr, value, tokens)

        g = Graph()

        for node_id in self.data:
            node = self.data[node_id]
            if self.filter_check(attr, operator, value, node):
                g.data[node_id] = node

        for node_id in g.data:
            node = g.data[node_id]
            node.edges = list(
                filter(lambda x: x.second_node in g.data, node.edges)) # filtering edges that are not in a filtered subset of our graph

        return g


    def filter_check(self, key, operator, value, node):
        if operator == "==":
            return True if node.data[key] == value else False
        elif operator == ">":
            return True if node.data[key] > value else False
        elif operator == ">=":
            return True if node.data[key] >= value else False
        elif operator == "<":
            return True if node.data[key] < value else False
        elif operator == "<=":
            return True if node.data[key] <= value else False
        elif operator == "!=":
            return True if node.data[key] != value else False
        else:
            raise ValueError("Los operator!")


    def filter_check_value_type(self, type_of_attr, value, tokens):
        if type_of_attr == float or type_of_attr == int:
            if not is_number(value):
                raise ValueError("Value ne odgovara tipu broja!")
            value = float(value)

        elif type_of_attr == datetime:
            if len(tokens) != 4:
                raise ValueError("Los broj delova querija za polje tipa datum!")
            time_part = tokens[3]
            value = datetime.strptime(value + " " + time_part, "%Y-%m-%d %H:%M:%S")

        return value


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
