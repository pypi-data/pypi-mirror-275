from setuptools import setup, find_packages

setup(
    name='crewai_logging_patch',
    version='0.2',
    author='theCyberTech',
    author_email='the_t3ch@pm.me',
    packages=find_packages(include=['logger_patch', 'logger_patch.*']),
    install_requires=[],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/theCyberTech/CrewAI_Logger_Patch"
)
