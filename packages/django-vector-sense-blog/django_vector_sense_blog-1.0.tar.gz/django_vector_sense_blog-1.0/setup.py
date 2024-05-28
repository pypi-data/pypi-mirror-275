import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-vector-sense-blog",
    version="1.0",
    author="Malaika",
    author_email="malaikaseher5@gmail.com",
    description="Geocoder Vector Sense",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/your_username/django_blog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.5',
    include_package_data=True,
)
