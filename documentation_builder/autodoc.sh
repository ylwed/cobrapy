rm cobra.rst cobra.*.rst
sphinx-apidoc -o . ../cobra ../cobra/oven ../cobra/external ../cobra/test ../cobra/solvers/*_java.py ../cobra/test_all.py
rm modules.rst
