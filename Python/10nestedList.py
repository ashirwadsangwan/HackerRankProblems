if __name__ == '__main__':
        marksheet=[]
        scorelist=[]
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 
        
        for a,c in sorted(marksheet):
             if c==b:
                    print(a)
