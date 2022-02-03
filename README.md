# [ThioJoe's YT-Spammer-Purge](https://github.com/ThioJoe/YT-Spammer-Purge/) Smart Mode "reverse"
He encoded everything with base85 and imported it as base64 (smart)
These are just some (or all idk) blacklisted words, emojis, usernames and... idk what the fuck the regex.compile thingy is (if anyone knows pls make an issue or write me on discord TerrificTable55#6998)

Output:
```
----------------WORDS----------------
['check my profil', 'open my profil', 'see my profil', 'check my video', 'check profil', 'check video', 'tap on my', 'on my picture']
['fuck', 'sex', 'dick', 'd!ck', 'f*ck', 'f**ck', 'nude', 's*x', '18+', 'porn']
['love', 'beautiful', 'body', 'girl', 'Mädchen', 'heiße', 'hot', 'pussy']
['------------------------------------------', 'exactly what i needed']

----------------USERNAMES----------------
['pinnedby', 'pinned by', 'on telegram', 'via telegram', 'on instagram', 'on ig', 'check my cha', 'see my cha', 'visit my cha', 'with 0 vid', 'with no vid', 'without any vid', 'instagram:', 'on insta', 'on insta gram', 'via instagram', 'sub4sub', 'sub 4 sub', 'on my cha']
['with 0 vid', 'with no vid', 'without any vid']
['vbucks', 'v bucks', 'robux', 'robucks']
['omg, exactly what i needed', 'omg, exactly what you needed', 'omg, exactly what people needed', 'megan: "hotter"']
['MY CONTENT IS', 'I MAKE WAY BETTER CONTENT', 'MY VIDEOS ARE']

----------------EMOJIS----------------
🔞
{'👆', '⬆', '👈', '♜', '👇', '⤵', '💬', '👉', '🔼', '☝'}
👅😘😍💋👙🍌
♥💘💖💗💓💙💚💛💜🧡💝🖤❤💕💞

----------------OTHER----------------
re.compile('([✚✙➕±˖ᐩ⁺₊∓∔⊕⊞⟴⧺⧻⨁⨄⨢⨣⨤⨥⨦⨧⨨⨭⨮⨹⩱⩲⬲﹢＋᛭⁜☩☨☦♰♱⛨✙✚✛✜✝✞✟✠Ꚛꚛ🕀🕁🕂🕆🕇🕈🞡🞢🞣🞤🞥🞦🞧] ?[1]|[+]              ?[１𝟏𝟙𝟣𝟭𝟷⒈⓵❶➀➊🄂߁①⑴]|[✚✙➕±˖ᐩ⁺₊∓∔⊕⊞⟴⧺⧻⨁⨄⨢⨣⨤⨥⨦⨧⨨⨭⨮⨹⩱⩲⬲﹢＋᛭⁜☩☨☦♰♱⛨✙✚✛✜✝✞✟✠Ꚛꚛ🕀🕁🕂🕆🕇🕈🞡🞢🞣🞤🞥�                 🞧]] ?[１𝟏𝟙𝟣𝟭𝟷⒈⓵❶➀➊🄂߁①⑴]       
)')
```
