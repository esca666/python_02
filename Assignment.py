#how would you modify a python script to append a new line of text
# "New data Entry", to an existing file named log.txt without erasing its current contents?

# with open ('log.txt', 'a') as file:
#     file.write('New data entry\n')

# ASSIGNMENT NO 2 


#Defining the chunk file 
chunk_size = 1024


with open ('large_file.txt', 'a') as file:
    file.write('New data entry\n')

#open the large file for reading in binary mode
with open('large_file.txt','r') as infile:

#open the large file for writing in binary mode

    with open('large_file.txt', 'wb') as outfile:
        while True:
            #read a chunk of data 
            chunk = infile.read(chunk_size)
            print(chunk)
            if not chunk:
                break #Exit the loop if end of file is reached 
                    #process the chunk (e.g:- convert to upercase)
            processed_chunk = chunk.upper()
            #write the processed chunk to the output file
            outfile.write(processed_chunk)

        