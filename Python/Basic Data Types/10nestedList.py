if __name__ == '__main__':
        marksheet=[]
        scorelist=[]
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        second_lowest = sorted(list(set(scorelist)))[1]
        
        for student, marks in sorted(marksheet):
             if marks == second_lowest:
                    print(student)
