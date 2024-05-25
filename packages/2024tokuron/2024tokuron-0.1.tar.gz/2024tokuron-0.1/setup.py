from setuptools import setup, find_packages

setup(
    name='2024tokuron',
    version='0.1',
    packages=find_packages(),
    py_modules=['2024tokuron'],  # モジュールを指定する
    install_requires=[
        'speechrecognition',
        'pydub'
    ],
    entry_points={
        'console_scripts': [
            '2024tokuron = 2024tokuron:main'
        ]
    },
    author='Your Name',
    author_email='your@email.com',
    description='Convert audio files to text using speech recognition',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/2024tokuron',
    license='MIT',
    keywords='audio text speech-recognition',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
