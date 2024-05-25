import subprocess, re, collections, codecs
import asyncio
import pfmisc
import pudb
from pfmisc._colors import Colors


# Credit to Anatoly Techtonik
# https://stackoverflow.com/questions/606191/convert-bytes-to-a-string/27527728#27527728
def slashescape(err):
    """codecs error handler. err is UnicodeDecode instance. return
    a tuple with a replacement for the unencodable part of the input
    and a position where encoding should continue"""
    # print err, dir(err), err.start, err.end, err.object[:err.start]
    thebyte = err.object[err.start : err.end]
    repl = "\\x" + hex(ord(thebyte))[2:]
    return (repl, err.end)


codecs.register_error("slashescape", slashescape)


class Base:
    """
    A Base class for pypx.

    This class is somewhat abstract/virtual in as much as it
    provides a substrate for derived classes and in and of
    itself does very little.

    """

    def defaults_init(self, d_arg):
        """
        Somewhat convoluted initialization that mirrors/duplicates
        the default initialization when called from CLI
        """

        for k, v in d_arg.items():
            if k in self.arg:
                setattr(self, k, self.arg[k])
            else:
                setattr(self, k, v)

    def __init__(self, arg):
        """
        Initialize some core self variables common to all derived classes.
        """

        self.arg = arg

        # For lint sanity, the following are explicitly set
        # (note that they are implicitly created in the call
        # to defaults_init):
        self.verbosity = 1
        self.aec = ""
        self.aet = ""
        self.serverIP = ""
        self.serverPort = ""

        self.defaults_init(
            {
                "aet": "CHRIS-AET",
                "aec": "CHRIS-AEC",
                "serverIP": "127.0.0.1",
                "serverPort": "4242",
                "findscu": "/usr/bin/findscu",
                "movescu": "/usr/bin/movescu",
                "storescp": "/usr/bin/storescp",
                "echoscu": "/usr/bin/echoscu",
                "colorize": "",
                "printReport": "",
                "verbosity": 1,
                "retrieve": False,
                "move": False,
            }
        )

        self.response = {"status": "error", "data": {}}

        self.dp = pfmisc.debug(verbosity=self.verbosity, within="Base", syslog=False)

    def systemlevel_run(self, opt, d_params):
        """
        Run the system command, based on the passed parameter dictionary
        """
        b_commandGen = False
        str_cmd = ""
        d_ret = {}

        # A function to execute to generate commands
        f_commandGen = None
        for k, v in d_params.items():
            if k == "f_commandGen":
                f_commandGen = v
                b_commandGen = True
            else:
                opt[k] = v

        if b_commandGen:
            str_cmd = f_commandGen(opt)
            self.dp.qprint("\n%s" % str_cmd, level=5, type="status")
            raw_response = subprocess.run(
                str_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
            )
            d_ret = self.formatResponse(raw_response)

        return d_ret

    async def systemlevel_runasync(self, opt, d_params):
        """
        Run the system command asynchronously, based on the passed parameter
        dictionary. Avoid using if large amounts of stdout data is generated!
        Output is assumed to be UTF-8 text.
        """
        b_commandGen = False
        str_cmd = ""
        d_ret = {}

        # A function to execute to generate commands
        f_commandGen = None
        for k, v in d_params.items():
            if k == "f_commandGen":
                f_commandGen = v
                b_commandGen = True
            else:
                opt[k] = v

        if b_commandGen:
            str_cmd = f_commandGen(opt) + " | strings "
            self.dp.qprint("\n%s" % str_cmd, level=5, type="status")
            raw_response = await asyncio.create_subprocess_shell(
                str_cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await raw_response.communicate()

            # if only stderr and not stdout, then equate the two...
            if not stdout and stderr:
                stdout = stderr

            d_ret = self.__formatResponseHelper(
                stdout, str_cmd, raw_response.returncode
            )

        return d_ret

    def commandSuffix(self):
        # required parameters
        command_suffix = " -aec " + self.aec
        command_suffix += " -aet " + self.aet
        command_suffix += " " + self.serverIP
        command_suffix += " " + self.serverPort

        return command_suffix

    def handle(self, raw_response):
        std = raw_response.stdout.decode("ascii")
        response = {"status": "success", "data": "", "command": raw_response.args}
        if std != "":
            response["status"] = "error"
            response["data"] = std

        return response

    def checkResponse(self, response):
        std_split = response.split("\n")
        info_count = 0
        error_count = 0
        for line in std_split:
            if line.startswith("I: "):
                info_count += 1
            elif line.startswith("E: ") or "error" in line.lower():
                error_count += 1

        status = "error"
        if error_count == 0:
            status = "success"

        return status

    def parseResponse(self, response):
        data = []

        uid = 0
        std_split = response.split("\n")

        for line in std_split:
            if line.startswith("I: ---------------------------"):
                data.append({})
                data[-1]["uid"] = {}
                data[-1]["uid"]["tag"] = 0
                data[-1]["uid"]["value"] = uid
                data[-1]["uid"]["label"] = "uid"
                uid += 1

            elif line.startswith("I: "):
                lineSplit = line.split()
                if len(lineSplit) >= 8 and re.search("\((.*?)\)", lineSplit[1]) != None:
                    # extract DICOM tag
                    tag = (
                        re.search("\((.*?)\)", lineSplit[1])
                        .group(0)[1:-1]
                        .strip()
                        .replace("\x00", "")
                    )

                    # extract value
                    value = re.search("\[(.*?)\]", line)
                    if value != None:
                        value = value.group(0)[1:-1].strip().replace("\x00", "")
                    else:
                        value = "no value provided for %s" % tag

                    # extract label
                    label = lineSplit[-1].strip()

                    data[-1][label] = {}
                    data[-1][label]["tag"] = tag
                    data[-1][label]["value"] = value
                    data[-1][label]["label"] = label
                else:
                    # Only append the line output for the echo command
                    if type(self).__name__ == "Echo":
                        data.append(line)

        return data

    def formatResponse(self, raw_response):
        return self.__formatResponseHelper(
            raw_response.stdout, raw_response.args, raw_response.returncode
        )

    def __formatResponseHelper(self, stdout, args, returncode):
        std = stdout.decode("utf-8", "slashescape")
        response = {
            "status": "success",
            "data": "",
            "command": args,
            "returncode": returncode,
        }

        status = self.checkResponse(std)

        if status == "error":
            response["status"] = "error"
            response["data"] = std
        else:
            response["status"] = "success"
            response["data"] = self.parseResponse(std)

        return response
