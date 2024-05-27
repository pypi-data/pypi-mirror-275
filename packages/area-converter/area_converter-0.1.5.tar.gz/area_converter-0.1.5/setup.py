import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='area_converter',
    version='0.1.5',
    author='Haruna Takada',
    description="A package that converts area to Tokyo Dome",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarunaTakada/area_converter",
    project_urls={
        "Bug Tracker": "https://github.com/HarunaTakada/area_converter",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['area_converter'],
    packages=setuptools.find_packages(where="src"),
    setup_requires=['wheel'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'area-converter=area_converter:main',
        ],
    }

)
