import numpy as np

def main():

    arrayList = ""
    maxDiameter = 32

    for i in range(1, maxDiameter + 1):
        array = func(i)
        arrayString = str(array).replace("[[", "{\n\t{").replace("[", "{").replace("], ","},\n\t").replace("]]","}}").replace("False","false").replace("True","true")
        arrayList += """
    public static boolean[][] circle{num} = {array};
    """.format(num=i,array=arrayString)

    javaCode = """// autogenerated circles by poor penguins and ferrets
public class CircleTables {{
    {getCircleFunction}

    {arrays}
}}
    """
    
    getSwitchCase="""public static boolean[][] getCircleGrid(int diameter) {{
        switch(diameter) {{
            {cases}
            
            default:
                throw new NullPointerException();
        }}
    }}
    """
    
    casesString = generateCases(maxDiameter)
    getSwitchCase = getSwitchCase.format(cases=casesString)

    file = open("CircleTables.java", "w")
    file.write(javaCode.format(arrays=arrayList,getCircleFunction=getSwitchCase))
    file.close()

def func(diameter):
    array = np.zeros((diameter,diameter), dtype=bool).tolist()
    cirCen = diameter / 2
    for x in range(diameter):
        for y in range(diameter):
            if ((x + 0.5 - cirCen)**2 + (y + 0.5 - cirCen)**2 <= cirCen**2):
                array[x][y] = True

    return array

def generateCases(numCircles):
    outStr = ""

    for i in range(1, numCircles + 1):
        outStr += "case {i}:\n\t\t\t\treturn circle{i};\n\t\t\t".format(i=i)
    
    return outStr
main()
