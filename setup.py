from setuptools import setup, find_packages

setup(
    name="q2-krona",
    version='1.0.1',
    packages=find_packages(),
    author="Kaan Büyükaltay",
    author_email="kaanb93@gmail.com",
    url="https://github.com/kaanb93/q2-krona",
    license="",
    description="Generate Krona plots from feature tables",
    entry_points={
        "qiime2.plugins":
        ["q2-krona=q2_krona.plugin_setup:plugin"]
    },
    zip_safe=False,
    package_data={'q2_krona': ['citations.bib']}
)
