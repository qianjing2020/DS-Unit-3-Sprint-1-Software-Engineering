## Notes on twine upload package to test pypi: 

I did both the following option and successfully uploaded package:

1. In terminal: Deactivate pipenv shell (only use conda base) when prepare package upload using twine

2. In vscode terminal: deactivate conda base
activate virtual env 
then upload package

But if both conda and pipenv is activated, it will mess up. Won't be able to upload successfully to test pypi website. 


## use pep8 style
```
pipenv install autopep8 --dev

autopep8 --aggressive --in-place --recursive .
``` 
will change style inplace for all files in current directory.