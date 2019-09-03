import logging

log = logging.getLogger('main')
log.setLevel(logging.DEBUG)

handler = logging.FileHandler('my.log')

format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
handler.setFormatter(format)
log.addHandler(handler)
log = logging.getLogger('main')
log.setLevel(logging.DEBUG)