# Lab 01 Enhanced Commands

# Additional commands to demonstrate in lab01/practice directory

# Test absolute vs relative paths
echo "Understanding paths:"
echo "Current absolute path: $(pwd)"
echo "Going up one level with relative path:"
cd ..
echo "Now at: $(pwd)"
cd lab01  # relative path back

# Command history examples
echo "Command history examples:"
history | tail -5

# More file operations
echo "Advanced file operations:"
find . -name "*.txt"  # find all txt files
wc -l *.txt          # word count for text files

# Create a simple backup scenario
mkdir backup
cp *.txt backup/ 2>/dev/null || echo "No txt files to backup"
ls -la backup/