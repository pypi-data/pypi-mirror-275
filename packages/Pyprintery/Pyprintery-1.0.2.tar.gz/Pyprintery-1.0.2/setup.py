from setuptools import setup, find_packages
setup(
    name="Pyprintery",
    version="1.0.2",
    packages=find_packages(),
    description=("Simulates a game window built by the terminal console, Simple word games can be developed, "+
                "Third-party libraries that are more entertaining than useful, Suitable for Python beginners"),
    package_data={
        "Pyprinter": [r"Pyprinter/Myprinter.py", r"Pyprinter/*"]
    },
    long_description=open("README.txt", encoding="utf-8").read(),
    long_description_content_type="text/markdown"
)