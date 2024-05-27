from setuptools import setup, find_packages

setup(
    name='adonamaria_compute_stats',  # Change to the name of your package
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'compute_stats=compute_stats:main',  # Assuming your main script is named compute_stats.py
        ],
    },
)
