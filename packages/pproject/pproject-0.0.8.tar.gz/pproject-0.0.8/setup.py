import setuptools
with open("README.md","r",encoding="utf-8")as fh:
    long_description=fh.read()
setuptools.setup(
    name="pproject",
    version="0.0.8",
    author="Sojiro4",
    author_email="s2122097@stu.musashino-u.ac.jp",
    description="Predicted price change for iphone in XX years",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sojiro4/pproject",
    project_urls={
    "Bug Tracker":"https://github.com/Sojiro4/pproject",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    py_modules=['pproject'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.11.3",
    entry_points={
        'console_scripts':[
            'pproject=pproject:main'
        ]
    },
)