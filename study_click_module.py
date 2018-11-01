import click

@click.command()
@click.option('--count', default = 1, help = 'Numbor of gretting')
@click.option('--name', nargs=2, prompt = 'your name', help = 'the person to greet.', default = '')

# @click.option('-m','--mail_to',default = '',help = 'mail to person email')
# parameters introdutions
# Click supports two types of parameters for scripts: options and arguments.
# parameter type
# If no type is provided, the type of the default value is used.
# Multi Value Options

#It automatically generates nicely formatted help pages:
# prompt varible can advocate youself you name
# default varible set per default value
# help varible can print its help document
# --name nargs=2 means name attribute have two varible
def hello(count,name):
    '''simple program that greets name for a total of count times'''
    for i in range(int(count)):
        click.echo('name1  is %s,name2 is %s' %  name)

if __name__ == '__main__':
    hello()

# we havo to run in the command line,for example:
# python env_click.py --help
# python env_click.py --count=3 --name='houkai'
# python env_click.py --count=3  after anter input you name via clue


