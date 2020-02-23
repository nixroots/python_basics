pip install wikipedia

import wikipedia
print(wikipedia.search("Bill"))
print(wikipedia.suggest("Bill cliton"))    # Output: bill clinton
print(wikipedia.summary("Ubuntu"))         #print(wikipedia.summary("Ubuntu", sentences=2))

print(wikipedia.summary("key"))            # code throws a DisambiguationError since there are many articles that would match "key".
                                           # print(wikipedia.summary("Key (cryptography)"))
                                
wikipedia.page("Ubuntu")                   # full wikipedia page
print(wikipedia.page("Python").content)    # just plain text. Excludes images 
print(wikipedia.page("Python").url)        # extract URLs

print(wikipedia.page("ubuntu").images[0])  # get the first image

