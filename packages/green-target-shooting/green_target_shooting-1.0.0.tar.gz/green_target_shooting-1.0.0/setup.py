from setuptools import setup, find_packages

setup(
    name='green_target_shooting',
    version='1.0.0',
    description='Green Target Shooting game for Python',
    long_description='A simple shooting game built with Python and Tkinter.',
    author='Okayama',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='game tkinter shooting',
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    python_requires='>=3.9',
)
