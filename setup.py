import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
        name='cogwatch',
        version='1.1.0',
        author='Rob Wagner',
        author_email='rob.wagner@outlook.com',
        license='License :: OSI Approved :: MIT License',
        description='Automatic hot-reloading for your discord.py command files.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/robertwayne/cogwatch',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3.9',
            'Operating System :: OS Independent',
            'Typing :: Typed',
            'Topic :: Communications :: Chat',
            'Intended Audience :: Developers',
            'Development Status :: 5 - Production/Stable',
        ],
        python_requires='>=3.8',
        install_requires=[
            'watchgod'
        ]
)
