import numpy as np
import sys
import argparse

def handleInput():

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--minimum", 
                        required=False, type=int, default=1,
                        help="The smallest circle's diameter (Default: 1)")
    parser.add_argument("-x", "--maximum",
                        required=False, type=int, default=32,
                        help="The biggest circle's diameter (Default: 32)")

    args = parser.parse_args()

    if args.minimum >= args.maximum:
        print("Minimum cannot be greater than or equal to maximum")
        sys.exit(1)

    generateFile(args.minimum, args.maximum)
    

def generateFile(smallCircDiam, bigCircDiam):
    
    strArrList = ""
    for i in range(smallCircDiam, bigCircDiam + 1):
        strArrJava = arrToJavaCode(func(i))
        strArrList += "\tpublic static boolean[][] circle{num} = {array};\n\n".format(num=i,array=strArrJava)
    
    generatedCases = generateCases(smallCircDiam, bigCircDiam)

    caseWrapper = "public static boolean[][] getCircleGrid(int diameter) throws NullPointerException {"
    caseWrapper += "\n\t\tswitch(diameter) {"
    caseWrapper += "\n\t{cases}".format(cases=generatedCases)
    caseWrapper += "\n"
    caseWrapper += "\n\t\t\tdefault:"
    caseWrapper += "\n\t\t\t\tthrow new NullPointerException();"
    caseWrapper += "\n\t\t}"
    caseWrapper += "\n\t}"

    #generatedCases = generateCases(smallCircDiam, bigCircDiam)
    #caseWrapper.format(cases=generatedCases)

    strJavaWrapper = "// autogenerated circles by poor penguins and ferrets"
    strJavaWrapper += "\npublic class CircleTables {{"
    strJavaWrapper += "\n{switchCase}"
    strJavaWrapper += "\n"
    strJavaWrapper += "\n{arrays}"
    strJavaWrapper += "\n}}"

    file = open("CircleTables.java", "w")
    file.write(strJavaWrapper.format(arrays=strArrList,switchCase=caseWrapper))
    file.close()

def func(diameter):
    array = np.zeros((diameter,diameter), dtype=int).tolist()
    centerCirc = diameter / 2
    for x in range(diameter):
        for y in range(diameter):
            if ((x + 0.5 - centerCirc)**2 + (y + 0.5 - centerCirc)**2 <= centerCirc**2):
                array[x][y] = 1

    return array

def generateCases(smallCircDiam, bigCircDiam):
    outStr = ""

    for i in range(smallCircDiam, bigCircDiam + 1):
        if i == smallCircDiam:
            outStr += "\t\t\tcase {i}:\n\t\t\t\treturn circle{i};".format(i=i)
        else:
            outStr += "\n\t\t\tcase {i}:\n\t\t\t\treturn circle{i};".format(i=i)
    
    return outStr

def arrToJavaCode(array):
    arrayString = str(array).replace("[[", "{\n\t\t{").replace("[", "{").replace("], ","},\n\t\t").replace("]]","}\n\t}")
    return arrayString

handleInput()
