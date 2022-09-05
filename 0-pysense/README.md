# purpose for pysense1 program
test all sensor installed on the pysense board :
- display values in console (via USB cable)
- inifnite loop and display every 5 seconds

## usage
via REPL console... 

## purpose for pysense2 program
test only one sensor installed on the pysense board, wire the scope to display the I2C frame:
- display value in console (via USB cable)
- infinite loop and display every 5 seconds

## usage
start via REPL console...  for example
```python
 exec(open("pysense2.py").read())
 ```