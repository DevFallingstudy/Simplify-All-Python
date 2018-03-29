import BlankSpaceChecker

if __name__ == '__main__':

    testStr = input('텍스트를 입력해주세요 >> ')
    resultStr = BlankSpaceChecker.checkSpace(testStr)
    simpleStr = ''
    # print()

    list_words = resultStr.split(" ")

    # print(list_words)

    for each_str in list_words:
        simpleStr += each_str[0]

    print('줄임 결과 >> {}'.format(simpleStr))
    # print(simpleStr)