import maya.cmds as cmds
import time
cmds.file(new=True, force=True)

#need to find 'b's, for all 'a's --> formula derived from (a+b)/a == a/b == 1.61803398875 ---> b = a*1.61803398875-a 
print 1.236/2

def formulaToCalulateBsUponAs(a):
	b=a*1.61803398875-a
	return b


for a in range(1,5):
	b=formulaToCalulateBsUponAs(a);
	print a,b
	
	cmds.polyCube()
	cmds.scale(a,0.1,b)
	cmds.refresh()
	time.sleep(0.5)
	
	#offset the new rectangle by a/2 in x axis
	cmds.move(a/2,0,0,  relative=True)
	cmds.refresh()
	time.sleep(0.2)
	#offset the new rectangle by b/2 in z axis
	cmds.move(0,0,b/2,relative=True)
	cmds.refresh()
	time.sleep(0.2)
	#cmds.rotate(0,90,0)
	
