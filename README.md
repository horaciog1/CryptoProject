# Introduction to Cryptography Project

Implement the 3 modes we've covered in class, `CBC`, `OFB` and `CTR`, and compare their
performance for (encryption, decryption).

Project written in Python3 using the `PyCryptodome` Library to implement the encryption algorithms.

This project will be comparing the performances of AES, DES, 3DES and Blow-fish with the modes of encryption. We will also be using parallelization when possible.

The code will be analyzed based on the following:
1) Plaintext sizes ranging from a few MB to a few GB. Please have at least 4-5 data points, and evaluate the running time. Plot this as a graph.
 
2) At least 3 algorithms: DES, 3DES, AES. For DES/3DES the key size is 64 bits, for AES, try different key sizes: 128, 192 and 256 bits. Evaluate the running time of your code on different key sizes, and evaluate the running time of the different plaintext sizes you picked in point #1 with varying key sizes.
 
Plot this on graph(s). For AES, you may want to have different graphs, since a single graph might look cluttered.
 
3) Compare the performance of your implementation of the 3 modes with a version of the modes implemented by a library API. Plot both on a graph.
 
It is likely the library one will be faster. In that case, think about and analyze what are they doing, i.e., what optimizations are they implementing that makes their code faster? This can be your own opinion, but it needs to be justified, and should be soundly reasoned through.

Authors: Horacio Gonzalez and Joseph Tomalewski

---

# Libraries
Install PyCryptodome library to be able to run the code:
```bash
pip install pycryptodome
```
> **_NOTE:_**  This command will try to install pycryptodome using the pip version of the python version that is set as default in your computer. Make sure you are running and installing on the same version.
> The Python version used for this project was 3.12.0, but any Python 3.X.X version should also work.
