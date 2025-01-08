.data 
	array: .space 400 #Array capable of holding upto 100 integers
	#p1: .asciiz "Enter the size of the array "
	#p2: .asciiz "Enter the elements of the array\n"
	#p3: .asciiz "The sorted array is\n"
	p4: .asciiz " "
.text
	#Asking the user for the size of the array
	#li $v0,4
	#la $a0,p1
	#syscall
	#s0=n(size of the array)
	li $v0,5
	syscall
	move $s0,$v0
	
	#Asking the user to input the array
	#li $v0,4
	#la $a0,p2
	#syscall
	
	addi $t1,$zero,0 # t1 = 0 (iterator)
	#Taking the array input
	while:
    		beq $t1,$s0,ans 
    		li $v0,5		 
    		syscall
    		mul $t0,$t1,4
    		sw $v0,array($t0)
    		addi $t1,$t1,1 # Increment iterator
    		j while
	
	
	
	ans:
		#k=1
		move $s1,$zero
		addi $s1,$s1,1
		#li $v0,4
		#la $a0,p3
		#syscall
		#s1=k
		j start
	
	start:
		move $t1,$zero #t1=0=i
		lw $s2,array($t1) #s2=low
		lw $s3,array($t1) #s3=high
		j maxmin
	
	bsearch:
		for1: #while(low<high)
			bge $s2,$s3,printans #return low
			add $s4,$s2,$s3 #mid=(low+high) s4=mid
			sra $s4,$s4,1 #mid=mid/2
			j lsearch
	
	check:
		blt $t7,$s1,lowres
		j highres
		
	lowres:
		addi $s2,$s4,1 #low=mid+1
		j bsearch
		
	highres:
		move $s3,$s4 #high=mid
		j bsearch	
			
	maxmin:
		for:
    			beq $t1,$s0,bsearch
    			mul $t0,$t1,4
    			lw  $t2,array($t0) #t2=array[i]
    			blt $t2,$s2,lowset #array[i]<low
    			bgt  $t2,$s3,highset #array[i]>high
    			addi $t1,$t1,1 # Increment iterator
    			j for
    	lowset:
    		move $s2,$t2 	#low=array[i]
    		addi $t1,$t1,1 # Increment iterator
    		j maxmin
    	highset:
    		move $s3,$t2   #high=array[i]
    		addi $t1,$t1,1 # Increment iterator
    		j maxmin
    	
    	lsearch:
    		move $t7,$zero #t7=count=0
    		move $t3,$zero #t3=0(iterator)
    		for2:
    			bge  $t3,$s0,check
    			mul $t6,$t3,4 #t6=t3*4
    			lw $t5,array($t6) #t5=array[i]
    			ble $t5,$s4,count_inc
    			addi $t3,$t3,1
    			j for2
    	
    	count_inc:
    		addi $t7,$t7,1
    		addi $t3,$t3,1
    		j for2
    					
	printans: #Print the answer and exit
		#Printing the answer
		li $v0,1
		move $a0,$s2 
		syscall
		#The space
		li $v0,4
		la $a0,p4
		syscall
		#if(k==n) exit
		beq $s1,$s0,exit
		addi $s1,$s1,1 #k+=1
		j start
	
	exit:	
		#Terminating the program
		li $v0,10
		syscall
