from re import search

input_file = open("temp_btn_names", 'r')
names = []
counter=0

for line in input_file:
    name = search(r'pushButton_\d+|p\d+_?\d*', line)
    if name != None:
        counter+=1
        print("self.ui." + str(name.group(0)) + ".clicked.connect(self.platform_clicked)")
        print("self.ui." + str(name.group(0)) + ".setStyleSheet(\"color: #e1e1e1;\")")