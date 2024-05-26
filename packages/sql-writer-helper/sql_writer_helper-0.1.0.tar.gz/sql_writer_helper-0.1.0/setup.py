from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="package the help you reduce redundancy in SQL code",
    name="sql_writer_helper",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    install_requires=["pandas",
        "os_toolkit>=0.1.1",
        "py_string_tool>=0.1.3",
        "python_wizard>=0.1.1"],

    # example
    # install_requires=['pandas>=1.0',
    # 'scipy==1.1',
    # 'matplotlib>=2.2.1,<3'],
    

)