#!/usr/local/bin/python evn
# coding=utf-8
import os, logging.handlers


'''日志文件名'''
__LOG_FILE = './runlog.log'
__ERROR_LOG_FILE = './error_runlog.log'

def prepareLogdir():
    log_path = os.path.dirname(__LOG_FILE)
    error_log_path = os.path.dirname(__ERROR_LOG_FILE)
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    if not os.path.isdir(error_log_path):
        os.makedirs(error_log_path)

def configLog():
    prepareLogdir()
    formatter = logging.Formatter("[%(asctime)-11s]: %(module)s %(levelname)s %(message)s")
    handler = logging.handlers.TimedRotatingFileHandler(__LOG_FILE, when='D', backupCount=10)    
    error_handler = logging.handlers.TimedRotatingFileHandler(__ERROR_LOG_FILE, when='W6', backupCount=30)
    
    logging.getLogger('').setLevel(logging.DEBUG)
    
    handler.setLevel(logging.DEBUG)
    error_handler.setLevel(logging.ERROR)
    
    handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    
    logging.getLogger('').addHandler(handler)
    logging.getLogger('').addHandler(error_handler)
    