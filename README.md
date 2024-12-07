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

---

# Performance of PyCryptodome

```text
Running DES tests...
DES | Mode: CBC | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.0236s | Decrypt Time: 0.0181s
DES | Mode: CBC | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 0.2301s | Decrypt Time: 0.1789s
DES | Mode: CBC | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 2.2810s | Decrypt Time: 1.8038s
DES | Mode: CBC | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 11.6555s | Decrypt Time: 9.1365s
DES | Mode: CBC | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 24.6886s | Decrypt Time: 19.1119s
DES | Mode: OFB | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.0547s | Decrypt Time: 0.0364s
DES | Mode: OFB | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 0.2238s | Decrypt Time: 0.2192s
DES | Mode: OFB | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 2.1952s | Decrypt Time: 2.1864s
DES | Mode: OFB | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 11.0573s | Decrypt Time: 11.1232s
DES | Mode: OFB | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 23.9081s | Decrypt Time: 23.4161s
DES | Mode: CTR | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.0736s | Decrypt Time: 0.0295s
DES | Mode: CTR | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 0.1782s | Decrypt Time: 0.1759s
DES | Mode: CTR | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 1.7664s | Decrypt Time: 1.7769s
DES | Mode: CTR | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 8.8736s | Decrypt Time: 8.8790s
DES | Mode: CTR | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 23.0249s | Decrypt Time: 22.7583s
Running 3DES tests...
3DES | Mode: CBC | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.0864s | Decrypt Time: 0.0700s
3DES | Mode: CBC | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 0.7660s | Decrypt Time: 0.7420s
3DES | Mode: CBC | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 6.5576s | Decrypt Time: 5.8925s
3DES | Mode: CBC | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 32.4300s | Decrypt Time: 29.6427s
3DES | Mode: CBC | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 66.8023s | Decrypt Time: 60.8776s
3DES | Mode: OFB | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.1206s | Decrypt Time: 0.0727s
3DES | Mode: OFB | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 0.6167s | Decrypt Time: 0.6153s
3DES | Mode: OFB | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 6.1591s | Decrypt Time: 6.2040s
3DES | Mode: OFB | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 31.3669s | Decrypt Time: 31.2299s
3DES | Mode: OFB | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 65.0857s | Decrypt Time: 64.3864s
3DES | Mode: CTR | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.0972s | Decrypt Time: 0.0762s
3DES | Mode: CTR | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 0.5733s | Decrypt Time: 0.5727s
3DES | Mode: CTR | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 5.7298s | Decrypt Time: 5.7219s
3DES | Mode: CTR | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 28.7163s | Decrypt Time: 28.8951s
3DES | Mode: CTR | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 60.2442s | Decrypt Time: 59.9729s
Running AES tests...
AES | Key Size: 128 bits | Mode: CBC | Plaintext Size: 1MB | Encrypt Time: 0.0096s | Decrypt Time: 0.0056s
AES | Key Size: 128 bits | Mode: CBC | Plaintext Size: 10MB | Encrypt Time: 0.0618s | Decrypt Time: 0.0511s
AES | Key Size: 128 bits | Mode: CBC | Plaintext Size: 100MB | Encrypt Time: 0.6286s | Decrypt Time: 0.5262s
AES | Key Size: 128 bits | Mode: CBC | Plaintext Size: 500MB | Encrypt Time: 3.3996s | Decrypt Time: 2.9316s
AES | Key Size: 128 bits | Mode: CBC | Plaintext Size: 1024MB | Encrypt Time: 8.4632s | Decrypt Time: 5.9462s
AES | Key Size: 128 bits | Mode: OFB | Plaintext Size: 1MB | Encrypt Time: 0.0197s | Decrypt Time: 0.0163s
AES | Key Size: 128 bits | Mode: OFB | Plaintext Size: 10MB | Encrypt Time: 0.0582s | Decrypt Time: 0.0569s
AES | Key Size: 128 bits | Mode: OFB | Plaintext Size: 100MB | Encrypt Time: 0.5968s | Decrypt Time: 0.5805s
AES | Key Size: 128 bits | Mode: OFB | Plaintext Size: 500MB | Encrypt Time: 3.3156s | Decrypt Time: 3.2323s
AES | Key Size: 128 bits | Mode: OFB | Plaintext Size: 1024MB | Encrypt Time: 8.1842s | Decrypt Time: 6.5626s
AES | Key Size: 128 bits | Mode: CTR | Plaintext Size: 1MB | Encrypt Time: 0.0187s | Decrypt Time: 0.0174s
AES | Key Size: 128 bits | Mode: CTR | Plaintext Size: 10MB | Encrypt Time: 0.0544s | Decrypt Time: 0.0530s
AES | Key Size: 128 bits | Mode: CTR | Plaintext Size: 100MB | Encrypt Time: 0.5525s | Decrypt Time: 0.5392s
AES | Key Size: 128 bits | Mode: CTR | Plaintext Size: 500MB | Encrypt Time: 2.7350s | Decrypt Time: 2.8689s
AES | Key Size: 128 bits | Mode: CTR | Plaintext Size: 1024MB | Encrypt Time: 7.0255s | Decrypt Time: 6.0561s
AES | Key Size: 192 bits | Mode: CBC | Plaintext Size: 1MB | Encrypt Time: 0.0193s | Decrypt Time: 0.0252s
AES | Key Size: 192 bits | Mode: CBC | Plaintext Size: 10MB | Encrypt Time: 0.0729s | Decrypt Time: 0.0608s
AES | Key Size: 192 bits | Mode: CBC | Plaintext Size: 100MB | Encrypt Time: 0.7105s | Decrypt Time: 0.6214s
AES | Key Size: 192 bits | Mode: CBC | Plaintext Size: 500MB | Encrypt Time: 3.6505s | Decrypt Time: 3.3645s
AES | Key Size: 192 bits | Mode: CBC | Plaintext Size: 1024MB | Encrypt Time: 9.5132s | Decrypt Time: 7.2455s
AES | Key Size: 192 bits | Mode: OFB | Plaintext Size: 1MB | Encrypt Time: 0.0729s | Decrypt Time: 0.0188s
AES | Key Size: 192 bits | Mode: OFB | Plaintext Size: 10MB | Encrypt Time: 0.0674s | Decrypt Time: 0.0667s
AES | Key Size: 192 bits | Mode: OFB | Plaintext Size: 100MB | Encrypt Time: 0.6761s | Decrypt Time: 0.6713s
AES | Key Size: 192 bits | Mode: OFB | Plaintext Size: 500MB | Encrypt Time: 3.6887s | Decrypt Time: 3.7255s
AES | Key Size: 192 bits | Mode: OFB | Plaintext Size: 1024MB | Encrypt Time: 9.0312s | Decrypt Time: 7.4878s
AES | Key Size: 192 bits | Mode: CTR | Plaintext Size: 1MB | Encrypt Time: 0.0199s | Decrypt Time: 0.0168s
AES | Key Size: 192 bits | Mode: CTR | Plaintext Size: 10MB | Encrypt Time: 0.0627s | Decrypt Time: 0.0619s
AES | Key Size: 192 bits | Mode: CTR | Plaintext Size: 100MB | Encrypt Time: 0.6306s | Decrypt Time: 0.6249s
AES | Key Size: 192 bits | Mode: CTR | Plaintext Size: 500MB | Encrypt Time: 3.1494s | Decrypt Time: 3.2485s
AES | Key Size: 192 bits | Mode: CTR | Plaintext Size: 1024MB | Encrypt Time: 7.9458s | Decrypt Time: 6.9214s
AES | Key Size: 256 bits | Mode: CBC | Plaintext Size: 1MB | Encrypt Time: 0.0224s | Decrypt Time: 0.0166s
AES | Key Size: 256 bits | Mode: CBC | Plaintext Size: 10MB | Encrypt Time: 0.0793s | Decrypt Time: 0.0725s
AES | Key Size: 256 bits | Mode: CBC | Plaintext Size: 100MB | Encrypt Time: 0.7944s | Decrypt Time: 0.7075s
AES | Key Size: 256 bits | Mode: CBC | Plaintext Size: 500MB | Encrypt Time: 4.2113s | Decrypt Time: 3.8299s
AES | Key Size: 256 bits | Mode: CBC | Plaintext Size: 1024MB | Encrypt Time: 10.0570s | Decrypt Time: 7.7753s
AES | Key Size: 256 bits | Mode: OFB | Plaintext Size: 1MB | Encrypt Time: 0.0474s | Decrypt Time: 0.0201s
AES | Key Size: 256 bits | Mode: OFB | Plaintext Size: 10MB | Encrypt Time: 0.0766s | Decrypt Time: 0.0754s
AES | Key Size: 256 bits | Mode: OFB | Plaintext Size: 100MB | Encrypt Time: 0.7693s | Decrypt Time: 0.7580s
AES | Key Size: 256 bits | Mode: OFB | Plaintext Size: 500MB | Encrypt Time: 4.1379s | Decrypt Time: 4.1824s
AES | Key Size: 256 bits | Mode: OFB | Plaintext Size: 1024MB | Encrypt Time: 10.0425s | Decrypt Time: 8.5548s
AES | Key Size: 256 bits | Mode: CTR | Plaintext Size: 1MB | Encrypt Time: 0.0220s | Decrypt Time: 0.0171s
AES | Key Size: 256 bits | Mode: CTR | Plaintext Size: 10MB | Encrypt Time: 0.0719s | Decrypt Time: 0.0712s
AES | Key Size: 256 bits | Mode: CTR | Plaintext Size: 100MB | Encrypt Time: 0.7183s | Decrypt Time: 0.7162s
AES | Key Size: 256 bits | Mode: CTR | Plaintext Size: 500MB | Encrypt Time: 3.5999s | Decrypt Time: 3.6806s
AES | Key Size: 256 bits | Mode: CTR | Plaintext Size: 1024MB | Encrypt Time: 8.9076s | Decrypt Time: 7.9238s
Running Blowfish tests...
Blowfish | Mode: CBC | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.0192s | Decrypt Time: 0.0090s
Blowfish | Mode: CBC | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 0.1651s | Decrypt Time: 0.0910s
Blowfish | Mode: CBC | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 1.6104s | Decrypt Time: 0.9110s
Blowfish | Mode: CBC | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 8.2462s | Decrypt Time: 4.7411s
Blowfish | Mode: CBC | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 18.7467s | Decrypt Time: 10.0188s
Blowfish | Mode: OFB | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.0279s | Decrypt Time: 0.0246s
Blowfish | Mode: OFB | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 0.1533s | Decrypt Time: 0.1517s
Blowfish | Mode: OFB | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 1.5380s | Decrypt Time: 1.5452s
Blowfish | Mode: OFB | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 8.0827s | Decrypt Time: 8.0744s
Blowfish | Mode: OFB | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 17.9639s | Decrypt Time: 16.5740s
Blowfish | Mode: CTR | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.0240s | Decrypt Time: 0.0194s
Blowfish | Mode: CTR | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 0.1007s | Decrypt Time: 0.1003s
Blowfish | Mode: CTR | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 1.0319s | Decrypt Time: 0.9970s
Blowfish | Mode: CTR | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 5.0567s | Decrypt Time: 5.1690s
Blowfish | Mode: CTR | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 11.6013s | Decrypt Time: 10.9945s
All tests completed.
```
---

