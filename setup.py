from setuptools import setup
import glob

setup(
    name="KubeDiagrams",
    version="0.1.0",
    author="Philippe Merle",
    author_email="philippe.merle@inria.fr",
    maintainer="Philippe Merle",
    maintainer_email="philippe.merle@inria.fr",
    url="https://github.com/philippemerle/KubeDiagrams",
    description="Generate Kubernetes architecture diagrams from Kubernetes manifest files, kustomization files, Helm charts, and actual cluster state",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
    ],
    keywords = "kubernetes architecture diagrams",
    python_requires=">=3.9",
    install_requires=[
        "PyYAML",
        "diagrams",
    ],
    scripts=[
        "bin/kube-diagrams",
        "bin/helm-diagrams",
    ],
    data_files=[
        ("bin", ["bin/kube-diagrams.yaml"]),
        ("bin/icons", glob.glob("bin/icons/*")),
    ],
    project_urls={
        "Issues": "https://github.com/philippemerle/KubeDiagrams/issues",
        "Discussions": "https://github.com/philippemerle/KubeDiagrams/discussions",
        "Wiki": "https://github.com/philippemerle/KubeDiagrams/wiki",
    },
)
