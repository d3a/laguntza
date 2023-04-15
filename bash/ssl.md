# SSL

## Claves Privadas

Clave privada RSA condificación PEM

(sin encriptación / -des3: con encriptación DES3 / -aes256: con encriptación AES256)

```openssl genrsa [-des3 | -aes256] -out clave_rsa.pem.key 2048```

Cambiar codificación de clave privada RSA

```openssl genrsa -in clave_rsa.pem.key [-des3 | -aes256] -out nueva_clave_rsa.pem.key```

Clave pública con condificación PEM desde clave privada RSA

```openssl rsa -in clave_rsa.pem.key -pubout -outform PEM -out clave_pub.pem```

---
## Petición Técnica

Comando general

```openssl req -new -sha256 -key fich.key -out fich.csr```

Comando que genera la private key

```openssl req -new -newkey rsa:2048 -nodes -out request.csr -keyout private.key```

Comando general con datos

```openssl req -new -sha256 -key fich.key -out fich.csr  -subj "/C=XX/ST=State/L=Location/O=Organization/OU=OrganizationUnit/CN=common_name"```

Usando fichero de configuración

```openssl req -new -sha256 -key fich.key -out fich.csr -config fich.cnf```

Usando otro certificado

```openssl x509 -x509toreq -in certificado_muestra.pem.cer  -signkey clave_privada.key -out request.csr```


---
## Certificados

### Información

Toda la información de un certificado

```openssl x509 -in certificado.pem.cer -text```

Información del certificado

```openssl x509 -in certificado.pem.cer -noout -<opcion>```
- ```text``` Todos los campos
- ```subject``` DN del titular
- ```issuer``` DN del emisor
- ```purpose``` Propositos del certificado
- ```serial``` Número de serie
- ```dates``` Fechas inicio y fin de vigencia
- ```startdate``` Fecha inicio vigencia
- ```enddate``` Fecha fin de vigencia

Informacion de certificado remoto

```openssl s_client -host dominio.con.certificado -port 443 -showcerts 2>&1 | openssl x509 -noout -text```

### Conversiones

PEM -> DER 

```openssl x509 -outform der -in certificate.pem -out certificate.der```

DER -> PEM 

```openssl x509 -inform der -in certificate.cer -out certificate.pem```

PEM -> P7B 

```openssl crl2pkcs7 -nocrl -certfile certificate.cer -out certificate.p7b -certfile CACert.cer```

P7B -> PEM 

```openssl pkcs7 -print_certs -in certificate.p7b -out certificate.cer```

CA/KEY/PEM -> P12

```openssl pkcs12 -export -certfile CACert.crt -inkey privateKey.key -in certificate.crt -out certificate.p12```

P12 -> PEM/KEY

```
openssl pkcs12 -in certificate.pfx -nokeys -clcerts -out certificate.pem.cer
openssl pkcs12 -in certificate.pfx -nocerts -nodes -out certificate.key
```

Crear X5C

```base64 -w 0 certificado_pem_o_der.cer > cadena_x5c.x5c```

---
## Comprobacion clave privada/petición técnica/certificados
```bash
openssl pkey -pubout -in .\private.key | openssl sha256
openssl req -pubkey -in .\request.csr -noout | openssl sha256
openssl x509 -pubkey -in .\certificate.crt -noout | openssl sha256
```

---
## Almacenes de Certificados
Mostrar Información

```keytool -list [-v]  -keystore almacen_certificados -storepass password```

Cambiar clave

```keytool -storepasswd -keystore almacen_certificados```

Importar Certificado

```keytool -import [-noprompt] [-trustcacerts] -alias alias_certificado -file certificado.cer -keystore almacen_certificados -storepass password```

Extraer Certificado

```keytool -export -keystore almacen_certificados -storepass password -trustcacerts -alias alias_certificado -file fichero_destino.cer```

Borrar Certificado

```keytool -delete -keystore almacen_certificados -storepass changeitpassword -alias alias_certificado```
