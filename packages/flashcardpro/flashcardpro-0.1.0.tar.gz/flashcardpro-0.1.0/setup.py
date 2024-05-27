import setuptools

setuptools.setup(
    name="flashcardpro",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A flashcard creation and learning application",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fuhma0q0/flashcardpro",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.0,<4.0",
        "djangorestframework",
        "django-cors-headers",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'flashcardpro=flashcardpro.__main__:main',
        ],
    },
)
