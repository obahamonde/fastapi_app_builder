from setuptools import setup, find_packages

LONG_DESCRIPTION = """# FastAPI AppBuilder

This project is intended to speed up development of applications by providing an automated schema-driven development environment with a soft learning curve and great DX, currently it extends the Swagger UI with an application that supports database schemas and API endpoints autogeneration from the schema.prisma file, which can also be edited from the web App, more features like monitoring, authentication and security coming soon."""


setup(
    name='fastapi_appbuilder',
    version='0.0.1',
    description='Opinionated FastAPI AppBuilder',
    author="Oscar Bahamonde",
    author_email="oscar.bahamonde@hatarini.com",
    url="https://smartpro.solutions",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-multipart",
        "boto3",
        "prisma",
        "pydantic[email]"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
    maintainer="Oscar Bahamonde",
    maintainer_email="oscar.bahamonde@hatarini.com",
    keywords=["fastapi", "django", "template", "appbuilder","crud", "prisma", "boto3", "s3", "aws", "cloud", "sql", "database", "orm", "api", "rest", "graphql", "async", "asyncio", "asynchronous", "python", "python3", "python3.6", "python3.7", "python3.8", "python3.9", "swagger","auto","documented","admin","dashboard","template","boilerplate","cookiecutter"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    zip_safe=False,
)

