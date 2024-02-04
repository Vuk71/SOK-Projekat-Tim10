import subprocess
import sys

def uninstall_packages(packages):
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', package])
            print(f"Izbrisan paket: {package}")
        except subprocess.CalledProcessError as e:
            print(f"Greška prilikom brisanja paketa {package}: {e}")

if __name__ == "__main__":
    # Definicija niza paketa za deinstalaciju
    packages_to_uninstall = [
        "core",
        "basic-visualizer",
        "detailed-visualizer",
        "load-github",
        "Django",
        "asgiref",
        "sqlparse",
        "tzdata",
        "setuptools"
    ]

    # Pozivanje funkcije za deinstalaciju paketa
    uninstall_packages(packages_to_uninstall)