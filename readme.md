Welcome to Super Simple Stock Market

this project is writen against python 3.6

to run tests
```
python setup.py pytest
```

Data classes are in
```
sssm/model
```

Data storage in
```
sssm/storage
```
Due to the nature of the storage in this project some business cases are covered in storage
file, when transforming it into proper datastorage solution it's wise to separate them.
Ala the check for dividend type, that will also allow to move the register stock to
constructor of stock(circular imports).
Also storage introduces some bad imports that would get fixed on proper storage solution.


general calculations
```
sssm/services
```