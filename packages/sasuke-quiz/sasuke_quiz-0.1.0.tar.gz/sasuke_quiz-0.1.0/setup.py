from setuptools import setup, find_packages

setup(
    name="sasuke_quiz",
    version="0.1.0",
    author="sasukekun",
    author_email="s2222070@stu.musashino-u.ac.jp",
    description="sasukeに関する簡単な問題を作りました",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nousouhiroyuki/quiz_app",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',   
    entry_points={
        'console_scripts': [
            'quiz_app=quiz_app.main:main',
        ],
    },
)