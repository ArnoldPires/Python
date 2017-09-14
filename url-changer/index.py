import sys
def update_url(input_url):
    output_url = input_url[:15]
    return output_url
url_from_command_line = sys.argv[1]
updated_url_from_command_line = update_url(url_from_command_line)
print("The input URL was:  " + url_from_command_line)
print("The updated URL is: " + updated_url_from_command_line)
