from setuptools import setup, find_packages

setup(
    name='IndicTrans2',
    version='0.1.2',
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
        'transformers>=4.0.0',
        'codecs',
        'urduhack[tf]',
        'nltk',
        'sacremoses',
        'indic-nlp-library',
        'mosestokenizer'
    ],
    license='MIT',
    project_urls={
        'Documentation': 'https://ai4bharat.iitm.ac.in/indic-trans2/docs',
        'Source': 'https://github.com/AI4Bharat/IndicTrans2/',
        'Issues': 'https://github.com/AI4Bharat/IndicTrans2/issues',
    }
)
