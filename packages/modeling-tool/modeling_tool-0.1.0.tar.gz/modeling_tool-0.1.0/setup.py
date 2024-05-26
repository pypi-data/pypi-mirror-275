from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="the extension of sklearn to help the your modeling code becomes more concise with common useful tool for modeling",
    name="modeling_tool",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    install_requires=["scikit-learn"],

    # example
    # install_requires=['pandas>=1.0',
    # 'scipy==1.1',
    # 'matplotlib>=2.2.1,<3'],
    

)