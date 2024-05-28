from setuptools import setup



with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

setup(name='gene_synthesis',
      version='0.1',
      description='gene synthesis design',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
      ],
      keywords=['gene synthesis', 'gene cloning', 'PCR'],
      url='https://github.com/shiqiang-lin/gene-synthesis',
      author='Shiqiang Lin',
      author_email='linshiqiang@fafu.edu.cn',
      license='MIT',
      packages=['gene_synthesis'],
      scripts=['bin/gene_synthesis'],
      install_requires=['biopython','matplotlib'],
      include_package_data=True,
      zip_safe=False)


