## Comprehensions exercices 


### P.1

Write a python program that takes a sentence or list of sentences and outputs a list of integers where each integer
represent the length of the world of the same index , if and only if the word is not "the"

* sentences : 
    * The quick brown fox jumps over the lazy dog
    * Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec orci nibh, lacinia vel nisi a, mollis auctor magna. Sed non consequat neque. Donec rhoncus ligula eget enim accumsan dictum.
    * Duis egestas dictum pharetra. Fusce sit amet porttitor augue. Integer luctus vel ligula et varius. Quisque pulvinar lobortis finibus. Proin lacus neque, pulvinar in facilisis eget, varius iaculis risus. Nullam tempor felis non diam maximus interdum. Integer eget hendrerit magna. Fusce ligula erat, posuere et turpis sed, laoreet dictum ex.

### P.2 

Given a list of stock price output a list prices that are higher than average and a list of prices that are lower than average 
hint : you need more functions

* Samples :
    * [prices](https://pastebin.com/raw/sZYhuSap)

### P.3

Given a dictionary of fruits and their prices create a new dictionary of fruits whose price is higher than 10

* samples : 
    * {"apple":15,"orange":22,"grapefruit":7,"coconuts":3,"melon":18,"bananas":8,"cherry":5,"peach":2,"pears":13}

### P.4

Given  a list of  (keys:values) make a new dictionary by taking modulo 5 of the values and lower case of strings.

* Samples :
    * [dict](https://pastebin.com/raw/m4CpuBDG)


## Building your first libraries 

### P.1

Implement a module called kmp that implements the following [algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)
the output should be the index of the start and end of the sequence 

* Test cases :
    * in : W = "ABCDABD" and S = "ABC ABCDAB ABCDABCDABDE" out :4,9 
    * in : W = "abra" and S = "abr lo abraca dabra"
    * in : W = "btc" and S = "eth trx b nbse npa scbtm xmr btcl enp osrop"

### P.2

Implement a module called prime field that implements a function called gen_field , gen_field should take one number p  as a parameter check if it's a prime
if it is generate a prime field (list of integers from 0 to p modulo p) gen_field should return the prime field as a list .

* helpers:
    - implement an is prime algorithm [hint](https://en.wikipedia.org/wiki/Primality_test)


