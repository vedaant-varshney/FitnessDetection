import sys

sys.stderr.write('this is stderr text \n')
sys.stderr.flush()

sys.stdout.write("This is stdout text \n")

# print(sys.argv)

# python understanding_sys.py 12 to add to arguments printed in sys.argv

if len(sys.argv) > 1:
    # adds 10 to the argument given 
    print(int(sys.argv[1]) + 10)

def(arg):
    print(arg)

main(sys.argv[1])