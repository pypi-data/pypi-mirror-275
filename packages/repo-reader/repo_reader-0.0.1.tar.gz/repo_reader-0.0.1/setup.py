from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='repo_reader',
    version='0.0.1',
    description='A package for reading GitHub repos and converting them for LLM processing',
    author='Sam Witteveen',
    author_email='sam@samwitteveen.com',
    url='https://github.com/samwit/repo_reader',
    # package_dir={"": "src"},  # Optional: where the package lives in the repo
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'tiktoken',
    ],
    extras_require={
        'dev': [
            'pytest',
            'twine',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)