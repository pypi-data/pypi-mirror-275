from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.2.2'
DESCRIPTION = 'A Package for optimize models, transfer or copy files from one directory to other, use for nlp short word treatment, choosing optimal data for ML models, use for Image Scraping , use in timeseries problem to split the data into train and test','Deal with emojis and emoticons in nlp,word tokenize,token, get the list of Punctuation marks and English Pronouns too, can be used to read text files'
LONG_DESCRIPTION = 'A package to increase the accuracy of ML models, transfer or copy files from one directory to other,  gives you the best data for model training, works on text data also, short word treatment for NLP problems, can be used for Image Scraping also, use it to split the timeseries data into training and testing, deal with emojis and emoticons,word tokenizer,tokenize words,can be use to remove stop words too,Punctuations and get English Pronouns list too, use to read text files'

# Setting up
setup(
    name="optimal_data_selector",
    version=VERSION,
    author="Rohan Majumder",
    author_email="majumderrohan2001@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['transfer or copy files from one directory to other','get best data combination','read text files','text files','lock data combination','save data','English','Pronouns','Punctuations','English pronouns','Model training', 'optimise accuracy', 'lock data combination', 'gives best result', 'best data for ML models', 'works on text data also','short word treatment','Image Scraping','download images','Web Image Scraping','timeseries','splitting timeseries data into train and test','deal with emojis and emoticons','emoji','emojis','emoticon','emoticons','word tokenize','NLP','short words','short words treatment','get best accuracy','performence enhancing','best data','more accurate model building','word to token','tokenizer'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.12',
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: iOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)