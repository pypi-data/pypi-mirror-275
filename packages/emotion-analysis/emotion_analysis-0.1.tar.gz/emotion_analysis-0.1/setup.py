from setuptools import setup, find_packages

setup(
    name='emotion_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'beautifulsoup4',
        'emoji',
        'nltk',
        'wordcloud',
        'matplotlib',
        'seaborn',
        'transformers',
        'torch',
    ],
    author='Ahsan Tariq',
    author_email='ahsantariq0724@email.com',
    description='A package for emotion detection using transformers-based models.',
    url='https://github.com/yourusername/frnn_emotion_detection',
)
