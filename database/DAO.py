from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Borough as borgo
from nyc_wifi_hotspot_locations nwhl 
"""
        cursor.execute(query, )
        for row in cursor:
            result.append(row["borgo"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(borgo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select nwhl.NTACode as codice
from nyc_wifi_hotspot_locations nwhl 
where nwhl.Borough = %s 
"""
        cursor.execute(query, (borgo, ))
        for row in cursor:
            result.append(row["codice"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPesoArchi(n1, n2):
        conn = DBConnect.get_connection()

        result = []
        part1 = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from (select tab.codice as codici1
                    from (select nwhl.SSID as codice 
                    from nyc_wifi_hotspot_locations nwhl 
                    where nwhl.NTACode = %s) as tab) as tabella1 union (select tab.codice as codici2
                    from (select nwhl.SSID as codice 
                    from nyc_wifi_hotspot_locations nwhl 
                    where nwhl.NTACode = %s) as tab)
        """
        cursor.execute(query, (n1, n2))
        for row in cursor:
            print(len(row["codici1"]), row["codici1"])
            result.append(row["codici1"])
        part1.append(result)
        print(part1)
        cursor.close()
        conn.close()
        return len(part1[0])
