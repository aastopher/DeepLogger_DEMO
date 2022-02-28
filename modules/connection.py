from modules.EZLogger import *

# Instantiate loggers
EZ = EZLogger('connection',['decrypt','socket','connect'])
decryptLogger = EZ.getLogger('decrypt')
socketLogger = EZ.getLogger('socket')
connectLogger = EZ.getLogger('connect')

def connect():
    # PORT LOOKUP SERVICE
    # Error Classes
    class Error(Exception):
        """Base class for exceptions in this module."""
        pass

    class BrowserError(Error):
        """Problem communicating with the SQL Browser service.
        """
        def __init__(self, message):
            self.message = message

    class NoTcpError(Error):
        """Instance not configured for TCP/IP connections.
        """
        def __init__(self, message):
            self.message = message

    # Query the SQL Browser service and extract the port number
    def lookup(server, instance):
        udp_port = 1434
        try:
            socketLogger.info('establishing connection to SQL Browser Service...')
            socketLogger.info('SUCCESSFUL connection to SQL Browser Service')
            # return port
            return 0

        except KeyError as no_tcp:
            socketLogger.info(f'FAILED connection to SQL Browser Service: {NoTcpError}')
        except socket.timeout as no_response:
            socketLogger.info(f'FAILED connection to SQL Browser Service: {BrowserError}')
        except ConnectionResetError as no_connect:
            socketLogger.info(f'FAILED connection to SQL Browser Service: {BrowserError}')

    # CONNECTION PROCESS
    # input files
    try:
        decryptLogger.info('attempting to decrypt configuration files...')
        socketLogger.debug('decrypted server_name as \'server name\' and password as \'password\'')
        decryptLogger.info('SUCCESSFUL decryption')
    except Exception as e:
        decryptLogger.info(f'FAILED decryption: {e}')
        EZ.console_logger.info(f'FAILED decryption: {e}')

    # use sockets to discover IP of server
    try:
        socketLogger.info('attempting ip discovery...')
        socketLogger.debug('ip set to \'0.0.0.0\'')
        socketLogger.info('SUCCESSFUL ip discovery')
    except Exception as e:
        socketLogger.info(f'FAILED ip discovery: {e}')
        EZ.console_logger.info(f'FAILED ip discovery: {e}')
        quit()
    # establish socket connection to SQL browser service to discover tcp port of the named instance
    try:
        socketLogger.info('attempting port discovery...')
        socketLogger.debug('port set to \'1400\'')
        socketLogger.info('SUCCESSFUL port discovery')
    except Exception as e:
        port = -1
        socketLogger.info(f'FAILED port discovery: {e}')
        EZ.console_logger.info(f'FAILED port discovery: {e}')
        quit()

    # Attempt a connection to the server\instance
    try:
        connectLogger.info(f'attempting a connection to the datebase')
        connectLogger.debug(f'attempting connection to DB: \'database\' via \'server\'\\\'instance_name\' using IP: \'server_ip\' and PORT: \'port\'')
        connectLogger.info(f'SUCCESSFUL connection to Database')
        connectLogger.debug(f'SUCCESSFUL connection to DB: \'database\' via \'server\'\\\'instance_name\' using IP: \'server_ip\' and PORT: \'port\'')
    except Exception as e:
        connectLogger.info(f'FAILED connection to Database')
        connectLogger.debug(f'FAILED connection to DB: \'database\' via \'server\'\\\'instance_name\' using IP: \'server_ip\' and PORT: \'port\'')
        EZ.console_logger.info(f'FAILED connection to Database')
        quit()

connect()
