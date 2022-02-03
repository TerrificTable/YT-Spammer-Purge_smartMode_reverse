from base64 import b85decode
import re
utf_16 = "utf-8"


def make_char_set(stringInput, stripLettersNumbers=False, stripKeyboardSpecialChars=False, stripPunctuation=False):
    translateDict = {}
    charsToStrip = " "
    if stripLettersNumbers == True:
        numbersLettersChars = (
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        charsToStrip += numbersLettersChars
    if stripKeyboardSpecialChars == True:
        keyboardSpecialChars = ("!@#$%^&*()_+-=[]\{\}|;':,./<>?`~")
        charsToStrip += keyboardSpecialChars
    if stripPunctuation == True:
        punctuationChars = ("!?\".,;:'-/()")
        charsToStrip += punctuationChars

    for c in charsToStrip:
        translateDict[ord(c)] = None
    translateDict[ord("\ufe0f")] = None

    stringInput = stringInput.translate(translateDict)
    listedInput = list(stringInput)

    return set(filter(None, listedInput))


blackAdWords, redAdWords, yellowAdWords, exactRedAdWords, = [], [], [], []
usernameBlackWords, usernameNovidBlackWords, usernameObfuBlackWords, textExactBlackWords, textUpLowBlackWords = [], [], [], [], []
compiledRegexDict = {
    'usernameBlackWords': [],
    'usernameNovidBlackWords': [],
    'blackAdWords': [],
    'redAdWords': [],
    'yellowAdWords': [],
    'exactRedAdWords': [],
    'usernameRedWords': [],
    'textObfuBlackWords': [],
    'usernameObfuBlackWords': [],
    'textExactBlackWords': [],
    'textUpLowBlackWords': [],
}
spamGenEmoji_Raw = b'@Sl-~@Sl-};+UQApOJ|0pOJ~;q_yw3kMN(AyyC2e@3@cRnVj&SlB@'
usernameBlackWords_Raw = [b'aA|ICWn^M`', b'aA|ICWn>^?c>', b'Z*CxTWo%_<a$#)', b'c4=WCbY*O1XL4a}', b'Z*CxIZgX^DXL4a}', b'Z*CxIX8', b'V`yb#YanfTAY*7@', b'b7f^9ZFwMLXkh', b'c4>2IbRcbcAY*7@',
                          b'cWHEJATS_yX=D', b'cWHEJAZ~9Uc4=e', b'cWHEJZ*_DaVQzUKc4=e', b'X>N0LVP|q-Z8`', b'Z*CxIZgX^D', b'Z*CxIZgX^DAZK!6Z2', b'c4=WCX>N0LVP|q-Z2', b'b9G`gb9G_', b'b9G`MG$3<zVg', b'Z*CxMc_3qGVE']
usernameNovidBlackWords_Raw = [
    b'cWHEJATS_yX=D', b'cWHEJAZ~9Uc4=e', b'cWHEJZ*_DaVQzUKc4=e']
usernameObfuBlackWords_Raw = [b'c4Bp7YjX',
                              b'b|7MPV{3B', b'a&KaFcm', b'a&KaFV{3B']
usernameRedWords = ["whatsapp", "telegram"]
textObfuBlackWords = ['telegram']
textExactBlackWords_Raw = [b'Z*6BRAZ2)AV{~kJAa`hCbRcOUZe?X;Wn=', b'Z*6BRAZ2)AV{~kJAa`hCbRc<ebs%nKWn^V!',
                           b'Z*6BRAZ2)AV{~kJAa`hCbRckLZ*Xj7AZ}%4WMyO', b'ZDnU+ZaN?$Xm50MWpW|']
textUpLowBlackWords_Raw = [
    b'O<5pAPfk=tPE;UCQv', b'Ngz!@OGO}8L0KR|MO0KpQXoT5PE<usQ~', b'O<5pTNkm0YQy@W7MF']

unicodeCategoriesStrip = ["Mn", "Cc", "Cf", "Cs", "Co", "Cn"]
lowAl = b'VPa!sWoBn+X=-b1ZEkOHadLBXb#`}nd3p'

spamGenEmojiSet = make_char_set(
    b85decode(spamGenEmoji_Raw).decode(utf_16))
lowAlSet = make_char_set(b85decode(lowAl).decode(utf_16))
for x in usernameBlackWords_Raw:
    usernameBlackWords.append(b85decode(x).decode(utf_16))
for x in usernameNovidBlackWords_Raw:
    usernameNovidBlackWords.append(b85decode(x).decode(utf_16))
for x in usernameObfuBlackWords_Raw:
    usernameObfuBlackWords.append(b85decode(x).decode(utf_16))
for x in textExactBlackWords_Raw:
    textExactBlackWords.append(b85decode(x).decode(utf_16))
for x in textUpLowBlackWords_Raw:
    textUpLowBlackWords.append(b85decode(x).decode(utf_16))

minNumbersMatchCount = 6
spamNums = b'@4S%jypiv`lJC5e@4S@nyp`{~mhZfm@4T4ryqWL3kng;a@4S-lyp!*|l<&Ni@4S}pyqE91nD4xq-+|(hpyH9V;*yBsleOZVw&I?E;+~4|pM-+ovAy7_sN#{K;*quDl8NGzw&I<);+}!xo{R9GgoEI*sp65M;*qxEl8WM!x8j|+;+}%yo{aFHgoNO$sp65N;*q!Fl8fS#xZ<6;;+})zo{jLIgoWafq~ejd;*yNwleyxZy5gRM;+~G;o`m9_j_{v^hT@T>;*q)Hl8xe%y5gO?;+}=#o{#XKgoomhrs9#h;*yTyle^-byyBjQ;+~N3k%YbQpM;3vf|%lwr{a;j;*yWzlf2@cz2csS;+~Q4pM;6xk*MO4yyB9O;*-7Noxb9ph~l1-@SlW=;*+Z4lfUqvgp2T>gpBZ?gn{s%gn;m!pN{aIpP2BSpQ7-cpRDkmpO5gJpPBHTpRMqnpQG@dpSJLwpOEmKpPKNUpRVwopQP}epSSRxpONsLpPTTVpRe$ppQZ4fpSbXypOWyMpPcZWpRn+qpQiAgpSkdzpOf&NpPlfXpRw?rpQrGhpStj!pOo;OpPulYpR(|spQ!MipS$p#pOx^PpP%rZpR@3tpQ-SjpS<v$pO)~QpP=xapS19upQ`YkpS|#%pO^5RpP}%bpSAFvpR4elpT6*&pT7'
spamPlus = b';+&e|oSEXDmBO*hmf?`8;(@y2f{NmZlj4Y!;)<2xik{-1wBo0_;-|afsDa|BgyN{8;;5tIsHEbkrQ)cj;;5(MsHozot>UPz;;6aesj=dzvf`|=@42Gyyo=$Rt>S^4;+U!8n5g2IrsA2f;+e7Ho2cTPnc|$9;+&h}oSfpEo#LFH;+&u2oS^EOn(CUH@Sl}{@Sl}|@Sl}}@Sl~2@Sl~3@Sl~4@SmQc@SmQd@SmQe@SmQf@SmQg@SmQh@SmQi'
spamOne = b'@4S)lou7~Jou8TTou8xdou94nou9Yjl8EAywc?$&;+}xwo{I3Fgo59J;*p@@k+c'
x = b85decode(spamNums).decode(utf_16)
y = b85decode(spamPlus).decode(utf_16)
z = b85decode(spamOne).decode(utf_16)

spammerNumbersSet = make_char_set(x)
regexTest1 = f"[{y}] ?[1]"
regexTest2 = f"[+] ?[{z}]"
regexTest3 = f"[{y}] ?[{z}]"
compiledNumRegex = re.compile(
    f"({regexTest1}|{regexTest2}|{regexTest3})")

blackAdWords_Raw = [b'V`yb#YanfTAaHVTW@&5', b'Z*XO9AZ>XdaB^>EX>0', b'b7f^9ZFwMYa&Km7Yy',
                    b'V`yb#YanfTAa-eFWp4', b'V`yb#YanoPZ)Rz1', b'V`yb#Yan)MWMyv', b'bYXBHZ*CxMc>', b'Z*CxMc_46UV{~<LWd']
redAdWords_Raw = [b'W_4q0', b'b7gn', b'WNBk-', b'WFcc~',
                  b'W-4QA', b'W-2OUYX', b'Zgpg3', b'b1HZ', b'F*qv', b'aBp&M']
yellowAdWords_Raw = [b'Y;SgD', b'Vr5}<bZKUFYy', b'VsB)5',
                     b'XK8Y5', b'O~a&QV`yb=', b'Xk}@`pJf', b'Xm4}', b'aCLKYc>']
exactRedAdWords_Raw = [
    b'EiElAEiElAEiElAEiElAEiElAEiElAEiElAEiElAEiElAEiElAEiC', b'Wq4s@bZmJbcW7aBAZZ|OWo2Y#WB']
redAdEmoji = b85decode(b'@Sl{P').decode(utf_16)
yellowAdEmoji = b85decode(
    b'@Sl-|@Sm8N@Sm8C@Sl>4@Sl;H@Sly0').decode(utf_16)
hrt = b85decode(
    b';+duJpOTpHpOTjFpOTmGpOTaCpOTsIpOTvJpOTyKpOT#LpQoYlpOT&MpO&QJouu%el9lkElAZ').decode(utf_16)

for x in blackAdWords_Raw:
    blackAdWords.append(b85decode(x).decode(utf_16))
for x in redAdWords_Raw:
    redAdWords.append(b85decode(x).decode(utf_16))
for x in yellowAdWords_Raw:
    yellowAdWords.append(b85decode(x).decode(utf_16))
for x in exactRedAdWords_Raw:
    exactRedAdWords.append(b85decode(x).decode(utf_16))


print("----------------WORDS----------------")
print(blackAdWords)
print(redAdWords)
print(yellowAdWords)
print(exactRedAdWords)

print("\n----------------USERNAMES----------------")
print(usernameBlackWords)
print(usernameNovidBlackWords)
print(usernameObfuBlackWords)
print(textExactBlackWords)
print(textUpLowBlackWords)

print("\n----------------EMOJIS----------------")
print(redAdEmoji)
print(spamGenEmojiSet)
print(yellowAdEmoji)


print("\n----------------OTHER----------------")
print(hrt)
print(compiledNumRegex)
