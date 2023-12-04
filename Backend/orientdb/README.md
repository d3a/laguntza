# OrientDB

## Connect
```bash
  # Variables para OrinetDB
  orientdb_base: "<carpeta base del producto>"

  # Variables para la consola OrinetDB
  orientdb_home: "${orientdb_base}/<carpeta raiz del producto>"
  orientdb_jar: "${orientdb_home}/orient-console.jar"
  orientdb_cmd: "java -jar \"${orientdb_jar}\""

  # Variables para la base de datos local
  orientdb_data: "${orientdb_base}/<carpeta de datos de la bbdd>"
  orientdb_db: "${orientdb_data}/component"
  orientdb_user: "<usuario>" #admin
  orientdb_pass: "<clave>"

  # Variable para la conexión a la base de datos local
  orientdb_sql_connect: "connect plocal:${orientdb_db} ${orientdb_user} ${orientdb_pass};"

  ${orientdb_cmd} "${orientdb_sql_connect}"
```
