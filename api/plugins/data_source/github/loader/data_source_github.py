from core.SOK.services.api import ParseDataBase
from core.SOK.services.model import Graph,Node,Edge
from github import Github

class DataSourceGithub(ParseDataBase):


    def __init__(self: str):
        self.github_token = "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"
        self.repo = "BookingAppTeam18/IKS"
        self.account = ""

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
        commits_list = [{"sha": commit.sha, "author": commit.author.login, "date": commit.commit.author.date, "message": commit.commit.message, "parents": [p.sha for p in commit.parents]} for commit in commits]
        print("loading data ...")
        
        print("making graph ...")
        graph = Graph()
        commit_nodes = {} 
        for commit_data in commits_list:
            sha = commit_data["sha"]
            author = commit_data["author"]
            date = commit_data["date"]
            message = commit_data["message"]

            # Kreirajte cvor za svaki commit
            node = Node(sha, {"author": author, "date": date, "message":message})
            graph.nodes[sha] = node
            commit_nodes[sha] = node

        # Dodajte grane na osnovu roditelja svakog commita
        for commit_data in commits_list:
            sha = commit_data["sha"]
            parents = commit_data["parents"]
            for parent_sha in parents:
                # Create an edge from parent commit to current commit
                edge = Edge(parent_sha, sha)
                graph.edges.append(edge)
        
        print("Number of nodes:", len(graph.nodes))

        return graph

    def __str__(self):
        return "load_github " + str(type(self))

if __name__ == "__main__":
    data_source = DataSourceGithub()
    graph = data_source.parse_data()
    print(graph)