import re

# \s  = [\f\n\t\v]
# \S  = [^\f\n\t\v]

if re.search("\w{2,20}\s\w{2,20}", "Sairaje Atukuri"):
    print("Full name is valid")