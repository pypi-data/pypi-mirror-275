from setuptools import setup, find_packages

setup(
    name='custom_viz_lib',
    version='1.0.1',
    description='A customizable data visualization library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aso Okada',
    author_email='s2222083@stu.musashino-u.ac.jp',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'seaborn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)