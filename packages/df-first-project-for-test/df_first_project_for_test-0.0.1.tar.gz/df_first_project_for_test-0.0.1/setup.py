from setuptools import setup, find_packages

setup(
    name="df_first_project_for_test",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        # 在这里列出你的项目依赖的包，例如
        # 'requests',
        # 'numpy',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

