from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.readlines()

long_description = 'A smarter way to timeblock your Google calendar.'

setup(
		name ='smartcal',
		version ='0.0.0',
		author ='Christian Thomas',
		author_email ='christianthomas35@gmail.com',
		url ='https://github.com/christiancthomas/google-smart-calendar',
		description ='Command line package for the Google Smart calendar project.',
		long_description = long_description,
		long_description_content_type ="text/markdown",
		license ='MIT',
		packages = find_packages(),
		entry_points ={
			'console_scripts': [
				'smartcal = src.smartcal.command:main'
			]
		},
		classifiers =[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
		# keywords ='smartcal google-smart-calendar',
		install_requires = requirements,
		zip_safe = False
)
