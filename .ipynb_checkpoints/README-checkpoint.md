# RSA_Encryption

**Hey guys! Feel free to change or upload your part of the code here. If there is any change you want others to know, just leave the comment here (or using email and message as always).**

## Nov 14th
Now the RSA_Code can show an interactive interface. 

I limit the maximum key length to 56 in case it crash the computer.

```
Please enter the length of the key:  64

The length is too long for this program right now. Use 56 instead.

Please enter the plain text:  1qaz.;[=

The plain text is: 1qaz.;[=
The cipher is :[462631532846931842543950565739186, 172723360282645624089723206265541, 442954017366962340760204228248601, 199096408282453953554341816015061, 502185762545212621969279807830433, 255627421293421808654019937350330, 447825839567714545949134830099123, 81349531277163393804503106226682]
The decrypted text is: 1qaz.;[=
The decrypted text using CRT is: 1qaz.;[=
```

## Nov 8th
I have modified my RSA code and convert it into python files. You can call the method like this:
```
python RSA_Code.py
```
Currently it just generate random prime number and plain text of 48 bits. I will change it later to accept key length and customized message as input.

You can also import it as a module to use those methods in it.