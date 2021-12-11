import time
import subprocess
import sys

try:

	mat_size=sys.argv[1]
	num_process=sys.argv[2]
	iterations=int(sys.argv[3])
	
	#1. Matrix multiplication sequential version
	# Compile the matrix multiplication program
	subprocess.call(["gcc","mat_seq.c","-o","x"])
	start=time.time() # Starting timestamp

	# Iterate the compiled code
	for i in range(iterations):
		subprocess.call(["./x",mat_size])

	end=time.time() # Ending timestamp
	total_time=end-start

	# Print total time taken and average time over all iterations
	print( "Sequential Implementaion")
	print("-------------------------")
	print( "Total time taken (in seconds): "+str(total_time) )
	print( "Average time (in seconds): "+str(total_time/iterations) )
	
	#2. Matrix multiplication openMP version
	subprocess.call(["gcc","-fopenmp","mat_openmp.c","-o","x"])
	start=time.time() # Starting timestamp

	# Iterate the compiled code
	for i in range(iterations):
        	subprocess.call(["./x",mat_size])

	end=time.time() # Ending timestamp
	total_time=end-start

	# Print total time taken and average time over all iterations
	print( "\nOpenMP implementation")
	print( "----------------------" )
	print( "Total time taken (in seconds): "+str(total_time) )

	print("Average time (in seconds): "+str(total_time/iterations) )

	#3. Matrix multiplication MPI version
	subprocess.call(["mpicc","mat_mpi.c","-o","x"])
	start=time.time() # Starting timestamp

        # Iterate the compiled code
	for i in range(iterations):
		subprocess.call(["mpirun","-np",num_process,"./x",mat_size])

	end=time.time() # Ending timestamp
	total_time=end-start

        # Print total time taken and average time over all iterations
	print( "\nMPI implementation")
	print( "----------------------")
	print( "Total time taken (in seconds): "+str(total_time) )

	print( "Average time (in seconds): "+str(total_time/iterations) )


except ValueError:
	print ("Invalid matrix size")
