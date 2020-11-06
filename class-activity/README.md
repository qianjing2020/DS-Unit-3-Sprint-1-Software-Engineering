## quick tip on twine upload package to test pypi: 
I did both the following option and successfully uploaded package 
In terminal: Deactivate pipenv shell (only use conda base) when prepare package upload using twine

In vscode terminal: deactivate conda base
activate virtual env 
then upload package


But if both conda and pipenv is activated, it will mess up. Won't be able to upload successfully to test pypi website. 

## first let python know module 
```python -m my_package.my_module.py```

## choose a license
https://choosealicense.com/appendix/


