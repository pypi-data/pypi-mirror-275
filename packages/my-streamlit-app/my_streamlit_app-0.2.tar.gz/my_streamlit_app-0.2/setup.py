from setuptools import setup, find_packages

setup(
    name='my_streamlit_app',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'streamlit'
    ],
    entry_points={
        'console_scripts': [
            'run-Chibalotte_Baseball_Predictor-app=Chibalotte_Baseball_Predictor_app.app:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


