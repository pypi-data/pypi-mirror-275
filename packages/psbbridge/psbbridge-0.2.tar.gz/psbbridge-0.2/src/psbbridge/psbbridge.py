import pacspeddbase as psb

"""PacSpedd Base Bridge is a in Python written Bridge Modul for the in Rust written PacSpedd Base Modul.
He Called only the PacSpedd Base Functions, but included Doc Strings and IDE Extensions"""

def print(text):
    """Print a Message to The Device, but with the Rust Print Line Macro
    
    Args:
        text (str):
            The Message to Print
    """
    psb.print(text)

def cprint(text, color=None):
    """Print a Colored Message to The Device
    
    Args:
        text (str):
            The Message to Print
        color (str):
            The Color 'green', 'blue' or 'red'"""
    psb.cprint(text, color)

def get_env(env):
    """Grep a Environment Variable"""
    psb.get_env(env)

class System:
    """Class to Interaction with the System"""
    def __init__(self):
        """Init The System Class without Argument"""
        self.system = psb.System()

    def cmd(self, command):
        """Call the Command to the System and execute him, but safer the the OS or SUBPROCESS implementation, like Rust

        Args:
            command (str):
                The Command to Execute

        """
        self.system.cmd(command)

    def mkdir(self, path):
        """Create a Single Directory
        
        Args:
            path (str):
                The Path to The Directory to Create"""
        self.system.mkdir(path)

    def cd(self, path):
        """Change the Current Workdir
        
        Args:
            path (str):
                The New WorkDir"""
        self.system.cd(path)
        
    def list_files(self, path):
        """List Files and Return a String

        Args:
            path (str):
                The Path to List Dir"""
        self.system.list_files(path)

    def clear(self):
        """Clear The Terminal"""
        self.system.clear()

    def wget(self, url):
        """Download a File from Url like wget Interaction

        Args:
            url (str):
                The Url to Download"""
        self.system.wget(url)

    def makedirs(self, path):
        """Make a Directory with all Sub or Header Directorys
        
        Args:
            path (str):
                The Full Path to Create"""
        self.system.makedirs(path)

    def copy(self, srcpath, despath):
        """Copy Files and/or Folder from a to b
        
        Args:
            srcpath (str):
                The Source Path
            despath (str):
                The Target path"""
        self.system.copy(srcpath, despath)

    def listdir(self, path):
        """List all Dire Files, Warning, this is not a String"""
        self.system.listdir(path)

    def source(self, path):
        """Source A File or Call him"""
        self.system.source(path)

class Args:
    """Class to Work with System Arguments"""
    def __init__(self):
        self.args = psb.Args()
    def get(self, position):
        """Get the Argument from the Given Position"""
        self.args.get(position)
    def get_from(self, position):
        """Get all Arguments, Starting from the Given Position"""
        self.args.get_from(position)

def argv(position):
    """Get the Argument From the Given Position"""
    psb.argv(position)