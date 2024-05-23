from setuptools import setup, find_packages

setup(
    name='season_detector',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Pillow',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'season_detector=season_detector.app:app.run',
        ],
    },
    author='soei',
    author_email='s2222004@stu.musashino-u.ac.jp',
    description='A web app to detect the season based on an image\'s RGB values.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/S0UEI/season_detector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
