from random import randint as RandomInt

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def power(x, y):
    return x ** y

def inverseStr(x: str):
    return x[::-1]

class Binary:
    def binary(x):
        if type(x) == str:
            binary_representation = ''.join(format(ord(char), '08b') for char in x)
            return binary_representation
        elif type(x) == int:
            strBin = f"{bin(x)[2:]}"
            intBin = int(strBin)
            return intBin
        else:
            raise ValueError("Expected a value of a string or integer.")

    def debinary(x):
        if type(x) == str:
            binary_chunks = [x[i:i+8] for i in range(0, len(x), 8)]
            characters = [chr(int(binary_chunk, 2)) for binary_chunk in binary_chunks]
            return ''.join(characters)
        elif type(x) == int:
            strBin = str(x)
            intBin = int(strBin, 2)
            return intBin
        else:
            raise ValueError("Expected a value of a string or integer.")

def getPos(foreveryk: int, SerializedString: str):
    return int(len(SerializedString) / foreveryk)

class Serialize:
    def serialize(x, serializeType: str):
        if type(x) == int and serializeType == "n":
            serializeBinaryStr = ""
            for char in str(x):
                if serializeType == "n":
                    if char == "1":
                        serializeBinaryStr += "NUL"
                    elif char == "0":
                        serializeBinaryStr += "EGT"
                    else:
                        raise ValueError("Expected Binary")
            return serializeBinaryStr
        elif type(x) == str and serializeType == "t":
            returnTStr = ""
            k = 8
            #global alphabetSerialize
            alphabetSerialize = {"space": "NUL", 
                        "a": "AGT", "b": 
                        "BUP", "c": 
                        "CPT", "d": 
                        "DWY", "e": 
                        "EPK", "f": 
                        "FQI", "g": 
                        "GKX", "h":
                        "HUI", "i":
                        "IGL", "j":
                        "JBV", "k":
                        "KBT", "l":
                        "LQO", "m":
                        "MAL", "n":
                        "NYT", "o":
                        "ODP", "p":
                        "PAU", "q":
                        "QBU", "r":
                        "RKO", "s":
                        "SNB", "t":
                        "TQO", "u":
                        "UBZ", "v":
                        "VKL", "w":
                        "WIX", "x":
                        "XOH", "y":
                        "YZN", "z":
                        "ZIA"}
            for _ in range(getPos(k, x)):
                if x.endswith("00100000"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["space"]
                elif x.endswith("01100001"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["a"]
                elif x.endswith("01100010"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["b"]
                elif x.endswith("01100011"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["c"]
                elif x.endswith("01100100"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["d"]
                elif x.endswith("01100101"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["e"]
                elif x.endswith("01100110"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["f"]
                elif x.endswith("01100111"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["g"]
                elif x.endswith("01101000"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["h"]
                elif x.endswith("01101001"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["i"]
                elif x.endswith("01101010"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["j"]
                elif x.endswith("01101011"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["k"]
                elif x.endswith("01101100"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["l"]
                elif x.endswith("01101101"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["m"]
                elif x.endswith("01101110"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["n"]
                elif x.endswith("01101111"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["o"]
                elif x.endswith("01110000"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["p"]
                elif x.endswith("01110001"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["q"]
                elif x.endswith("01110010"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["r"]
                elif x.endswith("01110011"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["s"]
                elif x.endswith("01110100"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["t"]
                elif x.endswith("01110101"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["u"]
                elif x.endswith("01110110"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["v"]
                elif x.endswith("01110111"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["w"]
                elif x.endswith("01111000"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["x"]
                elif x.endswith("01111001"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["y"]
                elif x.endswith("01111010"):
                    x = x[:-k]
                    returnTStr += alphabetSerialize["z"]
                else:
                    raise ValueError("Invalid Binary Text")
                    
            return str(returnTStr)
    def deserialize(x, serializeType: str):
        if serializeType == "n" and type(x) == str:
            returnStr = ""
            intStr = None
            for _ in range(getPos(3, x)):
                if x.endswith("NUL"):
                    x = x[:-3]
                    returnStr += "1"
                elif x.endswith("EGT"):
                    x = x[:-3]
                    returnStr += "0"
            intStr = int(returnStr[::-1])
            return intStr
        elif serializeType == "t" and type(x) == str:
            returnStr = ""
            alphabetSerialize = {"space": "NUL", 
                        "a": "AGT", "b": 
                        "BUP", "c": 
                        "CPT", "d": 
                        "DWY", "e": 
                        "EPK", "f": 
                        "FQI", "g": 
                        "GKX", "h":
                        "HUI", "i":
                        "IGL", "j":
                        "JBV", "k":
                        "KBT", "l":
                        "LQO", "m":
                        "MAL", "n":
                        "NYT", "o":
                        "ODP", "p":
                        "PAU", "q":
                        "QBU", "r":
                        "RKO", "s":
                        "SNB", "t":
                        "TQO", "u":
                        "UBZ", "v":
                        "VKL", "w":
                        "WIX", "x":
                        "XOH", "y":
                        "YZN", "z":
                        "ZIA"}
            for _ in range(getPos(3, x)):
                if x.endswith(alphabetSerialize["space"]):
                    x = x[:-3]
                    returnStr += "00100000"
                if x.endswith(alphabetSerialize["a"]):
                    x = x[:-3]
                    returnStr += "01100001"
                elif x.endswith(alphabetSerialize["b"]):
                    x = x[:-3]
                    returnStr += "01100010"
                elif x.endswith(alphabetSerialize["c"]):
                    x = x[:-3]
                    returnStr += "01100011"
                elif x.endswith(alphabetSerialize["d"]):
                    x = x[:-3]
                    returnStr += "01100100"
                elif x.endswith(alphabetSerialize["e"]):
                    x = x[:-3]
                    returnStr += "01100101"
                elif x.endswith(alphabetSerialize["f"]):
                    x = x[:-3]
                    returnStr += "01100110"
                elif x.endswith(alphabetSerialize["g"]):
                    x = x[:-3]
                    returnStr += "01100111"
                elif x.endswith(alphabetSerialize["h"]):
                    x = x[:-3]
                    returnStr += "01101000"
                elif x.endswith(alphabetSerialize["i"]):
                    x = x[:-3]
                    returnStr += "01101001"
                elif x.endswith(alphabetSerialize["j"]):
                    x = x[:-3]
                    returnStr += "01101010"
                elif x.endswith(alphabetSerialize["k"]):
                    x = x[:-3]
                    returnStr += "01101011"
                elif x.endswith(alphabetSerialize["l"]):
                    x = x[:-3]
                    returnStr += "01101100"
                elif x.endswith(alphabetSerialize["m"]):
                    x = x[:-3]
                    returnStr += "01101101"
                elif x.endswith(alphabetSerialize["n"]):
                    x = x[:-3]
                    returnStr += "01101110"
                elif x.endswith(alphabetSerialize["o"]):
                    x = x[:-3]
                    returnStr += "01101111"
                elif x.endswith(alphabetSerialize["p"]):
                    x = x[:-3]
                    returnStr += "01110000"
                elif x.endswith(alphabetSerialize["q"]):
                    x = x[:-3]
                    returnStr += "01110001"
                elif x.endswith(alphabetSerialize["r"]):
                    x = x[:-3]
                    returnStr += "01110010"
                elif x.endswith(alphabetSerialize["s"]):
                    x = x[:-3]
                    returnStr += "01110011"
                elif x.endswith(alphabetSerialize["t"]):
                    x = x[:-3]
                    returnStr += "01110100"
                elif x.endswith(alphabetSerialize["u"]):
                    x = x[:-3]
                    returnStr += "01110101"
                elif x.endswith(alphabetSerialize["v"]):
                    x = x[:-3]
                    returnStr += "01110110"
                elif x.endswith(alphabetSerialize["w"]):
                    x = x[:-3]
                    returnStr += "01110111"
                elif x.endswith(alphabetSerialize["x"]):
                    x = x[:-3]
                    returnStr += "01111000"
                elif x.endswith(alphabetSerialize["y"]):
                    x = x[:-3]
                    returnStr += "01111001"
                elif x.endswith(alphabetSerialize["z"]):
                    x = x[:-3]
                    returnStr += "01111010"
            return returnStr