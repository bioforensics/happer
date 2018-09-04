## help:        print this help message and exit
help: Makefile
	@echo ''
	@sed -n 's/^## //p' Makefile
	@echo ''

## test:        execute the automated test suite
test:
	py.test --cov=happer happer/tests/*.py

## style:       check Python code style against PEP8
style:
	pycodestyle setup.py happer/*.py happer/tests/*.py

## devdeps:     install development dependencies
devdeps:
	pip3 install pycodestyle pytest pytest-cov pytest-sugar

## hooks:       install git hooks for development
hooks:
	echo "make style" >> .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit

## clean:       remove development artifacts
clean:
	rm -rf __pycache__/ happer/__pycache__/ happer/*/__pycache__ build/ dist/ *.egg-info/
