from collections import Counter
import sys

c = sys.stdin.read()
c = c.splitlines()

def diffPerce(a, b):
    a="/".join(a.split("/")[3:])
    b="/".join(b.split("/")[3:])
    a = a.split("?")[0]
    b = b.split("?")[0]
    n = 0
    r1=""
    r2=""
    for i in range(min([a.count("/"), b.count("/")])): 
        if a.split("/")[i] != b.split("/")[i]:
            n = n + 1
            r1 = a.split("/")[i]
            r2 = b.split("/")[i]
            
    #True = keep, False = Remove from list.
    #Case 1: If there is more than one path that isn't exact then not similar.
    if n > 1:
        return True

    #Case 2: If path length exceeds 29 characters then it is similar if not then not similar.
    elif n == 1:

        if (len(r1) > 29) and (len(r2) > 29):
            return False
        else:
            return True
        
    #Case 3: If exact path then similar and count is equal then similar else false.
    elif n == 0:
        if a.count("/") == b.count("/"):
            return False
        else:
            return True

def lxl(clist, level):
    c=clist
    level = 7
    for i in range(level, len(c)-1):
        url=c[i]
        if url == "":
            continue
        for layer in range(1,level):
            url2 = c[i-level+layer]
            r=diffPerce(url, url2)
            if not r:
                c[i-level+layer] = ""
    c = list(filter(None, c))
    return c
"""
def stack(n, c, level):
    for i in range(n):
        c=lxl(c, level)
    return c
"""
c=lxl(c, 5)
c=lxl(c, 1000)
c=lxl(c, len(c)-1)



bl = ["\\","undefined",".webm","text/javascript","!","==",";","..","(", ")","*",":",".pdf",".xml",".ttf",".js",".css",".jpg",".jpeg",".icon",".png",".gif",".webp",".bmp",".tif",".tiff",".ico",".svg",".woff2",".woff"]

for u in range(len(c)):
    if ("&" in "/".join(c[u].split("/")[3:])) and ("?" not in "/".join(c[u].split("/")[3:])):
        c[u] = ""
    if len("/".join(c[u].split("/")[3:])) < 4:
        if "," in "/".join(c[u].split("/")[3:]):
            c[u] = ""
    for s in bl:
        if s in "/".join(c[u].split("/")[3:]):
            c[u] = ""
            break
c = list(filter(None, c))

def freq(c): # un used anymore
    x=[]
    y=[]
    done=[]
    for u in c:
        u="/".join(u.split("/")[3:])
        u = u.split("?")[0]
        s=u.split("/")[-1]
        if s == "":
            if len(u.split("/")) > 1:
                s = u.split("/")[-2]
        x.append(s)

    for t in list(Counter(x).most_common()):
        if t[1] > 4:
            if "index" not in t[0]:
                y.append(t[0])
    
    for i in range(len(c)):
        u=c[i]
        u="/".join(u.split("/")[3:])
        u = u.split("?")[0]
        s=u.split("/")[-1]
        if s == "":
            if len(u.split("/")) > 1:
                s = u.split("/")[-2]
        for b in y:
            if b == s:
                if b not in done:
                    done.append(b)
                if b in done:
                    c[i]=""
    c = list(filter(None, c))
    return c
    
#c=freq(c)

def freq2(c):
    newDirs = []
    let = 4
    for u in c:
        u="/".join(u.split("/")[3:]) # remove domain and keep path
        u = u.split("?")[0] # remove params
        d = u.split("/") # split path
        d = list(filter(None, d)) # remove white spaces (double paths and last path)
        for p in range(len(d)): 
            newDir = d[p] + "*" + str(p) + "*" + str(len(d)) # build mapper, separator = *, 
            newDirs.append(newDir)# First value = path, second = dir order, third = total number of dirs 

    mapper = list(Counter(newDirs).most_common()) # change counter to list e.g., (path map, frequancy)
    for m in mapper:
        lett = let
        if m[1] > let:# if frequancy is more than four, (let more than four exist).
            struct = m[0].split("*") # split the mapped path
            for uu in range(len(c)):
                u = c[uu]
                u="/".join(u.split("/")[3:])
                u = u.split("?")[0]
                d = u.split("/")
                d = list(filter(None, d))
                for p in range(len(d)):
                    newDir = d[p] + "*" + str(p) + "*" + str(len(d))
                    newDir = newDir.split("*")
                    if struct == newDir:
                        if lett > 0:
                            lett = lett -1
                        else:
                            c[uu] = ""
    c = list(filter(None, c))
    return c
                            
                        
            
            
    
c=freq2(c)

print("\n".join(c))










