import sys

if __name__ == "__main__":

	student_file = open("input.csv", 'r')
	template_file = open("template.txt", 'r')
	output_file = open("output.txt", 'w')

	template = template_file.read()

	for line in student_file:
		msg = template + "\n\n\n"

		items = line.split(',')
		
		msg = msg.replace("NAME", items[0])
		msg = msg.replace("TIME", items[1])
		msg = msg.replace("TEACHER", items[2])
		
		output_file.write(msg)

	print("Finished!")
