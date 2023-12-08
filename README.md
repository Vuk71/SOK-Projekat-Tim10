# Projekat iz SOK-a - TIM 10

## Studenti

| Indeks | Ime i prezime |
| ------ | ------ |
| SV6/2021 | Jelena Adamović |
| SV19/2021 | Marija Živanović |
| SV52/2021 | Vuk Dimitrov |
| SV57/2021 | Katarina Krstin |
| SV76/2020 | Jovan Vučković |

## To start the Django app

venv\Scripts\activate
cd graph_explorer
python manage.py runserver

## To start test console app

1. install venv in projekat folder (python -m venv venv)
2. activate venv windows->(venv/scripts/activate)
3. install core,plugins
    3.1 position at _platform->(python setup.py install)
    3.2 position at api.plugins.data_source.github->(python setup.py install)
    3.3 position at api.plugins.visualizer.basic->(python setup.py install)
4. run graph_main
5. expected result :

load_github <class 'loader.data_source_github.DataSourceGithub'>
visualize_basic <class 'visualizer.basic_visualizer.VisualizeBasic'>
NODOVI
{'2': <core.SOK.services.model.Node object at 0x000001D45E8F61B0>, '3': <core.SOK.services.model.Node object at 0x000001D45E8F6090>}
GRNCICE
[<core.SOK.services.model.Edge object at 0x000001D4606FF9B0>]
dobar pocetak

