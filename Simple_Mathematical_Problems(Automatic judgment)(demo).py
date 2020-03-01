import random
list_answer1 = []
list_answer2 = []
list_worng = []
list_right = []
list_proplem = []


class main(object):
    def __init__(self,x_value,y_value,proplem_number):
        self.x_value = x_value
        self.y_value = y_value
        self.problem_number = proplem_number
        self.point = 0

    def Addition(self):
        self.x_value = int(random.randint(1,10))
        self.y_value = int(random.randint(1,10))
        Answer_value = self.y_value+self.x_value
        list_answer1.append(Answer_value)
        list_proplem.append(str(self.x_value) + ' + ' +str(self.y_value)+ ' = ' )
    #def show_Addition(self):
    #    return "{} + {} =".format(self.x_value,self.y_value)

    def Settlement_point(self):

        for i in range(0,number):
            if list_answer1[i] != list_answer2[i]:
                list_worng.append(i)
            else:
                self.point += 1
                list_right.append(i)

        return self.point


if __name__ == '__main__':
    number = int(input('你想多少题（加法）：'))
    start = main(0,0,number)
    for i in range(0,number):
        start.Addition()

    for i in range(0,number):
        j = i+1
        print(str(j) + '.   ' + list_proplem[i],end='')
        Answer = int(input())
        list_answer2.append(Answer)
    print('你的得分为：' + str(start.Settlement_point()))
    print('你做对的题有:')
    for i in list_right:
        j = i + 1
        print(str(j) + '.   ' + list_proplem[i])

    print('你做错的题有:')
    for i in list_worng:
        j = i + 1
        print(str(j) + '.   ' + list_proplem[i])

