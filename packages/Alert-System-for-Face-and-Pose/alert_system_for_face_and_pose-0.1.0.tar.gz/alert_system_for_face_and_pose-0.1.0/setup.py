import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Alert_System_for_Face_and_Pose",
    version="0.1.0",
    author="yuta morimoto",
    author_email="s2222081@stu.musashino-u.ac.jp",
    description="Alert_System_for_Face_and_Pose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuta0726/Alert_System_for_Face_and_Pose",
    package_dir={'': 'src'},
    py_modules=['Alert_System'],
    packages=find_packages(where='src'),
    python_requires=">=3.12.3",
    entry_points = {
        'console_scripts': [
            'airpiano = airpiano:main'
        ]
    },
)
