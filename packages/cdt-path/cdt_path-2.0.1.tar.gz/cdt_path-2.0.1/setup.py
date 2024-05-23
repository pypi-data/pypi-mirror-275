from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="cdt_path",
    version='2.0.1',
    author="CaiShu",
    author_email="caiyi@mail.ustc.edu.cn",
    description="CDT for path-planning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license="MIT",
    # url="https://gitee.com/DerrickChiu/function_tool.git",
    packages=find_packages(),
    requires=[	'matplotlib',
				'triangle',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
