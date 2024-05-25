from setuptools import setup


def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='comment_inspect',
    version='0.1',
    install_requires=[
        'python-magic-bin>=0.4.14',
    ],
    description='Parse comments from various programming languages',
    author='Faiz Alam',
    author_email='mohdfaizalam53@gmail.com',
    license='MIT',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=['comment_inspect', 'comment_inspect.parsers'],
    python_requires='>=3.7',
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "comment_inspect = comment_inspect.comment_inspect:main",
        ],
    },

)
