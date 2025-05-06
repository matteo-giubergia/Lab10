from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        res= []

        query=""" select distinct CCode, StateAbb, StateNme
                    from country c, contiguity co
                    where co.state1no = c.CCode and co.conttype = 1 and co.`year` <= %s """
        cursor.execute(query, (anno,))

        for row in cursor:
            res.append(Country(row['CCode'], row['StateAbb'], row['StateNme']))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        res= []

        query="""  """
        cursor.execute(query, (anno,))

        for row in cursor:
            res.append()

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []

        query = """ select * 
                     from country c  """
        cursor.execute(query, )

        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        conn.close()
        return res

