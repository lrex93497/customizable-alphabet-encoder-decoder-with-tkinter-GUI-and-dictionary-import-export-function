# customizable-alphabet-encoder-decoder-with-tkinter-GUI-and-dictionary-import-export-function

*customizable alphabet encoder and decoder with tkinter GUI v1.0*<br />
## Index<br />
### [Introduction](#intro)
### [How to use](#use)
### [Dictionary import and export system](#im-export)
### [Error detection](#error)
### [System Requirement](#requirement)
### [License](#license)


<h3 id="intro"> Introduction</h3>

This is a customizable alphabet letter encoder and decoder with the addition of en/decryption dictionary import/export function.  Written in python 3.7.3 with Tkinter GUI.<br /><br /> 

This program works in the way by using dictionary to convert each alphabet (case sensitive) in the original text to the specified one. This program only converts English alphabet letters, other content such as numbers, symbols will not be converted.  <br /><br />

Below is the program GUI layout, all GUI scales will auto-resize with program window size.

<img src="image/GUI_layout.PNG" width="900">

<h3 id="use"> How to use</h3>

Run main.py to open the program

Users can choose to use encrypt mode or decrypt mode on the radio buttons at the top of the program.  <br /><br />

The section  "Current encrypt dictionary" shows the current dictionary using, all text will be encrypted according to this dictionary in encrypt mode. 
In decrypt mode, the dictionary's key and value will be reversed inside the program to form a decrypt dictionary, it will not be shown in the section of "Current encrypt dictionary". The decrypt dictionary will use to decrypt the encrypted text to plain text.  <br /><br />

Enter plain text in encrypt mode or ciphertext in decrypt mode inside the input box near "original text". Then press the "Process" button inside the red square, plain text will be encrypted into ciphertext in encrypt mode while ciphertext will be decrypted into plain text in decrypt mode. All results will be output in the text box near "Processed text". <br /><br />

Press right-click or use shortcut key to choose cut(Ctrl+x), copy(Ctrl+c) or paste(Ctrl+v) inside any input/output box to do respective function on the highlighted text. Please also be reminded scroll bar will appear in that two text boxes near "origin text" and "processed text" respectively if the number of words excessed the space, use the scroll wheel to scroll up and down or drag the scrollbar directly.<br /><br />

There are 3 methods to customize the encrypt dictionary: two default methods and user import encrypt dictionary.<br /><br />
Method 1 allows the user to customize which character will each alphabet transfer to. To do that, change each input box in method 1 section respective to each alphabet. After that, press "Apply Method 1" button to apply the change, a successful change will be shown in the section: "Current Encrypt Dictionary". <br /><br />

Please be reminded that only the first character inside each input box will be read, all extra input except the first character will be removed after pressing "Apply Method 1".<br />
All invalid input in method 1 like repeated character(s), non-alphabet input, etc. will cause errors. In such cases, an error window pops out pointing out the error, and the invalid input will not be applied to the encrypt dictionary which will remain as it is. For details, please refer to section [Error detection](#error).<br /><br />

Method 2 allows the user to customize the dictionary by indicating how many alphabets to shift, "+" for shift forward and "-" for shift backward. For examples +1 with change a:a, b:b, c:c... to  a:b, b:c, c:d..., while -1 will change to a:z, b:a, c:b... "+" sign is not necessary to type.<br />  The default dictionary is +1.<br /> 
All changes applied successfully will appear in section: "Current Encrypt Dictionary".<br /><br />

Method 2 only accept value from -26 to 26, other value than these will result in error message pop up and no change will be applied to encrypt dictionary. For details, please refer to section [Error detection system](#error) <br />

<h3 id="im-export"> Dictionary import and export system</h3>

Users can import or export the current dictionary by clicking "import existing encryption dictionary(.txt)" or "export existing decryption dictionary as .txt" respectively, after clicking the buttons mentioned, a window will pop out and ask users to choose a location and file name to export or location to import the file, see below pictures. The supported format in export and import mode is .txt only. Users can customize the dictionary .txt file exported and import it again.<br /><br />

Import window:<br/>
<img src="image/import_window.PNG" width="600"><br/>
Export window:<br/>
<img src="image/export_window.PNG" width="600"><br/>

All invalid data in the imported file or no file chose to import or export will result in an error message, with the suspension of the im/export process, please redo the process if such error message occurs, for details, please refer to section [Error detection](#error).<br /><br />

<h3 id="error"> Error detection </h3>

This program can detect different input/export/import errors.<br /><br />

**If an error occurred, the current command given by the user will be stopped. Not change/decryption/encryption will be made**<br />
**Only one error will be shown in a single time**<br /><br />

The error detection in method 2 can determine if the input is within -26 to 26. In the case of outranged input, the error message box "Please input integer within -26 to 26 in method 2 setting." will pop up. While in the case of non-number input, the error message box "Please input '+' or '-' integer only in method 2 setting." will pop up. See the below picture:<br/>
<img src="image/error_outrange.PNG" width="600"><br/>

On the other hand, the errors in method 1 were assigned a value in *error_code*  inside the program. The *error_code* was returned by function *check_if_valid_method_1()* with "False". If every input is ok, *check_if_valid_method_1()* return True and *error_code* has no use. <br/>
*error_code*  1-3 is for method 1's errors, a respective message box pops up with details if exact error(s) are present. See below table and example of pop-up message box:<br/><br/>
<img src="image/error_method_1_repetitive.PNG" width="600"><br/>
| *error_code*  | details |
| ------------- | ------------- |
| 1  | There is/are null input in method 1 setting. |
| 2  | There is/are repetitive input in method 1 setting. |
| 3  | There is/are non-alpha letter input in method 1 setting.|
<br/>
Other unknown error(s) in method 1 will result in a pop-up message box error with "There is/are invalid input(s) in method 1 setting."

<br/><br/>

In the same way but assessed by *check_if_valid_import()*, all data from imported .txt will first check by this function. *check_if_valid_import()* will return true for valid data, false for invalid data with *error_code*. *error_code* 4-9 is used for the case of invalid input, see below table:<br/>

| *error_code*  | details |
| ------------- | ------------- |
| 4  | There is/are null data in import .txt. |
| 5  | There is/are repetitive data (dictionary value) in import .txt. |
| 6  | There is/are non-alpha letter input in import .txt.  |
| 7  | There is/are repetitive data (dictionary key) in import .txt.  |
| 8  | abandoned |
| 9  | Same as error_code 7.  |<br/>

A similar error message box like the one in method 1 will pop up respective to the error.<br/><br/>

If the imported file is not a 52 length dictionary, "Error", "There dictionary in import .txt has bad format." will be given.<br/>
In case of no file confirmed to import, pop-up message box, "error", "There is/are invalid data in import .txt. or import canceled." will be given.<br/>
Another unknown error(s) will result in the same pop-up message box error with "There is/are invalid data in import .txt. or import canceled.".<br/><br/>


<h3 id="requirement"> System Requirement</h3>
Monitor minimum  support 1300x810 <br />
Python installed, recommended 3.7.3 

<h3 id="license"> License</h3>
This program was distributed under the BSD-3-Clause License.


