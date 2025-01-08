.data 
    array: .space 400 # Array of size 100
    p1: .asciiz "Enter the size of the array "
    p2: .asciiz "Enter the elements of the array(Each element in a new line)\n"
    p3: .asciiz "Enter the value of sum "
    space: .asciiz " "
    nf: .asciiz "Not found\n"
.text
    # Asking for the size
    #li $v0,4
    #la $a0,p1
    #syscall
    # Storing that size
    li $v0,5
    syscall
    move $t0,$v0 # t0 = v0(size)
    # Asking for the elements
    #li $v0,4
    #la $a0,p2
    #syscall
    # The elements are taken in new line
    
    
    addi $t1,$zero,0 # t1 = 0 (iterator)
    
while:
    beq $t1,$t0,suminput # Exit if iterator = size and start finding the array 
    li $v0,5		 #elements that satisfy a[i]+a[j]=x
    syscall
    mul $s0,$t1,4
    sw $v0,array($s0)
    addi $t1,$t1,1 # Increment iterator
    j while
    
suminput:    
    #Asking for the value of sum(x)
    #li $v0,4
    #la $a0,p3
    #syscall
    
    #Taking input of sum
    li $v0,5
    syscall
    move $s7,$v0 #s7=sum
    j findsum
    
    #Finding the matching pair of elements satisfying a[i]+a[j]=sum
findsum:
	#s5=i,s6=j
	move $s5,$zero #s5,i=0
	addi $t0,$t0,-1 #size=size-1
	move $s6,$t0 #j=size-1
	move $s3,$zero #flag=0 , s3=flag
	whiles:
		bge $s5,$s6,flag #if i>=j check flag
		mul $t3,$s5,4 	 #t3=s5*4 (i*4)
		mul $t4,$s6,4 	 #t4=s4*4 (j*4)
		lw $t5,array($t3)#t5=array[i]
		lw $t6,array($t4)#t6=array[j]
		add $t7,$t5,$t6  #t7=array[i]+array[j]
		beq $t5,$s7,equal#array[i]+array[j]=sum
		blt $t7,$s7,less #array[i]+array[j]<sum
		bgt $t7,$s7,more #array[i]+array[j]>sum
	equal:
		li $v0,1
		move $a0,$t5
		syscall  #Printing array[i]
		#printing the space
		li $v0,4
		la $a0,space
		syscall
		#printing array[j]
		li $v0,1
		move $a0,$t6
		syscall
		#Setting flag=1	
		addi $s3,$s3,1
		j flag
		
	less:
		addi $s5,$s5,1 #i+=1
		j whiles
	more:
		addi $s6,$s6,-1 #j+=-1
		j whiles
			
	flag:
		beq $s3,$zero,printnf #if flag=0,print not found
		j exit
		
	printnf:
		move $t7,$zero
		addi $t7,$t7,-1
		li $v0,1
		move $a0,$t7
		syscall
		j exit
				
exit:
    li $v0,10
    syscall
