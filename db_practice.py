# import pyodbc
#
# server = 'ALLENCHEN'
# database = 'Test'
# username = 'allen'
# password = '123'
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()
#
# cursor.execute("INSERT INTO [dbo].[Web] ([Title] ,[Url]) VALUES (?, ?)", articleTitle, articleUrl)
# cnxn.commit()