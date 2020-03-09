from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    README = f.read()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

VERSION = '0.1.0'
DEPENDENCIES = []


setup(
    name='azure-cli-ext-keyvault-kek',
    version=VERSION,
    description='Azure Key Vault Key Encryption Key extension',
    long_description=README,
    license='MIT',
    author='Luke Carrier',
    author_email='luke.carrier@avadolearning.com',
    url='https://github.com/AVADOLearning/azure-cli-extensions',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    package_data={
        'azext_keyvault_kek': [
            'azext_metadata.json',
        ],
    },
    install_requires=DEPENDENCIES
)
