import subprocess

def lay_egs(directory):
    subprocess.run(["pip", "install", directory])

def run_server(django_project):
    subprocess.run(["python", f"{django_project}/manage.py", "makemigrations"])
    subprocess.run(["python", f"{django_project}/manage.py", "migrate"])
    subprocess.run(["python", f"{django_project}/manage.py", "runserver"])



if __name__ == "__main__":
    lay_egs("./_platform")
    lay_egs("./api/plugins/data_source/instagram")
    lay_egs("./api/plugins/data_source/github")
    lay_egs("./api/plugins/visualizer/basic")
    lay_egs("./api/plugins/visualizer/detailed")
    subprocess.run(["pip", "install", "setuptools"])
    subprocess.run(["pip", "install", "django"])
    subprocess.run(["pip", "install", "PyGithub"])
    subprocess.run(["pip", "install", "instaloader"])