import configargparse
from configargparse import ArgumentDefaultsHelpFormatter

parser = configargparse.ArgParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add('-d', '--dbsnp', help='known variants .vcf', default="me", env_var='DBSNP_PATH')  # this option can be set in a config file because it starts with '--'

args = parser.parse_args()

print(args)
print("----------")
print(parser.format_help())
print("----------")
print(parser.format_values())    # useful for logging where different settings came from