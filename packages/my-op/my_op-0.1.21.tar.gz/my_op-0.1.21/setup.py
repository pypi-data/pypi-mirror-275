import setuptools

setuptools.setup(
  name='my_op',
  version='0.1.18',
  python_requires='>=3.7',
  packages=setuptools.find_packages(),
  package_data={'test': ['*.zip', '*.z*']},
  classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ]
)