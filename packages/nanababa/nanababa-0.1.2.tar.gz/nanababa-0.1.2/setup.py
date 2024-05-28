from setuptools import setup, find_packages


list_of_dependencies = []
# with open('./.dist_management/config/requirements.txt', 'r') as fh:
#     data = fh.read()
#     list_of_dependencies = data.split('\n')


setup(
    name='nanababa',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=list_of_dependencies,
    entry_points={
        'console_scripts': [
            'your_command=your_package.module:function',
        ],
    },
    author='Marcus',
    author_email='marcusongkiansiong@gmail.com',
    description='Testing my distribution management script (upload)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)