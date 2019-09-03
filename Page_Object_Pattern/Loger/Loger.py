import logging
import sys

main = logging.getLogger('main')
main.setLevel(logging.DEBUG)

handler = logging.FileHandler('my.log')

format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
handler.setFormatter(format)
main.addHandler(handler)
main = logging.getLogger('main')
main.setLevel(logging.DEBUG)