from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
        name="librds", 
        version="1.3.6",
        author="kuba201",
        description='RDS Group Generator',
        long_description=readme,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        url="https://flerken.zapto.org:1115/kuba/librds",
        install_requires=[],
        
        keywords=['radiodatasystem','rds'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Telecommunications Industry",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.10",
            "Development Status :: 4 - Beta"
        ]
)