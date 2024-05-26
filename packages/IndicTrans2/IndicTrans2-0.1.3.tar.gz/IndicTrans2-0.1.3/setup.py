from setuptools import setup, find_packages

setup(
    name='IndicTrans2',
    version='0.1.3',
    description='Indic NLP package',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='AI4Bharat',
    author_email='AI4Bharat@gmail.com',
    url='https://github.com/AI4Bharat/IndicTrans2/',
    packages=find_packages(include=['inference', 'baseline_eval', 'model_configs', 'huggingface_interface']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'torch>=1.6.0',
        'fairseq>=0.10.2',
        'transformers==4.28.1',
        'codecs',
        'urduhack[tf]',
        'nltk',
        'sacremoses',
        'indic-nlp-library',
        'mosestokenizer',
        'sacrebleu==2.3.1',
        'ctranslate2==3.9.0',
        'gradio',
        'sentencepiece',
        'regex',
        'pandas',
        'mock'
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'black'
        ]
    },
    include_package_data=True,
    license='MIT',
    project_urls={
        'Documentation': 'https://ai4bharat.iitm.ac.in/indic-trans2/docs',
        'Source': 'https://github.com/AI4Bharat/IndicTrans2/',
        'Issues': 'https://github.com/AI4Bharat/IndicTrans2/issues',
    },
    entry_points={
        'console_scripts': [
            'setup.sh=setup:main'
            # Add any command line scripts here
        ],
    },
)
