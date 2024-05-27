from setuptools import setup, find_packages

setup(
    name="fastybird_modules_metadata",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # 列出你的依赖包，例如：
        # 'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

