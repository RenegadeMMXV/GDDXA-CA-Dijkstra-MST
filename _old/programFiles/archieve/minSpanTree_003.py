#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	18/09/2018
#	@description	'Statistics, Algorithms, and AI' Python implementation of 
#					'Dijkstra's Minimum Spanning Tree' algorithm
#	@version		1.0.1

import GraphTools

def createGraph():
	fileName = 'customGraph'
	GraphTools.printGraphData(fileName)


def createGraph(fileName):
	GraphTools.printGraphData(fileName)

def main():
	nodes = 0

	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		createGraph(GraphTools.customFile())
		#main()

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		createGraph(fileName)
		#valuesFile = open(fileName+'.csv','r')
		#fileFormat = valuesFile.readline().rstrip()
		#nodes = int(valuesFile.readline())
		#print('File Format: %r\nNodes: %r' % (fileFormat,nodes))

		#valuesFile.close()

main()