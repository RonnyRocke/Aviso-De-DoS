import socket
import os
import sys

def verificar_ddos_alvo(endereco):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((endereco, 80))
        mensagem = "GET / HTTP/1.1\r\nHost: " + endereco + "\r\n\r\n"
        sock.send(mensagem.encode())
        resposta = sock.recv(2048).decode()
        sock.close()

        if "HTTP/1.1 200 OK" in resposta:
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
            print("TUDO CERTO COM A REDE")
        else:
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
            print("Tudo certo com a rede")
    except socket.error:
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")
        print("IP OU REDE ESTÁ SENDO ATACADA POR NEGAÇÃO DE SERVIÇO!.")

endereco = input("Digite o IP ou site a ser verificado: ")
verificar_ddos_alvo(endereco)

