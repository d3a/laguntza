# Utilidades paa manupular cadenas

## cut

Procesa líneas separando campos por un delimitador dado.

```cut [-s] -d'<separador>' -f<campos> <fichero>```

```cut -c<caracteres>|-b<bytes> <fichero>```

```-s``` Solo muestra las líneas en las que haya separador

```bash
  VAR1="c1:c2:c3:c4:c5"
  VAR2="123456789"
  
  echo ${VAR1} | cut -d':' -f 1
  # c1
  echo ${VAR1} | cut -d':' -f 1,5
  # c1:c5
  echo ${VAR1} | cut -d':' -f 2-3
  # c2:c3:c4

  echo ${VAR2} | cut -c 2
  # 2
  echo ${VAR2} | cut -c 1,5,7
  # 157
  echo ${VAR2} | cut -c 4-8
  # 45678
``` 
