from setuptools import setup, find_packages

setup(
    name='htmltestreport-ably',
    version='1.2.2',
    packages=find_packages(),
    package_data={'': ['templates/*.html']},
    include_package_data=True,
    install_requires=[
    ],
    author='AblyQA',
    author_email='ablyqa@gmail.com.com',
    description='Modified version of HtmlTestReport plugin',
    url='https://github.com/qa-inho-song/htmltestreport-ably',
)
