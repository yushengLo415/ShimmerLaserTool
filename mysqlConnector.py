import pymysql
from datetime import date
import json

class mysqlConnector:
      
    def __init__(self):
        try:
            with open('db_setting.json', 'r') as json_file:
                self.db_setting = json.load(json_file)
            self.conn = pymysql.connect(**self.db_setting)
            print("連線成功")
        except pymysql.MySQLError as e:
            print("連線失敗，請重新設定資料庫")

    def Disconnect(self):
        self.conn.close()
        print("Disconnect")

    def CreateClient(self, client):
        try:
            self.client = client
            with self.conn.cursor() as cursor:
                #檢查客戶是否存在
                check_command = "SELECT client FROM clients WHERE clients.client = %s"
                cursor.execute(check_command, self.client[0])
                existing_client = cursor.fetchone()

                if existing_client:
                    print("更新客戶資訊")
                    update_command = "UPDATE clients SET contact_info = %s, address = %s WHERE client = %s"
                    cursor.execute(update_command, (self.client[1], self.client[2], self.client[0]))
                else:
                    insert_command = "INSERT INTO clients(client, contact_info, address) VALUES (%s, %s, %s)"
                    cursor.execute(insert_command, (self.client[0], self.client[1], self.client[2]))
                self.conn.commit()
        except Exception as ex:
            print(ex)
            self.conn.rollback()

    def CreateOrder(self, orderID):
        try:
            self.orderID = orderID
            with self.conn.cursor() as cursor:
                check_command = "SELECT order_id FROM orders WHERE order_id = %s"
                cursor.execute(check_command, self.orderID)
                existing_order = cursor.fetchone()

                #檢查訂單是否存在
                if existing_order:
                    print("該筆訂單已存在")
                else:
                    #每次都會先檢查是否存在客戶，所以這裡不需要檢查客戶是否存在
                    insert_command = "INSERT INTO orders(order_id, client) VALUES (%s, %s)"
                    cursor.execute(insert_command, (orderID, self.client[0]))
            self.conn.commit()
        except Exception as ex:
            print(ex)
            self.conn.rollback()

    def CreateProducts(self, productList):
        try:
            with self.conn.cursor() as cursor:
                check_command = "SELECT product_id FROM products WHERE product_id = %s and order_id = %s"
                for product in productList:
                    cursor.execute(check_command, (product.GetName(), self.orderID))
                    existing_product = cursor.fetchone()

                    if existing_product:
                        print("更新product資訊")
                        update_command = "UPDATE products SET count = %s, type = %s, date = %s WHERE product_id = %s and order_id = %s"
                        cursor.execute(update_command, (product.GetCount(), product.GetTypeInString(), str(date.today()), product.GetName(), self.orderID))
                        update_command = "UPDATE metalSheet SET area = %s, thickness = %s, unit_price = %s WHERE product_id = %s"
                        cursor.execute(update_command, (product.GetMetalSheet().GetArea(), product.GetMetalSheet().GetThickness(), product.GetMetalSheet().GetUnitPrice(), product.GetName()))
                        update_command = "UPDATE laser_info SET length = %s, large_holes = %s, tiny_holes = %s WHERE product_id = %s"
                        cursor.execute(update_command, (product.GetLaserInfo().GetLength(), product.GetLaserInfo().GetLargeHolesCount(), product.GetLaserInfo().GetTinyHolesCount(), product.GetName()))
                    else:
                        insert_command = "INSERT INTO products(product_id, order_id, count, type, date) VALUES (%s, %s, %s, %s, %s)"
                        cursor.execute(insert_command, (product.GetName(), self.orderID, product.GetCount(), product.GetTypeInString(), str(date.today())))
                        insert_command = "INSERT INTO metalSheet(product_id, area, thickness, unit_price) VALUES(%s, %s, %s, %s)"
                        cursor.execute(insert_command, (product.GetName(), product.GetMetalSheet().GetArea(), product.GetMetalSheet().GetThickness(), product.GetMetalSheet().GetUnitPrice()))
                        insert_command = "INSERT INTO laser_info(product_id, length, large_holes, tiny_holes) VALUES(%s, %s, %s, %s)"
                        cursor.execute(insert_command, (product.GetName(), product.GetLaserInfo().GetLength(), product.GetLaserInfo().GetLargeHolesCount(), product.GetLaserInfo().GetTinyHolesCount()))
            self.conn.commit()
        except Exception as ex:
            print(ex)
            self.conn.rollback()