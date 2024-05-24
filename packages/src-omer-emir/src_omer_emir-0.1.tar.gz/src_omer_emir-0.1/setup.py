from setuptools import setup, find_packages

setup(
 name='src_omer_emir',
 version='0.1',
 author="Ömer Faruk Dişlitaş",
 author_email="omerfaruk.dislitas@stu.fsm.edu.tr",
 description="A comprehensive Python library for data preprocessing tasks Omer Faruk Dislitas ,Emir Kaan Ogsarim",
 packages=find_packages(),
install_requires=[  # Bağımlılıklar
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
 python_requires='>=3.6',
)