from setuptools import setup, find_packages

setup(
    name="bats-telegram-project",
    version="0.1",
    packages=find_packages(where="backend"),  # Look for packages in the "backend" folder
    package_dir={"": "backend"},  # Specify that packages are in the "backend" folder
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "psycopg2-binary",
        "pydantic",
        "python-dotenv",
        "websockets",
    ],
)