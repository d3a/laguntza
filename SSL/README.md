# SSL

## Claves Privadas
#### Clave privada RSA condificación PEM
(sin encriptación / -des3: con encriptación DES3 / -aes256: con encriptación AES256)

```openssl genrsa [-des3 | -aes256] -out clave_rsa.pem.key 2048```

#### Cambiar codificación de clave privada RSA
```openssl genrsa -in clave_rsa.pem.key [-des3 | -aes256] -out nueva_clave_rsa.pem.key```

#### Clave pública con condificación PEM desde clave privada RSA
```openssl rsa -in clave_rsa.pem.key -pubout -outform PEM -out clave_pub.pem```

## Petición Técnica
#### Comando general
```openssl req -new -sha256 -key fich.key -out fich.csr```
#### Comando que genera la private key
```openssl req -new -newkey rsa:2048 -nodes -out request.csr -keyout private.key```
#### Comando general con datos
```openssl req -new -sha256 -key fich.key -out fich.csr  -subj "/C=XX/ST=State/L=Location/O=Organization/OU=OrganizationUnit/CN=common_name"```
#### Usando fichero de configuración
```openssl req -new -sha256 -key fich.key -out fich.csr -config fich.cnf```


## Certificados
### Conversiones
#### PEM -> DER 
```openssl x509 -outform der -in certificate.pem -out certificate.der```
#### DER -> PEM 
```openssl x509 -inform der -in certificate.cer -out certificate.pem```
#### PEM -> P7B 
```openssl crl2pkcs7 -nocrl -certfile certificate.cer -out certificate.p7b -certfile CACert.cer```
#### P7B -> PEM 
```openssl pkcs7 -print_certs -in certificate.p7b -out certificate.cer```
#### CA/KEY/PEM -> P12
```openssl pkcs12 -export -certfile CACert.crt -inkey privateKey.key -in certificate.crt -out certificate.p12```
#### PFX -> PEM 
```openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes```
#### Crear X5C
```base64 -w 0 certificado_pem_o_der.cer > cadena_x5c.x5c```

### Almacenes de Certificados
#### Mostrar Información
```keytool -list [-v]  -keystore almacen_certificados -storepass password```
#### Cambiar clave
```keytool -storepasswd -keystore almacen_certificados```
#### Importar Certificado
```keytool -import [-noprompt] [-trustcacerts] -alias alias_certificado -file certificado.cer -keystore almacen_certificados -storepass password```
#### Extraer Certificado
```keytool -export -keystore almacen_certificados -storepass password -trustcacerts -alias alias_certificado -file fichero_destino.cer```
#### Borrar Certificado
```keytool -delete -keystore almacen_certificados -storepass changeitpassword -alias alias_certificado```
