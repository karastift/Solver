import re
def convertString(text: str) -> dict:
    result = dict()
    string = text
    string = string.split(sep=' ')
    alphabet = 'qwertzuiopasdfghjklöäüyxcvbnm'
    for i in range(0, len(string), 2):
        result[string[i]] = dict()
        curr = result[string[i]]
        sweet = string[i+1]
        valueType = re.sub('0', 'o', re.sub('[=]', '', sweet[:2]).lower())
        value = re.sub('[,]', '.', re.sub('[oO]', '0', sweet[sweet.index('=')+1:])).lower()
        if value[-3] in alphabet:
            value = value[:len(value) - 3]
        elif value[-2] in alphabet:
            value = value[:len(value) - 2]
        elif value[-1] in alphabet:
            value = value[:len(value) - 1]
        else: pass
        
        result[string[i]] = {
            valueType: value
        }

    return result

print(convertString('a) r=39cm c) V=980cm3 e) A0=5oooodm2 g) AO=35m2 b) AO=26OCm2 d) Ao=1985,96m2 f) r=O,71m h) V=36m3'))