from setuptools import setup, find_packages

try:
    import pypandoc

    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()


setup(
    name="latex_formatter",
    version="1.2.4",
    long_description=long_description,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ujson >= 5.8.0",
        # 你的依赖包列表，例如：
        # "matplotlib >= 2.2.0"
    ],
)
