import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="celltk",
    version="0.4.0",
    author="Stevan Jeknic",
    author_email="sjeknic@stanford.edu",
    description="A tool kit for working with large amounts of live-cell microscopy data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjeknic/CellTK",
    project_urls={
        "Bug Tracker": "https://github.com/sjeknic/CellTK/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages={"celltk", "celltk.utils", "celltk.core",
              "celltk.external.misic",
              "celltk.external.kit_sch_ge", "celltk.external.kit_sch_ge.tracker"},
    package_data={"celltk.external.misic": ["*.h5"]},
    include_package_data=True,
    install_requires=[
        'setuptools>=41.2.0',
        'tensorflow>=2.7.0,<2.9.0',
        'numpy>=1.20',
        'scipy>=1.6.3',
        'scikit_learn>=1.0.1',
        'scikit_image>=0.19.1',
        'matplotlib>=3.4.1',
        'plotly>=5.6.0',
        'pandas>=1.3.1',
        'cvxopt~=1.2.7',
        'gurobipy>=9.5.0',
        'h5py>=3.6.0',
        'imageio>=2.13.0',
        'mahotas>=1.4.5',
        'napari>=0.4.12',
        'PyYAML>=6.0',
        'SimpleITK>=2.1.1',
        'tifffile>=2021.11.2',
        'Bottleneck>=1.3.2',
        'btrack>=0.4.2',
        'colorcet~=3.0.0',
        'umap-learn>=0.5.3',
        'hdbscan~=0.8.28',
        'seaborn~=0.11.2'
    ],
    python_requires=">=3.8",
)