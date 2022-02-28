from modules.DeepLogger import *

# Instantiate loggers
DL = DeepLogger('process',['query','logic','clean','export'])
queryLogger = DL.getLogger('query')
logicLogger = DL.getLogger('logic')
cleanLogger = DL.getLogger('clean')
exportLogger = DL.getLogger('export')

#Initialize date and version variables
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d_%H-%M-%S")
query_version = '3.1'

def process():
    try:
        queryLogger.info('initializing local variables for query')
        queryLogger.debug(f'local var now as {now} and query_version as v{query_version}')
        queryLogger.info('SUCCESSFUL initializing variables')
    except Exception as e:
    	queryLogger.info(f'FAILED initializing local variables: {e}')
    	quit()

    #PROCESS QUERY
    try:
        queryLogger.info('attempting to run query...')
        queryLogger.debug('query running on DB: \'database\' via \'server\'\\\'instance_name\' using IP: \'server_ip\' and PORT: \'port\'')
        queryLogger.info('SUCCESSFUL query fetch')
    except Exception as e:
        queryLogger.info(f'FAILED query fetch: {e}')
        DL.console_logger.info(f'FAILED query fetch: {e}')
        quit()

    # PROCESS LOGIC
    try:
        logicLogger.info('SUCCESSFUL process logic')
        logicLogger.debug('logic step 1')
        logicLogger.debug('logic step 2')
        logicLogger.debug('logic step 3')
        logicLogger.debug('logic step 4')
    except Exception as e:
    	logicLogger.info(f'FAILED process logic: {e}')
    	DL.console_logger.info(f'FAILED process logic: {e}')
    	quit()

    # CLEAN UP
    try:
        cleanLogger.info('attempting clean up...')
        cleanLogger.debug('clean-up step 1')
        cleanLogger.debug('clean-up step 2')
        cleanLogger.debug('clean-up step 3')
        cleanLogger.info('SUCCESSFUL clean up')
    except Exception as e:
    	cleanLogger.info(f'FAILED clean up: {e}')
    	DL.console_logger.info(f'FAILED clean up: {e}')
    	quit()

    # SET DIRECTORIES & EXPORT
    try:
        exportLogger.info('attempting to mount network drive...')
        exportLogger.debug('export step 1')
        exportLogger.debug('export step 2')
        exportLogger.info('SUCCESSFUL network drive mount')
    except Exception as e:
    	exportLogger.info(f'FAILED network drive mount: {e}')
    	DL.console_logger.info(f'FAILED network drive mount: {e}')
    	quit()
    try:
        exportLogger.info('attempting to write file...')
        exportLogger.debug('writing file to destination /usr/bin/etc...')
        exportLogger.info('SUCCESSFUL file write')
    except Exception as e:
    	exportLogger.info(f'FAILED file write: {e}')
    	DL.console_logger.info(f'FAILED file write: {e}')
    	quit()

try:
    exportLogger.info('attempting process...')
    process()
    exportLogger.info('SUCCESSFUL process!')
    DL.console_logger.info(f'script ran SUCCESSFULLY! - {now}')
except Exception as e:
	exportLogger.info(f'FAILED process: {e}')
	DL.console_logger.info(f'script FAILED to run, please check logs - {now}')
