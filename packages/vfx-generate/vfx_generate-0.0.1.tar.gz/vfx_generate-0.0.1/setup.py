from setuptools import setup, find_packages

setup(
    name='vfx_generate',
    version='0.0.1',
    author='yuikawaguchi',
    author_email='s2222011@stu.musashino-u.ac.jp',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KawaguchiYui',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas',
        'numpy',
        'Pillow',
    ],
    python_requires='>=3.6',
)