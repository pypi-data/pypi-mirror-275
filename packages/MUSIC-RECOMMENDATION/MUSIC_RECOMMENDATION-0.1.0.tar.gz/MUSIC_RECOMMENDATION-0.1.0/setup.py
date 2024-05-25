from setuptools import setup, find_packages

setup(
    name='MUSIC_RECOMMENDATION',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'pandas',
        'scikit-learn',
        'spotipy',
        'gunicorn',
    ],
    entry_points={
        'console_scripts': [
            'your_project=your_project.app:main',
        ],
    },
    author='SayaMiyaji',
    author_email='s2222072@stu.musashino-u.ac.jp',
    description='A music recommendation system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sayamiyaji/MUSIC_RECOMMENDATION.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
