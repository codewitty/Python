#My Python code at De Anza

> This repo contains the beginner Python code I wrote at De Anza College


[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)

---

## Table of Contents 


- [In Class Assignments](#in-class-assignments)
	* [Exercise A.cpp](#1-exercise-A)
	* [Exercise B.cpp](#2-exercise-B)
	* [Exercise C.cpp](#1-exercise-A)
	* [Exercise D.cpp](#1-exercise-A)
	* [Exercise E.cpp](#1-exercise-A)
	* [Exercise F.cpp](#1-exercise-A)
	* [Exercise G.cpp](#1-exercise-A)
	* [Exercise H.cpp](#1-exercise-A)
	* [Exercise I.cpp](#1-exercise-A)
	* [Exercise J.cpp](#1-exercise-A)
	* [Exercise K.cpp](#1-exercise-A)
- [Take Home Assignments](#take-home-assignments)
	* [Problem A.cpp](#1-exercise-A)
	* [Problem B.cpp](#2-exercise-B)
	* [Problem C.cpp](#1-exercise-A)
	* [Problem D.cpp](#1-exercise-A)
	* [Problem E.cpp](#1-exercise-A)
	* [Problem F.cpp](#1-exercise-A)
	* [Problem G.cpp](#1-exercise-A)
	* [Problem H.cpp](#1-exercise-A)
	* [Problem I.cpp](#1-exercise-A)
	* [Problem J.cpp](#1-exercise-A)
	* [Problem K.cpp](#1-exercise-A)
---

### In Class Assignments
- These assignments were short in-class challenges that introduced a new concept.

#### 1. Exercise A
- Create a height and width for a rectangle. Print the height, width, and area of the rectangle in the following format, with the columns aligned:

height: x.x\
width:  x.x\
area:   x.xxxxxxx...\
Test with width 7.1 and height 2.9\
and in the same script use floor division to divide the width and height by 2 and save these values in the height and width.

---

#### 2. Exercise B
- **String methods:**\
Ask the user for a name (test with George Washington).\
Print the name in all uppercase letters.\
Print the length of the name.\
Print the 4th character of the name (r).\
Create a variable called name2. Assign to name2 the name with all "o" characters replaced with "x"s.\
Print name2.
Print the original name.\
**Counting and Finding**\
Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).\
Count how many "a" characters there are, print the result.\
Print the index of all the "a" characters.\
Hint: Except for the first find, set the start location for the next find as the previous location found index + 1. The second argument in the find method is the index where the find starts looking.

#### 3. Exercise C
- **List script**\
Create a list called list1 that has elements 2, 4.1, 'hello'.\
Copy list1 to list2 so that list2 is an alias of list1 (shallow copy).\
Copy list1 to list3 so that list3 is a new list (true deep copy).\
Using ==, compare list1 to list2, list 1 to list 3, and list 2 to list3.\
Using is, compare list1 to list2, list 1 to list 3, and list 2 to list3.\
Print the ids of list 1, list2, and list3.\
Append a new element with value 8 to list1.\
After the first element of list2, insert an element 'goodbye'.\
Remove the first element from list3.\
Print each of the three lists. Do the results match what you expected?

#### 4. Exercise D 
- **Dictionary Basics:**\
Create a dictionary of fruit and desserts made from the fruit. The fruit should be the key and the dessert should be the value. Use these key value pairs:\
apple:sauce\
peach:cobbler\
carrot:cake\
strawberry:sorbet\
banana:cream pie\
Add the mango fruit to the dictionary. Its dessert is sticky rice.\
Change the strawberry dessert to shortcake.\
Carrot is not a fruit, so remove carrot from the dictionary.\
Print the apple dessert.\
See if a banana dessert exists.\
See if a pear dessert exists.\
Print the keys in the dessert dictionary.\
Print the values in the dessert dictionary.\
Print the key-value pairs in the dessert dictionary.\
**Combining dictionaries:**\
Create a dictionary named capitols1 and populate it with these key value pairs:\
Alabama:Montgomery\
Alaska:Juneau\
Arizona:Phoenix\
Arkansas:Little Rock\
California:Sacramento\
Create a dictionary named capitols2 and populate it with these key value pairs:\
California:Sac.\
Colorado:Denver\
Connecticut:Hartford\
Be sure that the California capitol is Sac. and not Sacramento.\
Using the dictionary update() method, update capitols1 with capitols2.\
Print the sorted capitols (values). Note the updated value of California's capitol.\
**Sets Basics:**\
Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.\
Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.\
Add John to class1.\
Print a sorted list of students who are in both classes.\
Print a sorted list of all students.\
Test to see if Sasha is in class1. \


#### 5. Valid Mountain Array
- Given an array A of integers, return true if and only if it is a valid mountain array.\
Recall that A is a mountain array if and only if:
	* A.length >= 3
	* There exists some i with 0 < i < A.length - 1 such that:
		+ A[0] < A[1] < ... A[i-1] < A[i]
		+ A[i] > A[i+1] > ... > A[A.length - 1]
- My solution is <a href="https://github.com/codewitty/LeetCode/blob/master/Arrays/Valid_Mountain_Array.cpp/" target="_blank">`here`</a>.\
Find the problem <a href="https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/" target="_blank">`here`</a>.

#### 6. Replace Elements with Greatest Element on Right Side
- Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.\
After doing so, return the array.
	* Example 1:
		+ Input: arr = [17,18,5,4,6,1]
		+ Output: [18,6,6,6,1,-1]
- My solution is <a href="https://github.com/codewitty/LeetCode/blob/master/Arrays/Replace_Elements_with_Greatest_Element_on_Right_Side.cpp/" target="_blank">`here`</a>.\
Find the problem <a href="https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/" target="_blank">`here`</a>.

<!---
#### 
- Given an array nums and a value val, remove all instances of that value in-place and return the new length.\
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.\
The order of elements can be changed. It doesn't matter what you leave beyond the new length.\
My solution is <a href="/" target="_blank">`here`</a>.\
Find the problem <a href="/" target="_blank">`here`</a>.
-->

---

### Random

---
## Support

Reach out to me at one of the following places!

- <a href="https://codewitty.github.io/resume/" target="_blank">`My Website`</a>
- Instagram at <a href="https://www.instagram.com/drawntowildplaces/" target="_blank">`Instagram`</a>
- Twitter at <a href="https://twitter.com/codewitty_" target="_blank">`@codewitty_`</a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="https://codewitty.github.io/resume/" target="_blank">CodewittyProductions</a>.
