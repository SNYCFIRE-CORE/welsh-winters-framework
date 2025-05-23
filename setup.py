"""
Setup configuration for Welsh-Winters Balance Framework
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="welsh-winters-framework",
    version="1.0.0",
    author="SYNCFIRE Team",
    description="A quantitative framework for measuring and preventing AI hallucination through balanced human-AI interaction patterns",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SNYCFIRE-CORE/welsh-winters-framework",
    project_urls={
        "Bug Tracker": "https://github.com/SNYCFIRE-CORE/welsh-winters-framework/issues",
        "Documentation": "https://github.com/SNYCFIRE-CORE/welsh-winters-framework/tree/main/docs",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - pure Python implementation
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "welsh-winters=welsh_winters.cli:main",
        ],
    },
    keywords="ai, hallucination, nlp, human-ai-interaction, conversation-analysis, balance-metrics",
)