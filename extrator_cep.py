endereco = "Rua dos Bobos 1234, Apartamento 1002, São Paulo, SP, 02548-069"

# Regular Expressions -- RegEx

import re

patter = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = patter.search(endereco) #Match


if busca:
    cep = busca.group()
    print(cep)






