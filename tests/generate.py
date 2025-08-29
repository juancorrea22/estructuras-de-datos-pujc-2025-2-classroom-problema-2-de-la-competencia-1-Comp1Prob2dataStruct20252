#!/usr/bin/env python3
import random, os; random.seed(43)
def w(name, n, arr):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(str(n)+"\n"+" ".join(map(str,arr))+"\n")
    open(f"tests/output_{name}.txt","w").write(" ".join(map(str,arr[::-1]))+"\n")
def main():
    w("min", 1, [7])
    n=2*10**5; w("max", n, list(range(1,n+1)))
    n=17; w("rnd", n, [random.randint(-50,50) for _ in range(n)])
if __name__=="__main__": main()
