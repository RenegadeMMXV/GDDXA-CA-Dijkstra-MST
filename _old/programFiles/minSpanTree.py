'''	@author			Ciaran Bent [K00221230]
	@creationDate	18/09/2018
	@description	'Statistics, Algorithms, and AI' Python implementation of 
					'Dijkstra's Minimum Spanning Tree' algorithm
	@version		1.3.4
	@deadline		14/10/2018
'''

import GraphTools

def main():
	graph = []
	root = -GraphTools.math.inf

	print('**********************************************************')
	print('Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm.')
	print('**********************************************************\n\n')
	
	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')
	
	if usrInp == 'y' or usrInp == 'Y':
		print('You have created a file called \'%s.csv\' in the \'testFiles\' directory.\n\n' % GraphTools.customFile())
		main()

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		graph = GraphTools.compileGraph('testFiles\\%s' % fileName)
		
		invalid = 1
		while (invalid == 1) or ((root < 1) or (root > graph.getNodes())):
		 	try:
		 		root = int(input('Please enter a number between 1 - %r to be the Starting Node:\n>>' % graph.getNodes()))
		 		invalid = 0
		 	except:
		 		print('\n\nERROR: Invalid input.\n')
		 		invalid = 1

		GraphTools.dijkstra(graph,root)
		graph.shortPathTree.listTree(root)

		print('\n--------\nFINISHED\n--------\n')
		
main()
