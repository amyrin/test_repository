# takes in a .txt file and returns a list string-ified functions
def getFunctionStrings(file):
    f = open(file, "r")
    functions = []
    firstFunction = True
    isFunction = False
    linesList = f.readlines()
    for line in linesList:
        if line.startswith("def"):
            if firstFunction:
                isFunction = True
                function = line
                firstFunction = False
            else:
                functions += [function]
                isFunction = True
                function = line
        elif isFunction and line.startswith("\t"):
            function += line
            if line == linesList[-1]:
                functions += [function]
        elif isFunction and not line.startswith("\t"):
            isFunction = False
    for i in range(len(functions)):
        if functions[i][-1] == "\n":
            functions[i] = functions[i][:-1]
    return functions

# print(functions)
# count = 0
# for fun in functions:
#     count += 1
#     print("fun %d:" % count, fun)


# takes in a list of string-ified functions and executes them
newGlobals = dict()
def execute(lst):
    for item in lst:
        exec(item, newGlobals)
        result = newGlobals['testFunction1']()
        print(result)


functionStrings = getFunctionStrings("test2.txt")
execute(functionStrings)

