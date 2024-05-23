from setuptools import setup, find_packages

with open('./README.md', 'r') as file :
    long_description = file.read()
AUTHOR_USER_NAME = 'HarishKumarSedu'
AUTHOR_EMAIL = 'harishkumarsedu@gmail.com'
REPO_NAME = 'matrix'
setup(
    name=f'IvmDriver',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version='0.0.2',
    # py_modules=['src'],
    # description=[ 'text/markdown','text/x-rst'],
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    long_description_content_type=['text/plain', 'text/x-rst', 'text/markdown'],
    long_description=long_description,
    packages=find_packages(),
    package_data={'': ['*.json','*.py']},
    include_package_data=True,
    include_dirs=['IvmDriver'],

    
    
)