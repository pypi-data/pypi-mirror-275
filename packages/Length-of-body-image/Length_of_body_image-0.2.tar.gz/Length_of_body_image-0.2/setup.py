from setuptools import setup, find_packages

setup(
    name='Length_of_body_image',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'matplotlib',
    ],
    author='Akari Hosokawa',
    author_email='s2222057@stu.musashino-u.ac.jp',
    description='Package to measure length up and down at the waist',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hosson-aka/body.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)