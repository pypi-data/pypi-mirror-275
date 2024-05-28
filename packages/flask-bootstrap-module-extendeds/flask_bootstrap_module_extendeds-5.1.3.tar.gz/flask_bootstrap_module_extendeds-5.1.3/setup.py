from setuptools import setup, find_packages

setup(
    name="flask_bootstrap_module_extendeds",
    version="5.1.3",
    author="Dex",
    author_email="censored@gmail.com",
    description="Flask bootstrap-library EXTENDED",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/my_library",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['static/**/*', 'templates/**/*']},  # Включить все содержимое папок static и templates и их подпапок
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
