from src.georecl.geoserver import Geoserver

client=Geoserver(url='localhost:3000/geoserver',username='admin',password='geoserver')

print(client.get_status())

