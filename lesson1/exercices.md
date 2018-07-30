### Lesson 1 : Exercices

**N.B** : 
- Using comments , write your thought process for each solution
- Don't cheat (copy paste code) I'll smell it if you do it 


#### P.1
- Create a Github repository called learn-to-snake
- Clone and do all the exercises and push them to this repository 



#### P.2

- Write a function *reverse* that takes a string and outputs it in reverse

- Write a function *palindrome* that takes a string and checks if it's a [palindrome](https://en.wikipedia.org/wiki/Palindrome)

- Write a function *palindromer* that takes a list of strings and checks whether each string is a palindrome it should  return a list of true/false value 


#### P.3

- Implement the following algorithm *sieve of erasthotenes* that prints all primes smaller than n (it requires a bit of thinking don't rewrite the steps)


1. Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
2. Initially, let p equal 2, the first prime number.
3. Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, all the numbers in the list that are not marked are prime.


