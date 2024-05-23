python .\setup.py sdist

pip install .\dist\xiaojingcc-2.0.0.tar.gz

python -m build
twine check dist/*  
twine upload dist/*    
