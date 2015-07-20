import os, re
base_url = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(base_url, topdown=False):
    for name in files:
        file_url = os.path.join(root, name)
        if re.match("(.*)html$", file_url):
            file_obj = open(file_url, "r")
            file_contents = file_obj.readlines()
            file_obj.close()
            output_contents = []
            for line in file_contents:
                matches = re.match("^include ([^\s]*)$", line)
                if matches:
                    try:
                        file_to_include = open(base_url + "\\include\\" + matches.group(1), "r")
                        file_to_include_contents = file_to_include.readlines()
                        file_to_include.close()
                        for line_to_include in file_to_include_contents:
                            output_contents.append(line_to_include)
                    except FileNotFoundError:
                        error_file = open(base_url+"\\preprocessor_erros.txt", "w+")
                        error_file.write("Error while searching " + file_url + ": could not find " + matches.group(1))
                        error_file.close()
                        exit()
                else:
                    output_contents.append(line)
            output_file_url = re.match("^(.*)\.html$", file_url).group(1)
            output_file = open(output_file_url, "w+")
            output_file.write("\n".join(output_contents))
            output_file.close()
