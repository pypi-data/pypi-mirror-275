import setuptools
with open('README.md', 'r', encoding='utf-8')as fh:
  long_description = fh.read()
setuptools.setup(
  name='original_janken',
  version='0.0.2',
  author='Takeru_Wakatsuki',
  author_email='s2222100@stu.musashino-u.ac.jp',
  description='You can make original rock paper scissors.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/s2222100/original_janken',
  project_urls={
    "Bug Tracker":"https://github.com/s2222100/original_janken"
  },
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  package_dir={'':'src'},
  py_modules=["original_janken"],
  packages=setuptools.find_packages(where='src'),
  python_requires='>=3.7',
  entry_points={
      'console_scripts':[
        'original_janken=original_janken:main'
    ]
  },
)
