import os, subprocess, time

def main():
	# time.sleep(4500)
	time.sleep(3600)
	p = subprocess.Popen([r"C:\Users\Chris\Desktop\sleep.cmd"])
	p.communicate()

if __name__ == '__main__':
	main()
	