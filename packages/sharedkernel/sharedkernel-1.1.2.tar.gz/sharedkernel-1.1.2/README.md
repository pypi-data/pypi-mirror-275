# SharedKernel
this a shared kernel package

# Create Package
    py -m pip install --upgrade build
    py -m build
    cd dist
    py -m pip install --upgrade twine
    py -m twine upload dist/*

# Pypi
pip install sharedkernel
