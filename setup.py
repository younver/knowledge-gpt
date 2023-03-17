import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knowledgegpt",
    version="0.0.3b",
    author="Eren Akbulut, Kaan Ozbudak",
    author_email="erenakbulutwork@gmail.com, kaanozbudakk@gmail.com",
    description="A package for extracting and querying knowledge using GPT models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geeks-of-data/knowled-gpt",
    packages=["knowledgegpt", "knowledgegpt.extractors", "knowledgegpt.utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fastapi",
        "uvicorn",
        "pandas",
        "numpy",
        "scikit-learn",
        "transformers",
        "python-docx",
        "pdfminer.six",
        "beautifulsoup4",
        "requests",
        "gdown",
        "pymongo",
        "openai",
        "spacy",
        "sentence-transformers",
        "yt_dlp",
        "tiktoken",
        "pydub",
        "PyPDF2",
        "python-pptx",
        "faiss-cpu",
    ],
    python_requires=">=3.7",
)
