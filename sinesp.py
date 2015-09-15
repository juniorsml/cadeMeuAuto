#coding: utf-8
import socket
import random, math
from hashlib import sha1
from hmac import new as hmac

generateHash = lambda(placa): hmac("shienshenlhq",placa,sha1).digest().encode('hex')

rLong = -38.6791411

rLat = -3.6770324

pacote = lambda(placa): 'POST /sinesp-cidadao/ConsultaPlacaNovo27032014 HTTP/1.1\nHost: sinespcidadao.sinesp.gov.br\nContent-Length: %d\nContent-Type: application/x-www-form-urlencoded; charset=UTF-8\nAccept: text/plain, */*; q=0.01\nx-wap-profile: http://wap.samsungmobile.com/uaprof/GT-S7562.xml\nUser-Agent: Mozilla/5.0 (Linux; U; Android 4.1.4; pt-br; GT-S1162L Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30\nAccept-Encoding: gzip,deflate\nAccept-Language: pt-BR, en-US\nAccept-Charset: utf-8, iso-8859-1, utf-16, gb2312, gbk, *;q=0.7\n\n%s' % ( len(payload(placa)), payload(placa) ) 

payload = lambda(placa): '<?xl version="1.0" encoding="utf-8" standalone="yes" ?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" ><soap:Header><dispositivo>GT-S1312L</dispositivo><nomeSO>Android</nomeSO><versaoAplicativo>1.1.1</versaoAplicativo><versaoSO>4.1.4</versaoSO><aplicativo>aplicativo</aplicativo><ip>177.206.169.90</ip><token>%s</token><latitude>%s</latitude><longitude>%s</longitude></soap:Header><soap:Body><webs:getStatus xmlns:webs="http://soap.ws.placa.service.sinesp.serpro.gov.br/"><placa>%s</placa></webs:getStatus></soap:Body></soap:Envelope>' % (generateHash(placa),rLat,rLong, placa)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("sinespcidadao.sinesp.gov.br", 80))
pack =  pacote('faa4716')
s.send(pacote('faa1716'))
print s.recv(1024)
print pack
s.close()
