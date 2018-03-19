import os;
import sys;

message = str(sys.argv[0]);
subject = str(sys.argv[1]);

os.system('echo '+ subject +' | mail -s ' + message + ' hugo.pierre@devinci.fr');
