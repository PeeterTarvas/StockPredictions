import string

def checkDetailsAreValid(accountNumber:str, bankCode:str):
    print(accountNumber)

    accountNumber = accountNumber.replace(" ", "")
    accountNumber = calcCorrectAccountNr(accountNumber)
    bankCode = bankCode.replace(" ", "")

    if isValidBankCode(bankCode) and isValidAccountNumber(accountNumber):
        concatenatedNR = accountNumber + bankCode
        # remove checksum
        temp_list = concatenatedNR.split("-")
        checksum = temp_list[0]
        concatenatedNR = temp_list[1]
        checksumCalulated = calcWeights(concatenatedNR)
        return str(checksumCalulated)
    return ""

def split(word):
    return [char for char in word]

def calcWeights(concatedNR: str):
    checksum = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    inx_dict:dict = {1: 7, 2: 3, 3: 1, 4:5 ,5:2, 6:4, 7:8, 8:6, 9:1, 10: 6, 11:5}
    concatedNR = split(concatedNR)
    for enum, i in enumerate(concatedNR):
        if i.isdecimal():
            print(f"{int(i)} * {inx_dict.get(enum + 1)}")
            checksum += int(i) * inx_dict.get(enum + 1)
        elif i.isalpha():
            print(f"{(alphabet.index(i.lower())) + 10} * {inx_dict.get(enum + 1)}")
            checksum += (alphabet.index(i.lower()) + 10) * inx_dict.get(enum + 1)
    print(checksum)
    if checksum % 2 == 0:
        return checksum % 89
    else:
        return 89 - (checksum % 89)


def calcCorrectAccountNr(accountNr):
    if '-' in accountNr and len(accountNr.split("-")[0]) < 2:
        return "0" + accountNr
    return accountNr

def isValidBankCode(bankCode):
    if len(bankCode) == 4:
        characters = bankCode[:2]
        numbers = bankCode[2:4]
        return characters.isalpha() and numbers.isdecimal()
    return False

def isValidAccountNumber(accountNr):
    if "-" in accountNr:
        temp_list = accountNr.split("-")
        if len(temp_list[0]) == 2 and len(temp_list[1]) == 7:
            return temp_list[0].isdecimal() and temp_list[1].isdecimal()
    return False



if __name__ == '__main__':
    a = "11-0007395"
    bank = "XX55"
    print(checkDetailsAreValid(a, bank))