global GLOB
GLOB = 4

def foo():
	print(GLOB)

def main():
	global GLOB
	GLOB = 10
	foo()

if __name__ == '__main__':
	main()