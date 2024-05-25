from setuptools import setup, find_packages

setup(
    name='topic_modeling_tool',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas',
    ],
    test_suite='tests',
    author='Takumi Maruyama',
    author_email='s2222095@stu.musashino-u.ac.jp',
    description='A simple topic modeling tool using LDA',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/topic_modeling_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
