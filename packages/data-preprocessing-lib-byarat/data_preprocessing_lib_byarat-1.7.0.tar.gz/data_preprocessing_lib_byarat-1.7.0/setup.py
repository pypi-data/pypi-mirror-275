from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.call(['python', 'download_nltk_data.py'])

setup(
    name='data_preprocessing_lib_byarat',
    version='1.7.0',
    description='An easy peasy comprehensive library for data preprocessing tasks',
    author='Mehdi Miraç ARAT, Latif Şimşek',
    author_email='mehdimirac.arat@stu.fsm.edu.tr, latif.simsek@stu.fsm.edu.tr',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
        'beautifulsoup4',
        'contractions',
        'emoji',
        'pyspellchecker',
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': PostInstallCommand,
    },
)