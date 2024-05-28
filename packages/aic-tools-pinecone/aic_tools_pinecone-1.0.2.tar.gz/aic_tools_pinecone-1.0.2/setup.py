from setuptools import setup, find_packages

# Function to read the contents of the requirements file
def read_requirements():
    with open('requirements.txt', 'r') as req:
        # Exclude any comments or empty lines
        return [line.strip() for line in req if line.strip() and not line.startswith('#')]

# Call the function and store the requirements list
install_requires = read_requirements()

setup(
    name='aic_tools_pinecone',
    version='1.0.2',
    packages=find_packages(),
    description='Pinecone tools for AI Characters',
    long_description_content_type='text/markdown',
    author='Viacheslav Kovalevskyi',
    author_email='viacheslav@kovalevskyi.com',
    license='MIT',
    install_requires=install_requires
)