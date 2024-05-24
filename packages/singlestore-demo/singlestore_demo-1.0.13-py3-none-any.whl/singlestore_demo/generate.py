# pip install singlestoredb
# pip install numpy
# pip install mimesis
import random
import os
from os.path import exists
import sys
from sys import exit
import argparse
import threading
import numpy as np

from mimesis import Person
from mimesis import Text
from mimesis import Numeric
from mimesis import Datetime
from mimesis import Address
from mimesis import Finance
from mimesis.random import Random
from mimesis.locales import Locale

import singlestoredb as s2

mimefinance = Finance(Locale.EN)
mimeperson = Person(Locale.EN)
mimetext = Text(Locale.EN)
mimerandom = Random()
mimeaddress = Address()
mimenumeric = Numeric()
mimedate = Datetime()

parser = argparse.ArgumentParser()

parser.add_argument("--host", default="localhost", help="The hostname of the SingleStoreDB node to connect to")
parser.add_argument("--port", default=3306, type=int, help="The port of the SingleStoreDB node to connect to")
parser.add_argument("--username", default="root", help="The username of the SingleStoreDB user with permissions to create a database.")
parser.add_argument("--password", default="", help="The password of the SingleStoreDB user specified.")

parser.add_argument("--rows-per-insert", default=10000, help="The number of rows to send to SingleStore at once")

parser.add_argument("--total-orders", default=10, type=int, help="The total number of orders * rows per insert")
parser.add_argument("--total-suppliers", default=1, type=int, help="The total number of suppliers * rows per insert")
parser.add_argument("--total-parts", default=20, type=int, help="The total number of parts * rows per insert")
parser.add_argument("--total-parts-suppliers", default=80, type=int, help="The total number of parts on suppliers * rows per insert")
parser.add_argument("--total-customers", default=15, type=int, help="The total number of customers * rows per insert")
parser.add_argument("--lineitem-max", default=10, type=int, help="The Maximum number of line items per order")
parser.add_argument("--lineitem-min", default=4, type=int, help="The Minimum number of line items per order")
parser.add_argument("--only-orders", action='store_true', help="Only adds a new orders to the database. Doesn't drop the database")

parser.add_argument("--schema", default=None, help="The database schema file.")

options = parser.parse_args()

HOST = options.host
PORT = options.port
USERNAME = options.username
PASSWORD = options.password
DATABASE = "memsql_demo"
SCHEMA = os.path.join(os.path.dirname(__file__), "schema.sql")
if options.schema != None :
  SCHEMA = options.schema

ROWSPERINSERT = options.rows_per_insert

TOTALORDERS = options.total_orders * ROWSPERINSERT
TOTALSUPPLIERS = options.total_suppliers * ROWSPERINSERT
TOTALPARTS = options.total_parts * ROWSPERINSERT
TOTALPARTSSUPPLIERS = options.total_parts_suppliers * ROWSPERINSERT
TOTALCUSTOMERS = options.total_customers * ROWSPERINSERT
LINEITEMMAX = options.lineitem_max
LINEITEMMIN = options.lineitem_min

ONLYORDERS = options.only_orders

PARTTYPES = ["PROMO BURNISHED COPPER", "STANDARD POLISHED BRASS", "PROMO PLATED STEEL", "SMALL BURNISHED STEEL", "STANDARD BURNISHED NICKEL", "PROMO PLATED TIN", "SMALL BURNISHED STEEL", "SMALL ANODIZED NICKEL", "PROMO POLISHED BRASS", "SMALL BRUSHED STEEL"]
CONTAINERTYPES = ["SMALL CASE", "MED CASE", "LARGE CASE", "JUMBO CASE", "SMALL PACK", "MED PACK", "LARGE PACK", "JUMBO PACK", "SMALL BOX", "MED BOX", "LARGE BOX", "JUMBO BOX", "SMALL DRUM", "MED DRUM", "LARGE DRUM", "JUMBO DRUM"]
MKTSEGMENT = ["HOUSEHOLD", "AUTOMOBILE", "FURNITURE", "MACHINERY", "BUILDING"]

