from core.SOK.services.api import ParseDataBase
from core.SOK.services.model import Graph,Node,Edge
import instaloader
from itertools import islice
import time

#profile - starting point profile
#followee - profile that starting point profile follows

#profile object has username, num of followers, list of followers...
class DataSourceInstagram(ParseDataBase):


    def __init__(self: str):
        self.username = "jovanvuckovic2"
        self.password = "&ca#VPsN5d3szS"
        self.profile = "jovanvuckovic2"
        self.width = 5
        self.depth = 1

    def set_profile(self, profile):
        self.profile = profile

    def set_width(self, width):
        self.width = width

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def identifier(self):
        return "Instagram Data Source"

    def name(self):
        return "Load from instagram"

    def parse_data(self) -> Graph:
        ig = instaloader.Instaloader()
        ig.login(self.username, self.password)
        profile = instaloader.Profile.from_username(ig.context, self.profile)

        # dictionary to keep profile followees username as key and their followees (profiles) as value
        profile_followees = {}

        print("loading data: ")

        for followee in islice(profile.get_followees(), self.width):
            followee_followees = islice(followee.get_followers(), self.width)
            profile_followees[followee] = followee_followees

        # forming graph from data
        print("making graph: ")
        graph = Graph()
        profile_node = Node(id=profile.username, data={"private": profile.is_private, "followers": profile.followers,
                                                       "followees": profile.followees})
        graph.nodes[profile_node.id] = profile_node
        for followee, followee_followees in profile_followees.items():
            node = Node(id=followee.username, data={"private": followee.is_private, "followers": followee.followers,
                                                    "followees": followee.followees})
            graph.nodes[node.id] = node
            edge = Edge(source=self.username, target=followee.username, name="following")
            graph.edges.append(edge)
            for followee_followee in followee_followees:
                edge = Edge(source=followee.username, target=followee_followee.username, name="following")
                node = Node(id=followee_followee.username,
                            data={"private": followee_followee.is_private, "followers": followee_followee.followers,
                                  "followees": followee_followee.followees})
                graph.nodes[node.id] = node
                graph.edges.append(edge)

        return graph

    def __str__(self):
        return "load_instagram " + str(type(self))


if __name__=="__main__":
    data_source = DataSourceInstagram()
    graph = data_source.parse_data()
    print(graph)