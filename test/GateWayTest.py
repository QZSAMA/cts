import sys
sys.path.insert(0, '../src')

from GateWay import *
from testAndPrint import *

def main():

	Manager = GateWay()

	testAndPrint(Manager.vaild_user('if'), False)

	testAndPrint(Manager.vaild_user('testuser2'), True)

main()