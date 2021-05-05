import animation
import time

elipses = (
    '.......              ', '...........              ', '...........          ',
    '...........          ', '..............           ', '...............      ',
    '................     ', '...................      ', '..................   ',
    '...................  ', '........................ ', '.....................'
)


@animation.wait(elipses, color='red')
def long_running_function():
    time.sleep(5)
    return
long_running_function()
