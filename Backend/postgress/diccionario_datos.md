# Diccionario e Datos

## Tablas
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY 1;
```

## Columnas
```sql
SELECT
  column_name,
  data_type,
  is_nullable
FROM information_schema.columns
WHERE table_name = '<nombre_tabla>';
```
