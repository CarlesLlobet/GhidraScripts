import ghidra.framework.Platform

fileinput=open("/root/ghidra_scripts/functions.txt","r")
fileoutput=open("/root/ghidra_scripts/functions_out.txt","w")
separator = "*"

def printAndWrite(line):
	print(line)
	fileoutput.write(line+"\n")

def readFunctions():
	return fileinput.read().split()

def recursiveRef(depth, references):
	depth += 1
	for i in range(len(references)):
		refaddr=references[i].getFromAddress()
		if references[i].getReferenceType().getName()=="UNCONDITIONAL_CALL":
			references2=getReferencesTo(getFunctionBefore(refaddr).getEntryPoint())
			if references2 != None:
				printAndWrite((depth+1)*separator+str(getFunctionBefore(refaddr)))
				recursiveRef(depth, references2)	
			else:
				depth -=1
				return
				
def run(name,addr):
	printAndWrite("*"+name)
	references=getReferencesTo(addr)
	recursiveRef(0,references)


if __name__ == "__main__":
	iterator = currentProgram.getFunctionManager().getFunctions(True)
	functions=readFunctions()
	for function in iterator:
		name = function.getName()
		if name in functions:
			run(name,function.getEntryPoint())
	fileinput.close()
	fileoutput.close()