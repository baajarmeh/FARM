from io import open

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    parsed_requirements = f.read().splitlines()
# remove blank lines and comments
parsed_requirements = [
    x.strip()
    for x in parsed_requirements
    if ((x.strip()[0] != "#") and (len(x.strip()) > 3) and "-e git://" not in x)
]

parsed_requirements.append('transformers @ git+https://github.com/huggingface/transformers.git@90b7df444fc30d5f476e5ab32d1f89340998a28d#egg=transformers@v2.3.0#egg=transformers')

setup(
    name="farm",
    version="0.3.2",
    author="Malte Pietsch, Timo Moeller, Branden Chan, Tanay Soni, Huggingface Team Authors, Google AI Language Team Authors, Open AI team Authors",
    author_email="malte.pietsch@deepset.ai",
    description="Toolkit for finetuning and evaluating transformer based language models",
    long_description=open("readme.rst", "r", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
    keywords="BERT NLP deep learning language-model transformer qa question-answering transfer-learning",
    license="Apache",
    url="https://gitlab.com/deepset-ai/ml/lm/farm",
    download_url="https://github.com/deepset-ai/FARM/archive/0.3.2.tar.gz",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=parsed_requirements,
    python_requires=">=3.5.0",
    tests_require=["pytest"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
