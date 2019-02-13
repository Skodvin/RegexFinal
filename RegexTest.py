import re

txt = "[  3]  0.0-30.0 sec   243 KBytes  66.4 Kbits/sec  11.253 ms    8/  838 (0.95%)"

Transfer = re.findall("\d{3}|$", txt) [0]
print ("Transfer: " + Transfer + " KBytes")

Bandwidth = re.findall("\d{2}.\d{1}", txt) [1]
print ("Båndbredde: " + Bandwidth + " Kb/sec")

Jitter = re.findall("\d{2}.\d{3}", txt) [0]
print ("Jitter: " + Jitter + " ms")

PLoss1 = re.findall("\d{3}", txt) [2]


PLoss = re.findall("\d{1}/", txt) [0]
print ("Pakketap: " + PLoss + PLoss1)

PLossPerc = re.findall("\d{1}.\d{2}%", txt) [0]
print ("Pakketap i %: " + PLossPerc)
