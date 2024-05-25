from setuptools import setup, find_packages

setup(
    name='promising_stocks',
    version='0.1.4',
    author='ryotatakasaki226',
    author_email='s2222022@stu.musashino-u.ac.jp',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ryotatakasaki226/pr_st.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
