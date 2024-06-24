def main():
    name = input('Enter your name: ')
    description = input('Describe yourself: ')
    outfile = open('mypage.html', 'w')

    outfile.write('<html>')
    outfile.write('<body>')

    outfile.write('<h1>')
    outfile.write(name)
    outfile.write('</h1>')

    outfile.write('<hr />')
    outfile.write(description)
    outfile.write('<hr />')

    outfile.write('</body>')
    outfile.write('</html>')

    outfile.close()

main()
