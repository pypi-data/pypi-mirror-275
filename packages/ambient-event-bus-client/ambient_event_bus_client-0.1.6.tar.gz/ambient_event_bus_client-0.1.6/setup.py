from setuptools import setup, find_packages

setup(
    name="ambient_event_bus_client",
    version="0.1.6",
    description="A library to interact with the Ambient Labs Event Bus.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Jose Catarino",
    author_email="jose@ambientlabscomputing.com",
    url="https://github.com/ambientlabscomputing/ambient-event-bus-client",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "aiohttp",
        "websockets",
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
