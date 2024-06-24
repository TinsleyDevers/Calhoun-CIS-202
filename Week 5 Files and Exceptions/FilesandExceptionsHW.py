name = input(f'Please enter your name: ')
info = input(f'Describe yourself: ')
html = f'''
<html>
<body>
<h1>{name}</h1>
<hr />
{info}
<hr />
</body>
</html>
'''

websitefile = 'website.html'
with open(websitefile, 'w') as file:
    file.write(html)

print('HTML file created! Check website.html')
