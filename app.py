from pymongo import MongoClient
from datetime import datetime
import pymongo
import logging

logging.basicConfig(filename='app.log',
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

def get_hosts():
    """
        
    """
    conn = MongoClient()
    if conn is None: 
        return logging.critical('Connection unsuccessful')
    else: 
       
        logging.info('User connected to Mongo Client Successfully')
        try:
            dbnames = conn.list_database_names()

            sourcedb=input('Enter the source database:') #Books
            if sourcedb == '' :
                return logging.error("No value entered in Source Db")
            if sourcedb in dbnames:
                logging.info('Source Database Exists')
            # if sourcedb  not in dbnames:
            else:  
                return logging.critical('Source Database does not exist')  
            
            sourcecoll=input('Enter the source collection:') #BookNames 
            x=conn[sourcedb]
            collectionames=x.list_collection_names()

            if sourcecoll == '':
                return logging.error("No value entered for source collection")
            if sourcecoll in collectionames:
                logging.info('Source Collection Exists')
            else:
                return logging.critical('Source Collection Unavailable')

            # logging.info('All user inputs done')
    
            targetdb=input('Enter the target database:')

            if targetdb == '':
                return logging.error("No value entered for Target DB")

            if targetdb  in dbnames:
                logging.info('Target Database Exists')
            else:
                logging.warning('Target Database doesnt exist, Created user entered Db')

            targetcoll=input('Enter the target collection:') 
            y=x[sourcecoll] 
            if targetcoll =='':
                return logging.error('No value entered for Target Collection')

            if  targetcoll in collectionames:
                logging.info('Target Collection exists')
            else:
                logging.warning('Target Collection doesnt exist,Created user entered Db')

            a=conn[targetdb]
            b=a[targetcoll]

            logging.info("All userinputs successfully entered")

            hosts_obj = y.find()
            logging.info("Time stamp berfore inserting")
            for x in hosts_obj:
                b.insert_many(hosts_obj)
            logging.info("Time stamp after inserting")

            # print('Out of the loop')
            logging.info('Successfully Copied')
        except:
            print("No hosts found")
        finally:
            print("============END==============")

get_hosts()