# Performance of Our Implementation

```text
Running DES tests...
DES | Mode: CBC | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.2485s | Decrypt Time: 0.2510s
DES | Mode: OFB | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.2546s | Decrypt Time: 0.2559s
DES | Mode: CTR | Plaintext Size: 1MB | Key Size: 64 bits | Encrypt Time: 0.2680s | Decrypt Time: 0.2640s
DES | Mode: CBC | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 2.4989s | Decrypt Time: 2.4856s
DES | Mode: OFB | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 2.5480s | Decrypt Time: 2.5492s
DES | Mode: CTR | Plaintext Size: 10MB | Key Size: 64 bits | Encrypt Time: 2.6674s | Decrypt Time: 2.6591s
DES | Mode: CBC | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 25.3852s | Decrypt Time: 25.2066s
DES | Mode: OFB | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 26.0356s | Decrypt Time: 26.0275s
DES | Mode: CTR | Plaintext Size: 100MB | Key Size: 64 bits | Encrypt Time: 26.8013s | Decrypt Time: 26.6109s
DES | Mode: CBC | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 125.2140s | Decrypt Time: 125.4859s
DES | Mode: OFB | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 128.7590s | Decrypt Time: 127.9677s
DES | Mode: CTR | Plaintext Size: 500MB | Key Size: 64 bits | Encrypt Time: 140.7880s | Decrypt Time: 135.2792s
DES | Mode: CBC | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 278.8124s | Decrypt Time: 287.6125s
DES | Mode: OFB | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 305.9997s | Decrypt Time: 287.2194s
DES | Mode: CTR | Plaintext Size: 1024MB | Key Size: 64 bits | Encrypt Time: 287.1949s | Decrypt Time: 289.6033s
Running 3DES tests...
3DES | Mode: CBC | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.2750s | Decrypt Time: 0.2731s
3DES | Mode: OFB | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.2799s | Decrypt Time: 0.2806s
3DES | Mode: CTR | Plaintext Size: 1MB | Key Size: 192 bits | Encrypt Time: 0.2847s | Decrypt Time: 0.2848s
3DES | Mode: CBC | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 2.7225s | Decrypt Time: 2.7883s
3DES | Mode: OFB | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 3.1252s | Decrypt Time: 2.9151s
3DES | Mode: CTR | Plaintext Size: 10MB | Key Size: 192 bits | Encrypt Time: 2.9835s | Decrypt Time: 2.9908s
3DES | Mode: CBC | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 29.0715s | Decrypt Time: 28.4458s
3DES | Mode: OFB | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 29.6771s | Decrypt Time: 31.0525s
3DES | Mode: CTR | Plaintext Size: 100MB | Key Size: 192 bits | Encrypt Time: 39.2389s | Decrypt Time: 35.9553s
3DES | Mode: CBC | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 142.9565s | Decrypt Time: 136.6240s
3DES | Mode: OFB | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 150.0791s | Decrypt Time: 174.2878s
3DES | Mode: CTR | Plaintext Size: 500MB | Key Size: 192 bits | Encrypt Time: 145.6136s | Decrypt Time: 146.6694s
3DES | Mode: CBC | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 292.5874s | Decrypt Time: 287.0507s
3DES | Mode: OFB | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 295.1751s | Decrypt Time: 310.6609s
3DES | Mode: CTR | Plaintext Size: 1024MB | Key Size: 192 bits | Encrypt Time: 345.6371s | Decrypt Time: 332.1454s
Running AES tests...
Testing AES with a 128-bit key...
AES-128 | Mode: CBC | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.1399s | Decrypt Time: 0.1404s
AES-128 | Mode: OFB | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.1460s | Decrypt Time: 0.1459s
AES-128 | Mode: CTR | Plaintext Size: 1MB | Key Size: 128 bits | Encrypt Time: 0.1508s | Decrypt Time: 0.1510s
AES-128 | Mode: CBC | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 1.4197s | Decrypt Time: 1.4203s
AES-128 | Mode: OFB | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 1.4703s | Decrypt Time: 1.4562s
AES-128 | Mode: CTR | Plaintext Size: 10MB | Key Size: 128 bits | Encrypt Time: 1.5236s | Decrypt Time: 1.5379s
AES-128 | Mode: CBC | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 14.3338s | Decrypt Time: 14.5371s
AES-128 | Mode: OFB | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 14.6918s | Decrypt Time: 14.7569s
AES-128 | Mode: CTR | Plaintext Size: 100MB | Key Size: 128 bits | Encrypt Time: 15.7675s | Decrypt Time: 15.8424s
AES-128 | Mode: CBC | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 72.3653s | Decrypt Time: 71.8957s
AES-128 | Mode: OFB | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 74.6293s | Decrypt Time: 74.7186s
AES-128 | Mode: CTR | Plaintext Size: 500MB | Key Size: 128 bits | Encrypt Time: 77.2300s | Decrypt Time: 77.3159s
AES-128 | Mode: CBC | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 148.2683s | Decrypt Time: 148.5283s
AES-128 | Mode: OFB | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 151.8386s | Decrypt Time: 152.7266s
AES-128 | Mode: CTR | Plaintext Size: 1024MB | Key Size: 128 bits | Encrypt Time: 159.3191s | Decrypt Time: 159.1953s
Testing AES with a 192-bit key...






All tests completed.

```
