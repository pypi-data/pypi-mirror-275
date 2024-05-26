from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='picture2pixel',
    version='1.0.0',
    description='A Python library for converting images into FPGA-displayable pixel art.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gu0y1/picture2pixel',
    author='Chen Guoyi',
    author_email='guoyi@comp.nus.edu.sg',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'imageio',
        'Pillow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
