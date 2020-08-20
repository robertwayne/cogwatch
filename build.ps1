./venv/scripts/activate.ps1
rm build -recurse
python setup.py sdist bdist_wheel
python -m twine upload --skip-existing dist/*
