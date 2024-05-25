from setuptools import setup, find_packages

setup(
    name='ERTool',
    version='0.2.9',
    author='Tongyue Shi',
    author_email='tyshipku@gmail.com',
    packages=find_packages(),
    description='ERTool: A Python Package for Efficient Implementation of the Evidential Reasoning Approach for Multi-Source Evidence Fusion',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "seaborn",
        # 其他依赖
    ],
    classifiers=[
        # 分类器
    ],
)
