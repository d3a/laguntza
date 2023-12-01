# Snippets

## Cast
```sql
SELECT cast(<cadena> as integer);
```

## Fechas
```sql
SELECT current_date + <n> * interval '1 <periodo>'
```
periodo:
- hour
- day
- month
- year

## Expresiones Regulares
```sql
SELECT regexp_replace(<cadena>, '<patron>(variable)<patron>', '\1')
```
