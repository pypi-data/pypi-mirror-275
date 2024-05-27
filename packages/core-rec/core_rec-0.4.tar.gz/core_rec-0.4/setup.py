# from setuptools import setup, find_packages

# with open('README.md', 'r') as f:
#     long_description = f.read()

# setup(
#     name='vishgraphs',
#     version='0.2',
#     packages=find_packages(),
#     install_requires=[
#         'numpy',
#         'matplotlib',
#         'networkx',
#     ],
#     long_description=long_description,
#     long_description_content_type='text/markdown',  # Assuming your README is in Markdown format
# )

from setuptools import setup, find_packages

setup(
    name='core_rec',  # Replace with your library's name
    version='0.4',  # Start with a low version for initial releases
    description='A Python library for graph-related operations',  # Short description
    long_description='''
        vishgraphs is a Python library that provides functionalities for working with graphs.
        It includes features like
        making bipartite graphs, random graphs, find trending nodes etc
        and corerec is engine supports exclusive graphtransformer
    ''',
    url='https://github.com/your-username/vishesh9131',  # Replace with your project's URL (optional)
    author='Vishesh Yadav',
    author_email='sciencely98@gmail.com',
    packages=find_packages(exclude=['tests.*', '*.tests', '*.test']),  # Exclude test directories
    install_requires=[  # List any external dependencies your library needs
         'numpy',
        'matplotlib',
        'networkx',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
