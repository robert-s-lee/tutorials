import configargparse
from configargparse import ArgumentDefaultsHelpFormatter

global args
parser = configargparse.ArgParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add('--data_dir', help='MONAI data dir', default=".", env_var='MONAI_DATA_DIRECTORY')  
parser.add('--max_epochs', help='Number of epochs', type=int, default=30, env_var='MONAI_MAX_EPOCHS')  
parser.add('--val_interval', help='Eval for best metric on epoch interval', type=int, default=1)  
parser.add('--log_dir', help='Tensorboard log dir', default=None, env_var='MONAI_TB_DIR')  
args = parser.parse_args()      
if args.max_epochs < args.val_interval: args.val_interval = args.max_epochs