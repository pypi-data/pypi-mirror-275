from setuptools import setup, find_packages

setup(
    name='string-utils-practice',  # パッケージ名
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 依存関係があればここに記述
    ],
    author='kazuki15',
    author_email='s2222008@stu.musashino-u.ac.jp',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Kzkyo/string-utils',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)

