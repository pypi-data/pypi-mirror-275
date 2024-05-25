import setuptools
with open("README.md","r",encoding="utf-8")as fh:
    long_descripion = fh.read()
setuptools.setup(
    name="nanika",
    version="0.1.1",
    author="yui sugawara",
    author_email="s2222049@stu.musashino-u.ac.jp",
    description="nanika",
    long_description=long_descripion,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license = 'MIT',
    package_dir={"":"src"},
    py_modules=['nanika'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points={
        'console_scripts':[
            'nanika=nanika:main'
            ]
    }
)