from setuptools import find_packages, setup

setup(
    name="pandalibs",
    packages=find_packages(include=["pandalibs"]),
    package_data={
        "pandalibs": ["config/*.yaml"],
    },
    version="0.1.6",
    description="My personal library.",
    author="nightpanda2810",
    install_requires=["pyyaml"],
    setup_requires=[],
    tests_require=[],
    test_suite="tests",
)

# How to run:
# python .\setup.py bdist_wheel
# python setup.py sdist bdist_wheel
# twine upload dist/*
# Paste in the below API
# pypi-AgEIcHlwaS5vcmcCJGVkZTY5NWVmLWY1ZjMtNGQ0Mi04ZWE1LTNkMjZmNjVlYTE3ZQACKlszLCIzNGU3NTAwMi1lYjU4LTQwYWQtYWRhZi00ZGRmNzZhNTM5ZTQiXQAABiAri09IgwSekjjUASSzvISM5tlG7pz-KGgAvtte9hGUwg
