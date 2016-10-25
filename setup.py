from setuptools import setup, find_packages

setup(name='data_kobe_util',
	version='0.1.0',
	description='Health check library for data.city.kobe.lg.jp',
	long_description=open("README.rst").read(),
	author='Hiroaki Kawai',
	author_email='hiroaki.kawai@gmail.com',
	url='https://github.com/hkwi/data_kobe_util/',
	packages=find_packages(),
	test_suite = "nose.collector"
)
