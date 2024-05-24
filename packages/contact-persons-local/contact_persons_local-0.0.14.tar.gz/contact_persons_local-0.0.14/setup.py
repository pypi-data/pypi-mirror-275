import setuptools
PACKAGE_NAME = "contact-persons-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.14',  # update only the minor version each time # https://pypi.org/project/contact-persons-local
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles contact-person-local Python",
    long_description="",
    long_description_content_type='text/markdown',
    url="https://github.com/circles",  # https://pypi.org/project/contact-person-local
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    # TODO: Update which packages to include with this package
    install_requires=[
        'PyMySQL>=1.0.2',
        'pytest>=7.4.0',
        'mysql-connector>=2.2.9',
        'logzio-python-handler>= 4.1.0',
        'person-local>=0.0.53',
        'python-sdk-remote>=0.0.93',
        'language-remote>=0.0.17',
        'people-local>=0.0.12'
    ],
)
