from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    name = 'YourUniquePackageNameRu', 
    
    version = '0.1.0',
    
    description = 'An NLP python package for computing Boilerplate score and many other text features.',
     
    py_modules = ["TheModuleName"],
    
    package_dir = {'':'src'},
    
    author = 'AuthorName',
    author_email = 'xyz123@something.com',
    
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    url='https://github.com/jinhangjiang/morethansentiments',
    
    include_package_data=True,
    
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    
    install_requires = [
        'pandas ~= 1.2.4'
    ],
    keywords = ['Text Mining', 'Data Science'],
    
)
