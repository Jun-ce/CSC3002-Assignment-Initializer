def createQuestionFile(n):
    """
    initialize a qn.cpp and a qn.h files
    :param n: number for questions
    :return: null
    """
    cpp = open('q'+str(n)+'.cpp','w')
    cppTemplateFile = open('cpp.txt', 'r')
    cppText = cppTemplateFile.read()
    cppText = cppText.replace('?', str(n))
    cpp.write(cppText)
    cpp.close()

    h = open('q'+str(n)+'.h','w')
    hTemplateFile = open('h.txt', 'r')
    hText = hTemplateFile.read()
    hText = hText.replace('?', str(n))
    h.write(hText)
    h.close()

    return 0

def createMainFile(n):
    """
    initialize a main cpp including n .h files
    :param n: number for questions
    :return: null
    """
    main = open('hello.cpp', 'w')
    mainTemplateFile = open('main.txt', 'r')
    mainText = mainTemplateFile.read()
    for i in range(1,n+1):
        mainText = '#include "q' + str(i) + '.h"\n' + mainText
    main.write(mainText)
    main.close()
    return 0

no = int(input("Enter the total number of questions:"))
for i in range(no):
    createQuestionFile(i+1)
createMainFile(no)