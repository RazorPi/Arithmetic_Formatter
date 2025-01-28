# Arithmetic_Formatter
This is the first test on the Scientific Computation with Python cert by Free Code Camp.


##NOTE FROM THE AUTHOR:
In all fairness, I tried my best to solve the problem with the information I've acquired in the other courses of this certification. I tried to find answers in the "Help section" [Linked here]([url](https://forum.freecodecamp.org/search?q=Build%20an%20Arithmetic%20Formatter%20Project)). I also tried Google... lots of Google. And after hours of frustration, I asked the forum and got some answers. [Link to the FORUM here]([url](https://forum.freecodecamp.org/t/build-an-arithmetic-formatter-project-build-an-arithmetic-formatter-project/732218)).  All that to say... I did what every developer would do these days: ask Chat GPT. 

## Chat GPT:
**My Prompt:** Help me understand why this "Arithmetic Arranger" Python code is not passing test number 9. Here is the code to evaluate. [see original code for reference(/original_code.py:)](/original_code.py:) 

**The answer:**

## Possible Issues in Your Code
### 1. Use of eval() for calculations

* Using eval(x) can be dangerous and isn't necessary for a simple arithmetic problem. You should parse the numbers and perform the operations manually.

## 2. Incorrect Operator Validation

* Your operator check if set(operations) != {'+', '-'} and len(set(operations)) != 2: is incorrect.
* It will fail when there is a mix of valid and invalid operators because {'+', '-', '*'} will still have more than one element, leading to unpredictable behavior. \
**Fix:** Instead, iterate over operations and check each operator explicitly.

### 3. Incorrect Formatting of Output

* The expected format should have each operand aligned properly, but your implementation might not handle all edge cases correctly.\

**Potential Problem:** Handling of spacing and alignment when numbers are shorter or longer. The expected output format should look exactly like this:

<img width="298" alt="Screenshot 2025-01-28 at 3 43 50 PM" src="https://github.com/user-attachments/assets/60f548c7-8835-4239-9db3-c1c40caf658b" />


*Your approach may not be aligning numbers correctly, especially for numbers with different lengths.

### 4. Error Message Formatting Differences**

* Some test cases might expect exact error message wording. Ensure the error messages match exactly as required.


# Why Your Function Fails Test #9
## Misalignment in Second Operand (+ Sign Spacing Issue)

### In the expected output, the second operand (+ 40) is aligned with an extra space before the number:

  988
  +40

* Your function currently does:
  988
 +40

The missing extra space causes misalignment. \

### Incorrect Handling of Result Alignment

* The solutions should also align properly based on the problem width.
* Your approach using str(eval(x)) might be missing the necessary formatting adjustments.

# Fixes Needed
* Ensure that the second operand (+ operator and number) is properly formatted with an extra space.
* Align the results properly under the dashes.


[Link to new proposed code (Arithmetic_Formatter/build-an-arithmetic-formatter-project.py]



# Key Fixes
✅ Replaced eval() with direct arithmetic \
✅ Corrected operator validation logic \
✅ Ensured spacing and formatting are correct \
✅ Matched error messages exactly as expected \

