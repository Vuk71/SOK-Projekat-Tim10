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
        self.username = "betty_foxterrier"
        self.password = "bettykerety"
        self.profile = "betty_foxterrier"
        self.width = 5
        self.depth = 1

    def set_profile(self, profile):
        self.profile = profile

    def set_width(self, width):
        self.width = width

    def identifier(self):
        return "Instagram Data Source"

    def name(self):
        return "Load from instagram"

    def parse_data(self) -> Graph:
        ig = instaloader.Instaloader()
        ig.login(self.username, self.password)
        profile = instaloader.Profile.from_username(ig.context, self.profile)

        graph = Graph()

        profile_node = Node(id=profile.username, data={"private": profile.is_private, "followers": profile.followers,
                                                       "followees": profile.followees})
        graph.nodes[profile_node.id] = profile_node

        # Add profile's followees and their followees to the graph
        for followee in islice(profile.get_followees(), self.width):
            followee_node = Node(id=followee.username,
                                 data={"private": followee.is_private, "followers": followee.followers,
                                       "followees": followee.followees})
            graph.nodes[followee_node.id] = followee_node
            graph.edges.append(Edge(source=self.username, target=followee.username, name="following"))

            # Handle rate limit
            while True:
                try:
                    for followee_followee in islice(followee.get_followers(), self.width):
                        followee_followee_node = Node(id=followee_followee.username,
                                                      data={"private": followee_followee.is_private,
                                                            "followers": followee_followee.followers,
                                                            "followees": followee_followee.followees})
                        graph.nodes[followee_followee_node.id] = followee_followee_node
                        graph.edges.append(Edge(source=followee.username, target=followee_followee.username,
                                                name="following"))
                    break  # Ako je zahtjev uspješno izvršen, prekidamo petlju
                except instaloader.HTTPException as e:
                    if e.msg.startswith('HTTP error "429'):
                        print("Premašen rate limit. Čekamo {} sekundi...".format(self.rate_limit_wait_time))
                        time.sleep(self.rate_limit_wait_time)
                    else:
                        raise  # Ukoliko je greška drugačija od rate limite, izuzetak se ponovo podiže

        return graph

    def __str__(self):
        return "load_instagram " + str(type(self))


if __name__=="__main__":
    data_source = DataSourceInstagram()
    graph = data_source.parse_data()
    print(graph)