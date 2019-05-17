import re
import sys
import ase.calculators.turbomole as turbomole

functional = "???"
basis = "???"

dg_dft = turbomole.read_data_group('dft')
tab = dg_dft.split()
functional = tab[tab.index("functional")+1]

dg_basis = turbomole.read_data_group('basis')
dg_basis = re.sub(r'#.*\n', "", dg_basis)
basis = re.findall(r'\*\n(.*?)\n\*\n', dg_basis)

if len(basis)>1:
    b=re.search(r'\ .*',basis[0])[0]
    for i in range(1,len(basis)):
        if re.search(r'\ .*',basis[i])[0] != b:
            b='mixed'
            break
    if b!='mixed':
        basis = b.strip()

print(basis, functional)
