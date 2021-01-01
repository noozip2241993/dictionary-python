"""Write a Python script to merge two Python dictionaries"""
def merging(d1,d2):
    d3={}
    for k in (d1,d2):d3.update(k)
    print(d3)
def main():
    dic1 = {number:number*10 for number in range(1,6)}
    dic2 = {number:number*5 for number in range(7,10)}
    merging(dic1,dic2)


main()