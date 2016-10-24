#!/usr/bin/python3

def main():
    out = open('decoded.txt', 'w')
    file1 = open('file1.txt')
    file2 = open('file2.txt')
    file3 = open('file3.txt')
    
    line1 = get_line_from_file1(file1)
    line2 = get_line_from_file2(file2)
    line3 = get_line_from_file3(file3)
    while line1 or line2 or line3:
        out.write(line1.rstrip() + '\n')
        out.write(line2.rstrip() + '\n')
        out.write(line3.rstrip() + '\n')
        line1 = get_line_from_file1(file1)
        line2 = get_line_from_file2(file2)
        line3 = get_line_from_file3(file3)
    
    out.close()
    file1.close()
    file2.close()
    file3.close()
    
    
def get_line_from_file1(file_obj):
    """Continually read lines from file_obj until a line starting 
       'ZZ' appears or the end of the file is reached."""
    line = file_obj.readline().strip()
    while line:
        if line.startswith('ZZ'):
            return line[2:]
            
        line = file_obj.readline().strip()
    return line
    
    
def get_line_from_file2(file_obj):
    """Read the next line in file_obj. If it's not empty, reverse the chars
       in each word and return the line with its changes."""
    line = file_obj.readline().strip()
    line_fixed = ''
    if line:
        words = line.split()
        for i in range(len(words)):
            line_fixed += words[i][::-1] + ' '
    return line_fixed
    
    
def get_line_from_file3(file_obj):
    """Read the next line in file_obj. If it's not empty, move the first
       character of each word to the beginning, invert its case, 
       and return the line with its changes."""
    line = file_obj.readline().strip()
    line_fixed = ''
    if line:
        words = line.split()
        for i in range(len(words)):
            last = words[i][-1]
            if last.islower():
                last = last.upper()
            else:
                last = last.lower()
            line_fixed += last + words[i][:-1] + ' '
    return line_fixed
    

main()
