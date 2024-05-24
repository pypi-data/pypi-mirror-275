# setup.py

from setuptools import setup, find_packages

setup(
    name='Chibalotte_Baseball_Predictor_app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'streamlit',
        'glob'
    ],
    entry_points={
        'console_scripts': [
            'run-my-streamlit-app=my_streamlit_app.app:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