SUPPLIERS = None
PARTS = None
CUSTOMERS = None
NATIONS = None

def get_connection(db = ""):
    out = s2.connect(
        host=HOST,
        port=PORT,
        user=USERNAME,
        password=PASSWORD,
        database=db)
    return out

def test_connection():
    try:
        with get_connection(db="information_schema") as conn:
            conn.is_connected()
    except s2.Error:
        print("Unable to connect to SingleStoreDB Cloud with provided connection details.")
        print("Please verify that SingleStoreDB Cloud is running @ %s:%s" % (HOST, PORT))
        sys.exit(1)

class InsertWorker(threading.Thread):
    """ A simple thread which inserts empty rows in a loop. """

    def __init__(self, query):
        super(InsertWorker, self).__init__()
        self.query = query
        self.daemon = True
        self.exception = None

    def run(self):
      with get_connection(DATABASE) as conn:
        with conn.cursor() as cur:
          cur.execute(self.query)
          conn.commit()
          print("Insert completed...")

class InsertCustomer(threading.Thread):
  def __init__(self, count):
    super(InsertCustomer, self).__init__()
    self.count = count
    self.daemon = True
    self.exception = None
  def run(self):
    print("Generating data for customers...")
    rows = [[
      mimerandom.generate_string_by_mask(mask="Customer#####", digit='#'),
      mimeaddress.address()[:40],
      random.choice(NATIONS),
      mimeperson.telephone()[:15],
      round(mimenumeric.decimal_number(start=0.00,end=999.00),2),
      random.choice(MKTSEGMENT),
      mimetext.sentence()[:50]
      ] for x in np.arange(ROWSPERINSERT)]
    
    insertRows = (",".join('("{}", "{}", {}, "{}", {}, "{}", "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows))
    print("Inserting records {}/{}".format((self.count + 1) * ROWSPERINSERT, TOTALCUSTOMERS))
    query = ' \
      INSERT INTO `customer` (name, address, nationkey, phone, acctbal, MKTSEGMENT, comment) \
      VALUES {}'.format(insertRows)
    th = InsertWorker(query)
    th.start()
    th.join()

class InsertOrder(threading.Thread):
  def __init__(self, count):
    super(InsertOrder, self).__init__()
    self.count = count
    self.daemon = True
    self.exception = None
  def run(self):
    print("Generating data for orders...")
    rows = [[
      random.choice(CUSTOMERS),
      mimerandom.generate_string_by_mask(mask="@"),
      round(mimenumeric.decimal_number(start=0.00,end=999.00),2),
      mimedate.date(start=2010,end=2023),
      mimetext.level(),
      mimeperson.first_name(),
      mimenumeric.integer_number(start=1, end=99),
      mimetext.sentence()[:79]
      ] for x in np.arange(ROWSPERINSERT)]
    print("Inserting records {}/{}".format((self.count + 1) * ROWSPERINSERT, TOTALORDERS))
    insertRows = (",".join('({}, "{}", {}, "{}", "{}", "{}", {}, "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows))
    query = ' \
      INSERT INTO `orders` (custkey, orderstatus, totalprice, orderdate, orderpriority, clerk, shippriority, comment) \
      VALUES {}'.format(insertRows)
    th = InsertWorker(query)
    th.start()
    th.join()

def create_database():
  print("Creating demo database from ", SCHEMA)
  if not exists(SCHEMA):
    exit("File %s is not found. Aborting demo creationg." % SCHEMA)
  with get_connection() as conn:
    with conn.cursor() as cur:
      with open(SCHEMA, 'r') as dbschema:
        sql = dbschema.read()
        sqlcommands = sql.split(';')
        for sqlcommand in sqlcommands:
          if sqlcommand.strip():
            print("` %s `" % sqlcommand)
            cur.execute(sqlcommand)

def create_suppliers():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generating and Inserting `supplier` data")
      for supplier in np.arange(int(TOTALSUPPLIERS/ROWSPERINSERT)):
        rows = [[
          mimefinance.company()[:25],
          mimeaddress.address()[:40],
          17,
          mimeperson.telephone()[:15],
          round(mimenumeric.decimal_number(start=0.00,end=9999999.00),2),
          mimetext.sentence()[:50]
         ] for x in np.arange(ROWSPERINSERT)]

        insertRows = (','.join('("{}", "{}", {}, "{}", {}, "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows))

        print("Inserting records {}/{}".format((supplier + 1) * ROWSPERINSERT, TOTALSUPPLIERS));
        query = ' \
                INSERT INTO `supplier` (name, address, nationkey, phone, acctbal, comment) \
                VALUES {}'.format(insertRows)
        th = InsertWorker(query)
        th.start()
        ths.append(th)
  for th in ths:
    th.join()

def get_suppliers():
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      cur.execute('SELECT suppkey FROM `supplier`')
      return [item[0] for item in cur.fetchall()]

def create_parts():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generation and inserting `part` data")
      for part in np.arange(int(TOTALPARTS/ROWSPERINSERT)):
        rows = [[
          mimefinance.stock_name()[:55],
          mimerandom.generate_string_by_mask(mask="Manufacturer####", digit='#'),
          mimerandom.generate_string_by_mask(mask="Brand####", digit='#'),
          random.choice(PARTTYPES),
          mimenumeric.integer_number(start=0, end=99),
          random.choice(CONTAINERTYPES),
          round(mimenumeric.decimal_number(start=0.00,end=999.00),2),
          mimetext.sentence()[:23]
         ] for x in np.arange(ROWSPERINSERT)]

        insertRows = (','.join('("{}", "{}", "{}", "{}", {}, "{}", {}, "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows))
        
        print("Inserting records {}/{}".format((part + 1) * ROWSPERINSERT, TOTALPARTS));
        query = ' \
                INSERT INTO `part` (name, mfgr, brand, type, size, container, retailprice, comment) \
                VALUES {}'.format(insertRows)
        th = InsertWorker(query)
        th.start()
        ths.append(th)
  for th in ths:
    th.join()

def get_parts():
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      cur.execute('SELECT partkey FROM `part`')
      return [item[0] for item in cur.fetchall()]

def create_partSupplier():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generation and inserting `partsupp` data")
      if PARTS == None or len(PARTS) == 0 :
        exit("ERROR: Unable to retrieve data from `part` table. Exiting...")
      if SUPPLIERS == None or len(SUPPLIERS) == 0:
        exit("ERROR: Unable to retrieve data from `supplier` table. Exiting...")
      for part in np.arange(int(TOTALPARTSSUPPLIERS/ROWSPERINSERT)):
        rows = [[
          random.choice(PARTS),
          random.choice(SUPPLIERS),
          mimenumeric.integer_number(start=0, end=9999),
          round(mimenumeric.decimal_number(start=0.00,end=999.00),2),
          mimetext.sentence()[:50]
         ] for x in np.arange(ROWSPERINSERT)]
         
        insertRows = (','.join('({}, {}, {}, {}, "{}")'.format(row[0], row[1], row[2], row[3], row[4]) for row in rows))
        print("Inserting records {}/{}".format((part + 1) * ROWSPERINSERT, TOTALPARTSSUPPLIERS))
        query = ' \
          INSERT INTO `partsupp` (partkey, suppkey, availqty, supplycost, comment) \
          VALUES {} \
          ON DUPLICATE KEY UPDATE availqty = availqty + 1'.format(insertRows)
        th = InsertWorker(query)
        th.start()
        ths.append(th)
  for th in ths:
    th.join()

def get_nations():
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      cur.execute('SELECT nationkey FROM nation')
      return [item[0] for item in cur.fetchall()]

def create_customers():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generating and inserting `customer` data")
      for customer in np.arange(int(TOTALCUSTOMERS/ROWSPERINSERT)):
        th = InsertCustomer(customer)
        th.start()
        ths.append(th)
  for th in ths:
    th.join()

def get_customers():
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      cur.execute('SELECT custkey FROM customer')
      return [item[0] for item in cur.fetchall()]

def create_orders():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generating and inserting `orders` data")
      cur.execute('SELECT custkey FROM customer')
      customers = [item[0] for item in cur.fetchall()]
      for order in np.arange(int(TOTALORDERS/ROWSPERINSERT)):
        th = InsertOrder(order)
        th.start()
        ths.append(th)
  for th in ths:
    th.join()


def create_lineitem():
  ths = []
  with get_connection(DATABASE) as conn:
    with conn.cursor() as cur:
      print("Generating and inserting `lineitem` data")
      # let's get only orders with no lines
      cur.execute('SELECT * \
                  FROM orders \
                  LEFT JOIN lineitem ON lineitem.orderkey = orders.orderkey \
                  WHERE lineitem.orderkey IS NULL;')
      orders = [item[0] for item in cur.fetchall()]
      currentOrder = 0
      while True:
        if currentOrder >= len(orders) :
          print("No orders to create lines...")
          break
        rows = []
        for i in np.arange(ROWSPERINSERT/LINEITEMMIN):
          maxLineItem = random.randint(LINEITEMMIN, LINEITEMMAX)
          orderkey = [orders[currentOrder] for x in np.arange(maxLineItem)]
          partkey = [random.choice(PARTS) for x in np.arange(maxLineItem)]
          suppkey = [random.choice(SUPPLIERS) for x in np.arange(maxLineItem)]
          linenumber = np.arange(maxLineItem)
          quantity = mimenumeric.integers(start=1, end=9999, n=maxLineItem)
          extendedprice = [round(mimenumeric.decimal_number(start=0.00,end=99999.00),2)  for x in np.arange(maxLineItem)]
          discount = [round(mimenumeric.decimal_number(start=0.00,end=9.99),2) for x in np.arange(maxLineItem)]
          tax = [round(mimenumeric.decimal_number(start=0.00,end=9.99),2) for x in np.arange(maxLineItem)]
          returnflag = [mimerandom.generate_string_by_mask(mask="@") for x in np.arange(maxLineItem)]
          linestatus = [mimerandom.generate_string_by_mask(mask="@") for x in np.arange(maxLineItem)]
          shipdate = [mimedate.date(start=2010,end=2023) for x in np.arange(maxLineItem)]
          commitdate = [mimedate.date(start=2010,end=2023) for x in np.arange(maxLineItem)]
          receiptdate = [mimedate.date(start=2010,end=2023) for x in np.arange(maxLineItem)]
          shipinstruct = [mimetext.level() for x in np.arange(maxLineItem)]
          shipmode = [mimetext.color() for x in np.arange(maxLineItem)]
          comment = [mimetext.sentence()[:40] for x in np.arange(maxLineItem)]
          lineorder = list(zip(
            orderkey,
            partkey, suppkey, linenumber, quantity, extendedprice, discount, tax, returnflag, linestatus, shipdate, commitdate, receiptdate, 
            shipinstruct, shipmode, comment
          ))
          rows = rows + lineorder
          currentOrder += 1

        if len(rows) == 0:
          break
        print("Inserting records. Orders missing %s" % (len(orders) - currentOrder))
        insertRows = (",".join('({}, {}, {}, {}, {}, {}, {}, {}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]) for row in rows))
        query = ' \
          INSERT INTO `lineitem` (orderkey, partkey, suppkey, linenumber, quantity, extendedprice, discount, tax, returnflag, linestatus, shipdate, commitdate, receiptdate, shipinstruct, shipmode, comment) \
          VALUES {}'.format(insertRows)
        th = InsertWorker(query)
        th.start()
        ths.append(th)
        # exit cycle
        if currentOrder >= len(orders) :
          break
  for th in ths:
    th.join()

def main():
  test_connection()

  if not ONLYORDERS:
    create_database()
    create_suppliers()
  global NATIONS
  NATIONS = get_nations()
  
  global SUPPLIERS
  SUPPLIERS = get_suppliers()

  if not ONLYORDERS:
    create_parts()
  global PARTS
  PARTS = get_parts()

  if not ONLYORDERS: 
    create_partSupplier()
    create_customers()
  global CUSTOMERS
  CUSTOMERS = get_customers()

  create_orders()
  create_lineitem()

  print("Data generation finished with success.")

if __name__ == "__main__":
  main()


        

