from careers import careers

career_tuples = ()
with open('careers.txt', 'a') as file:
    for career in careers:
        career_tuples += ( (career, career), )
        file.write(f"(\"{career}\", \"{career}\"),\n")

