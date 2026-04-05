from modelos.repositorios.repositorio_cientificos import RepositorioCientificos
from modelos.repositorios.repositorio_experimentos import RepositorioExperimentos

repo_miembros = None
repo_experimentos = None

def obtener_repositorio_cientificos():
    global repo_miembros
    if repo_miembros is None:
        repo_miembros = RepositorioCientificos()
    return repo_miembros

def obtener_repositorio_experimentos():
    global repo_experimentos
    if repo_experimentos is None:
        repo_experimentos = RepositorioExperimentos()
    return repo_experimentos
