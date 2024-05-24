from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='online_scheduler',
    version='0.1',
    description='Awesome library',
    url='https://github.com/2222041',
    author='2222041',
    author_email='s2222041@stu.musashino-u.ac.jp',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "online_scheduler"#,
        #"online_scheduler.subpackage",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
