from setuptools import setup, find_packages
import pathlib

# Read the content of README.md for long description
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='NetHyTech-DeepTTS',
    version='0.1',
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@example.com',
    description='A Python package for text-to-speech conversion using DeepAI API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'playsound',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'NetHyTech-DeepTTS = my_package.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
