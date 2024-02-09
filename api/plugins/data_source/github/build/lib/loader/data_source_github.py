from core.SOK.services.api import ParseDataBase
from core.SOK.services.model import Graph, Node, Edge
from github import Github

class DataSourceGithub(ParseDataBase):
    def __init__(self: str):
        self.github_token = "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"
        self.repo = "BookingAppTeam18/IKS"
        self.account = ""
        self.node_counter = 0  # Dodajemo brojač za čvorove

    def set_token(self, token):
        self.github_token = token

    def set_repo(self, repository):
        self.repo = repository

    def set_account(self, account):
        self.account = account

    def identifier(self):
        return "Github Data Source"

    def name(self):
        return "Load from github"

    def parse_data(self) -> Graph:
        g = Github(self.github_token)
        repo = g.get_repo(self.repo)
        commits = repo.get_commits()
        commits_list = [{"sha": commit.sha, "author": commit.author.login, "date": commit.commit.author.date, "parents": [p.sha for p in commit.parents]} for commit in commits]
        print("loading data ...")
        
        print("making graph ...")
        graph = Graph()

        for commit_data in commits_list:
            sha = commit_data["sha"]
            author = commit_data["author"]
            date = commit_data["date"]
            message = commit_data["message"]

            # Kreirajte čvor za svaki commit sa rednim brojem kao ID
            node = Node(self.node_counter, {"sha": sha, "author": author, "date": date})
            graph.nodes[self.node_counter] = node
            self.node_counter += 1  # Povećavamo brojač

        # Dodajemo grane na osnovu roditelja svakog commit-a
        for commit_data in commits_list:
            sha = commit_data["sha"]
            parents = commit_data["parents"]
            for parent_sha in parents:
                # Pronalazimo ID-jeve roditelja i deteta
                parent_id = [k for k, v in graph.nodes.items() if v.data["sha"] == parent_sha][0]
                child_id = [k for k, v in graph.nodes.items() if v.data["sha"] == sha][0]
                # Dodajemo granu sa izvorom i ciljem koji pokazuju na ID-jeve čvorova
                edge = Edge(parent_id, child_id)
                graph.edges.append(edge)
        
        return graph

    def __str__(self):
        return "load_github " + str(type(self))

if __name__ == "__main__":
    data_source = DataSourceGithub()
    graph = data_source.parse_data()
    print(graph)
