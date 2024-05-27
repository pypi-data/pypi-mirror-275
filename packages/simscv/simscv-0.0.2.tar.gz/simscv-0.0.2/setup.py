import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="simscv",
    version="0.0.2",
    author="Kanra_Ishido",
    author_email="s2222002@stu.musashino-u.ac.jp",
    description="A simple csv reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kanra-Ishido/simscv",
    project_urls={
        "Bug Tracker": "https://github.com/Kanra-Ishido/simscv",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=["simscv"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        'numpy',
        'scikit-learn',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'simscv = simscv:main'
        ]
    }
)