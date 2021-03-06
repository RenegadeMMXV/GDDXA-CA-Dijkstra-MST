'''	@author			Ciaran Bent [K00221230]
	@creationDate	18/09/2018
	@description	'Statistics, Algorithms, and AI' Python containing
					several utilities used in the 'minSpanTree.py' program.
	@version		1.2.0
	@deadline		12/10/2018
'''

import random

#################################
#			OBJECTS				#
#################################

'''	@descr	- An object to represent a node connection in a Graph.
	@param	- 
			n1	- The node FROM
			n2	- The node TO
			wt	- The connection WEIGHT
	@funct	-
			nodeFrom 	- INTEGER iterator assigned to the PREVIOUS node
			nodeTo 		- INTEGER iterator assigned to the NEXT node
			edgeWeight	- INTEGER value assigned to the WEIGHT of this connection
'''
class Connection:
	def __init__(self,n1,n2,wt):
		self.node1 = n1
		self.node2 = n2
		self.weight = wt

	def nodeFrom(self):
		return(self.node1)

	def nodeTo(self):
		return(self.node2)

	def edgeWeight(self):
		return(self.weight)

#################################
#			FUNCTIONS			#
#################################

'''	@descr	- Reads a '.csv' file and creates a 'Graph' object based on the contents.
	@param	-
		fileName 	- The STRING name of the name of the input '.csv' file.
'''
def compileGraph(fileName): 			#EXAMINE LECTURE 5 - PG. 58
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())

	graph = []

	for line in out.readlines():
		
		u = line.split(',')[0]
		v = line.split(',')[1]
		w = line.rstrip().split(',')[2]
		graph.append(Connection(u,v,w))

	out.close()

	return(graph)

'''	@descr	- Prints all connections in a '.csv' file
	@param	-
		fileName	- The STRING name of the name of the input '.csv' file.
'''
def getFileNodeCount(fileName):
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())
	out.close()

	return(nodes)


'''	@descr 		- Prints all connections in a '.csv' file
	@param -
		fileName 	- The STRING name of the name of the input '.csv' file.
'''
def printGraphData(fileName):
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())
	print('File Format: %r\nNodes: %r' % (fileFormat,nodes))

	for line in out.readlines():
		u = line.split(',')[0]
		v = line.split(',')[1]
		w = line.rstrip().split(',')[2]
		print('%r,%r,%r' % (u,v,w))

	out.close()

'''	@descr 		- Generates a '.csv' file based in input values.
	@param -
		fileName 	- The STRING name to assign to the generated file
		nodeMin 	- 
		nodeMax 	- 
		conns 		- 
		wt 			- 
'''
def generateFile(fileName,nodeMin,nodeMax,conns,wt):
	random.seed()
	nodes = random.randint(nodeMin,nodeMax)
	out = open(fileName + '.csv','w')
	out.write('s\n%r\n' % nodes)

	for x in range(conns):
		u = random.randint(0,nodes)
		v = random.randint(0,nodes)
		w = random.randint(1,wt)
		out.write('%r,%r,%r\n' % (u,v,w))

	out.close()

'''	@descr -	Read in data to create a new random data file.
'''
def customFile():
	print('Please enter the following information to generate your test file...\n\n')
	fileName = input('Name of custom file:\n>>')
	nodeMin = input('Minimum Nodes:\n>>')
	nodeMax = input('Maximum Nodes:\n>>')
	connections = input('Connection Count:\n>>')
	wtMax = input('Maximum Path Weight:\n>>')
	generateFile(fileName,int(nodeMin),int(nodeMax),int(connections),int(wtMax))

	return(fileName)