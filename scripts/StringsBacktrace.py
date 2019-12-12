import ghidra.framework.Platform
from ghidra.program.util import DefinedDataIterator

fileinput=open("/root/ghidra_scripts/strings.txt","r")
fileoutput=open("/root/ghidra_scripts/strings_out.txt","w")
separator = "*"

def printAndWrite(line):
	print(line)
	fileoutput.write(line+"\n")

def readStrings():
	return fileinput.read().split()

def recursiveRef(depth, references, funcFrom):
	depth += 1
	for i in range(len(references)):
		refaddr=references[i].getFromAddress()
		if references[i].getReferenceType().getName()=="DATA":
			references2=getReferencesTo(getFunctionBefore(refaddr).getEntryPoint())
			if references2 != None:
				if str(funcFrom)!=str(getFunctionBefore(refaddr)):
					printAndWrite((depth+1)*separator+str(getFunctionBefore(refaddr)))
					function=getFunctionBefore(refaddr)
					recursiveRef(depth, references2, function)
				else:
					break
			else:	
				depth-=1
				return
				
def run(name,addr):
	printAndWrite("*"+name)
	references=getReferencesTo(addr)
	recursiveRef(0,references, None)

if __name__ == "__main__":
	iterator = DefinedDataIterator.definedStrings(currentProgram,None)
	strings=readStrings()
	for string in iterator:
		value=string.value
		if value in strings:
			run(value,string.address)
	fileinput.close()
	fileoutput.close()