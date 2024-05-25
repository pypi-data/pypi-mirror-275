from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tacalendar_ttime',
    version='0.2',
    description='Handles date time manipulation with simplicity',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Tousif Anaam',
    author_email='tousifanaam@gmail.com',
    py_modules=['tacalendar_ttime'],
    keywords=['ttime', 'tcalendar', 'tcalendar_time', 'tc', 'tt'],
    url='https://github.com/tousifanaam/tcalendar',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)