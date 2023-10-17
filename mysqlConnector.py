import pymysql

class mysqlConnector:

    db_setting = {
        
    }

    def __init__(self):
        self.conn = pymysql.connect(**self.db_setting)
        print("DB connect sucessfully")

    def __del__(self):
        self.conn.cursor.close()
        self.conn.close()
        print("DB disconnect")

    def CreateClient(self, client):
        try:
            with self.conn.cursor() as cursor:
                #檢查客戶是否存在
                check_command = "SELECT client FROM clients WHERE clients.client = %s"
                cursor.execute(check_command, client[0])
                existing_client = cursor.fetchone()

                if existing_client:
                    print("更新客戶資訊")
                    update_command = "UPDATE clients SET contact_info = %s, address = %s WHERE client = %s"
                    cursor.execute(update_command, (client[1], client[2], client[0]))
                else:
                    insert_command = "INSERT INTO clients(client, contact_info, address) VALUES (%s, %s, %s)"
                    cursor.execute(insert_command, (client[0], client[1], client[2]))
                self.conn.commit()
        except Exception as ex:
            print(ex)
            self.conn.rollback()

    def CreateOrder(self, orderID, client):
        try:
            with self.conn.cursor() as cursor:
                check_command = "SELECT order_id FROM orders WHERE order_id = %s"
                cursor.execute(check_command, orderID)
                existing_order = cursor.fetchone()

                #檢查訂單是否存在
                if existing_order:
                    print("該筆訂單已存在")
                else:
                    #每次都會先檢查是否存在客戶，所以這裡不需要檢查客戶是否存在
                    insert_command = "INSERT INTO orders(order_id, client) VALUES (%s, %s)"
                    cursor.execute(insert_command, (orderID, client))
            self.conn.commit()
        except Exception as ex:
            print(ex)
            self.conn.rollback()