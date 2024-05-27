from setuptools import setup, find_packages

setup(
    name='color-extractor',
    version='1.0.0',
    description='A Python package to extract main colors from images.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Mizuha Kojima",
    author_email="s2222076@stu.musashino-u.ac.jp",
    url="https://github.com/Mizu0927/extract_main_color",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
